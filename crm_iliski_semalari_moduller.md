# CRM Iliski Semalari - Moduler

- Uretim tarihi: 2026-02-12 11:23:30
- Kaynak: `crm_veri_sozlugu.csv`
- Diyagram formati: Mermaid ER
- Audit FK filtreleri: `CreatedBy, DeletedBy, UpdatedBy`

## Moduller

| Modul | Tablolar | Dis Referans Tablo | Ic Iliski | Moduller Arasi Iliski | Dosya |
|---|---:|---:|---:|---:|---|
| Kullanici, Organizasyon ve Yetki | 59 | 44 | 63 | 83 | `crm_iliski_semasi_modul_01_kullanici_organizasyon_yetki.mmd` |
| Musteri, Lead ve Pazarlama | 16 | 18 | 9 | 28 | `crm_iliski_semasi_modul_02_musteri_lead_pazarlama.mmd` |
| Satis, Teklif ve Sozlesme | 36 | 34 | 25 | 53 | `crm_iliski_semasi_modul_03_satis_teklif_sozlesme.mmd` |
| Teslimat, Operasyon ve Kalite | 44 | 16 | 23 | 50 | `crm_iliski_semasi_modul_04_teslimat_operasyon_kalite.mmd` |
| Finans, Mortgage ve Tahsilat | 35 | 10 | 11 | 21 | `crm_iliski_semasi_modul_05_finans_mortgage_tahsilat.mmd` |
| Sistem, Entegrasyon ve Ayarlar | 23 | 7 | 1 | 17 | `crm_iliski_semasi_modul_06_sistem_entegrasyon_ayarlar.mmd` |

## Kullanim

1. Istegin modulu sec
2. Ilgili `.mmd` dosyasini https://mermaid.live uzerine yapistir
3. PNG/SVG export et

> Not: Tum iliskilerin tamamini gormek icin `crm_iliski_semasi.mmd` dosyasini kullanabilirsin.
