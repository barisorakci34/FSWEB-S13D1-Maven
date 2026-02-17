# CRM Full ER - Readable Package

Bu paket, onceki karisik tek-gorsel yerine katmanli ve okunabilir cikti verir.

## Ozet

- Toplam FK: **719**
- Audit FK (Crm.Users + CreatedBy/UpdatedBy/DeletedBy): **479**
- Business FK (kalan): **240**
- Business graph node: **213**
- Business graph aggregated edge: **223**
- Community diyagram sayisi: **14**
- Audit Users sayfa sayisi: **2**

## Dosyalar

- `00-business-overview-highres.png/.svg`
- `01-business-overview-without-users-highres.png/.svg`
- `community-XX-highres.png/.svg` (modul bazli kume diyagramlari)
- `audit-users-pX-highres.png/.svg` (audit FK'ler ayri)
- `fk-business-pairs.csv`
- `fk-audit-users.csv`
- `communities-summary.csv`

Okuma sirasi: once 00 -> 01 -> community dosyalari -> audit-users sayfalari.
