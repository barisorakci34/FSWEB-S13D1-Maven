# CRM Iliski Semalari - Moduler

- Uretim tarihi: 2026-02-12 11:23:30
- Kaynak: `crm_veri_sozlugu.csv`
- Diyagram formati: Mermaid ER
- Audit FK filtreleri: `CreatedBy, DeletedBy, UpdatedBy`
- Bu klasorde ayni adlarla `.png` ciktilari da uretildi.

## Moduller

| Modul | Tablolar | Dis Referans Tablo | Ic Iliski | Moduller Arasi Iliski | Mermaid Dosyasi | PNG Dosyasi |
|---|---:|---:|---:|---:|---|---|
| Kullanici, Organizasyon ve Yetki | 59 | 44 | 63 | 83 | `crm_iliski_semasi_modul_01_kullanici_organizasyon_yetki.mmd` | `crm_iliski_semasi_modul_01_kullanici_organizasyon_yetki.png` |
| Musteri, Lead ve Pazarlama | 16 | 18 | 9 | 28 | `crm_iliski_semasi_modul_02_musteri_lead_pazarlama.mmd` | `crm_iliski_semasi_modul_02_musteri_lead_pazarlama.png` |
| Satis, Teklif ve Sozlesme | 36 | 34 | 25 | 53 | `crm_iliski_semasi_modul_03_satis_teklif_sozlesme.mmd` | `crm_iliski_semasi_modul_03_satis_teklif_sozlesme.png` |
| Teslimat, Operasyon ve Kalite | 44 | 16 | 23 | 50 | `crm_iliski_semasi_modul_04_teslimat_operasyon_kalite.mmd` | `crm_iliski_semasi_modul_04_teslimat_operasyon_kalite.png` |
| Finans, Mortgage ve Tahsilat | 35 | 10 | 11 | 21 | `crm_iliski_semasi_modul_05_finans_mortgage_tahsilat.mmd` | `crm_iliski_semasi_modul_05_finans_mortgage_tahsilat.png` |
| Sistem, Entegrasyon ve Ayarlar | 23 | 7 | 1 | 17 | `crm_iliski_semasi_modul_06_sistem_entegrasyon_ayarlar.mmd` | `crm_iliski_semasi_modul_06_sistem_entegrasyon_ayarlar.png` |

## Kullanim

1. Istegin modulu sec
2. Hazir PNG lazimsa ilgili `.png` dosyasini ac/indir
3. Mermaid uzerinde duzenleyip tekrar export etmek icin `.mmd` dosyasini https://mermaid.live uzerine yapistir

> Not: Tum iliskilerin tamamini gormek icin `crm_iliski_semasi.mmd` ve onun PNG karsiligi olan `crm_iliski_semasi.png` dosyalarini kullanabilirsin.
