#!/usr/bin/env python3
"""Generate high-resolution ER diagram assets for Kasbox."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Set, Tuple

import matplotlib.pyplot as plt
import networkx as nx
from openpyxl import load_workbook


@dataclass
class TableInfo:
    schema: str
    table: str
    columns: Set[str]
    pk_columns: List[str]

    @property
    def full_name(self) -> str:
        return f"{self.schema}.{self.table}"


def read_dictionary(input_xlsx: Path) -> Dict[str, TableInfo]:
    wb = load_workbook(input_xlsx, data_only=True, read_only=True)
    ws = wb["Kolonlar"]

    table_columns: Dict[str, Set[str]] = defaultdict(set)
    table_pks: Dict[str, List[str]] = defaultdict(list)
    table_parts: Dict[str, Tuple[str, str]] = {}

    rows = ws.iter_rows(min_row=2, values_only=True)
    for row in rows:
        schema, table, column, _, _, _, is_pk, _, _ = row
        if not (schema and table and column):
            continue
        full = f"{schema}.{table}"
        table_parts[full] = (str(schema), str(table))
        table_columns[full].add(str(column))
        if str(is_pk).strip().lower() == "yes":
            table_pks[full].append(str(column))

    table_infos: Dict[str, TableInfo] = {}
    for full, cols in table_columns.items():
        schema, table = table_parts[full]
        table_infos[full] = TableInfo(
            schema=schema,
            table=table,
            columns=cols,
            pk_columns=table_pks.get(full, []),
        )
    return table_infos


def infer_relationships(tables: Dict[str, TableInfo]) -> List[Tuple[str, str, str, str]]:
    """
    Infer relationships where a column matches a unique single-column PK.

    Returns:
        (source_table, target_table, via_column, confidence)
    """
    single_pk_index: Dict[str, List[str]] = defaultdict(list)
    for full, info in tables.items():
        if len(info.pk_columns) == 1:
            single_pk_index[info.pk_columns[0].upper()].append(full)

    edges: List[Tuple[str, str, str, str]] = []
    seen: Set[Tuple[str, str, str]] = set()

    for source_full, source_info in tables.items():
        source_pk_set = {x.upper() for x in source_info.pk_columns}
        for col in source_info.columns:
            col_u = col.upper()
            if col_u in source_pk_set:
                continue
            targets = [t for t in single_pk_index.get(col_u, []) if t != source_full]
            if len(targets) != 1:
                continue

            target = targets[0]
            confidence = "high" if (col_u.endswith("_ID") or col_u.endswith("ID")) else "medium"
            key = (source_full, target, col)
            if key not in seen:
                edges.append((source_full, target, col, confidence))
                seen.add(key)

    edges.sort(key=lambda x: (x[0], x[1], x[2]))
    return edges


def table_category(full_table_name: str) -> str:
    table = full_table_name.split(".", 1)[1]
    if table.startswith("IBS_"):
        return "IBS"
    if table.startswith("KBAUDIT_"):
        return "KBAUDIT"
    if table.startswith("KBARSIV_"):
        return "KBARSIV"
    if table.startswith("KBFAST"):
        return "KBFAST"
    if table.startswith("KBSIPER"):
        return "KBSIPER"
    if table.startswith("ALL_MSG_") or table.startswith("FROM_") or table.startswith("TO_"):
        return "KAS_MSG"
    if table.startswith("TCMB"):
        return "TCMB"
    if table.startswith("KB"):
        return "KB_GENEL"
    return "DIGER"


def build_graph(
    tables: Dict[str, TableInfo], relationships: List[Tuple[str, str, str, str]]
) -> nx.DiGraph:
    g = nx.DiGraph()
    for full, info in tables.items():
        g.add_node(
            full,
            label=info.table,
            col_count=len(info.columns),
            category=table_category(full),
        )
    for src, dst, via_col, confidence in relationships:
        g.add_edge(src, dst, via=via_col, confidence=confidence)
    return g


def compute_positions(g: nx.DiGraph) -> Dict[str, Tuple[float, float]]:
    undirected = g.to_undirected()
    connected_nodes = [n for n in g.nodes if undirected.degree(n) > 0]
    isolated_nodes = sorted([n for n in g.nodes if undirected.degree(n) == 0])

    pos: Dict[str, Tuple[float, float]] = {}

    if connected_nodes:
        sub = undirected.subgraph(connected_nodes)
        pos_connected = nx.spring_layout(sub, seed=42, k=0.48, iterations=600)
        for node, (x, y) in pos_connected.items():
            pos[node] = (x * 8.0, y * 8.0)
        min_y = min(y for _, y in pos.values())
    else:
        min_y = 0.0

    if isolated_nodes:
        cols = 12
        x_spacing = 1.45
        y_spacing = 1.25
        start_x = -((cols - 1) * x_spacing) / 2
        start_y = min_y - 3.0
        for idx, node in enumerate(isolated_nodes):
            row = idx // cols
            col = idx % cols
            pos[node] = (start_x + col * x_spacing, start_y - row * y_spacing)

    return pos


def draw_graph(g: nx.DiGraph, output_png: Path, output_svg: Path) -> None:
    category_colors = {
        "IBS": "#4C78A8",
        "KBAUDIT": "#F58518",
        "KBARSIV": "#72B7B2",
        "KBFAST": "#54A24B",
        "KBSIPER": "#E45756",
        "KAS_MSG": "#B279A2",
        "TCMB": "#FF9DA6",
        "KB_GENEL": "#9D755D",
        "DIGER": "#BAB0AC",
    }

    pos = compute_positions(g)
    labels = {n: n.split(".", 1)[1] for n in g.nodes}

    node_sizes = []
    node_colors = []
    for n in g.nodes:
        col_count = g.nodes[n]["col_count"]
        node_sizes.append(480 + (col_count * 5))
        node_colors.append(category_colors.get(g.nodes[n]["category"], "#BAB0AC"))

    plt.figure(figsize=(30, 20))
    ax = plt.gca()
    ax.set_axis_off()

    nx.draw_networkx_edges(
        g,
        pos=pos,
        arrows=True,
        arrowstyle="-|>",
        arrowsize=8,
        width=0.8,
        alpha=0.35,
        edge_color="#3B4A5A",
        connectionstyle="arc3,rad=0.04",
    )

    nx.draw_networkx_nodes(
        g,
        pos=pos,
        node_size=node_sizes,
        node_color=node_colors,
        linewidths=0.7,
        edgecolors="#1F2A35",
    )

    nx.draw_networkx_labels(g, pos=pos, labels=labels, font_size=5.8, font_color="#111111")

    table_count = g.number_of_nodes()
    edge_count = g.number_of_edges()
    isolated = sum(1 for n in g.nodes if g.to_undirected().degree(n) == 0)
    plt.title(
        (
            "Kasbox ER Semasi (Yuksek Cozunurluk)\n"
            f"Toplam Tablo: {table_count} | Cikarilan Iliski: {edge_count} | Izole Tablo: {isolated}\n"
            "Not: Iliskiler, SQL scriptte FK tanimi olmadigi icin PK-kolon isim eslesmesi ile cikarildi."
        ),
        fontsize=14,
        pad=16,
    )

    # Legend
    legend_handles = []
    for cat, color in category_colors.items():
        handle = plt.Line2D(
            [0],
            [0],
            marker="o",
            color="w",
            label=cat,
            markerfacecolor=color,
            markeredgecolor="#1F2A35",
            markersize=8,
        )
        legend_handles.append(handle)
    plt.legend(
        handles=legend_handles,
        title="Tablo Gruplari",
        loc="upper right",
        fontsize=8,
        title_fontsize=9,
        framealpha=0.9,
    )

    output_png.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_png, format="png", dpi=420, bbox_inches="tight", pad_inches=0.2)
    plt.savefig(output_svg, format="svg", bbox_inches="tight", pad_inches=0.2)
    plt.close()


def write_relationship_csv(
    relationships: List[Tuple[str, str, str, str]], output_csv: Path
) -> None:
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    with output_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["source_table", "target_table", "via_column", "confidence"])
        writer.writerows(relationships)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Kasbox ER diagram assets.")
    parser.add_argument(
        "--input-xlsx",
        default="docs/kasbox-veri-sozlugu.xlsx",
        help="Input data dictionary xlsx path",
    )
    parser.add_argument(
        "--output-prefix",
        default="docs/kasbox-er-semasi",
        help="Output file prefix (without extension)",
    )
    args = parser.parse_args()

    input_xlsx = Path(args.input_xlsx)
    if not input_xlsx.exists():
        raise FileNotFoundError(f"Input dictionary not found: {input_xlsx}")

    tables = read_dictionary(input_xlsx)
    relationships = infer_relationships(tables)
    graph = build_graph(tables, relationships)

    prefix = Path(args.output_prefix)
    output_png = prefix.with_name(prefix.name + "-highres.png")
    output_svg = prefix.with_name(prefix.name + "-highres.svg")
    output_csv = prefix.with_name(prefix.name + "-iliskiler.csv")

    draw_graph(graph, output_png=output_png, output_svg=output_svg)
    write_relationship_csv(relationships, output_csv)

    print(f"Input: {input_xlsx}")
    print(f"Tables: {len(tables)}")
    print(f"Relationships: {len(relationships)}")
    print(f"PNG: {output_png}")
    print(f"SVG: {output_svg}")
    print(f"CSV: {output_csv}")


if __name__ == "__main__":
    main()
