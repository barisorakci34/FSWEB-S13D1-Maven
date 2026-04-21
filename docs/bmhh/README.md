## BMHH Banka Yazisi Operasyon Onay Akisi

Bu klasorde, yuklenen **BMHHBankaServisleri.pdf** dokumanindaki servisler baz alinarak hazirlanan iki artefakt bulunur:

- `n8n-bmhh-operasyon-onay-workflow.json`  
  n8n'e import edilebilir detayli workflow
- `bmhh-operasyon-onay-akisi.drawio`  
  draw.io ile acilabilir detayli surec diyagrami

### Kapsanan BMHH servisleri

1. `POST /BankApi/LoginBank` - Token alma
2. `POST /BankApi/BankService/GetApplicantPaginatedList` - Sayfali basvuru sorgulama
3. `PUT /BankApi/BankService` - Basvuruyu isleme alindi bildirme
4. `POST /BankApi/BankService/GetApplicantDocuments` - Basvuru dokumanlarini cekme
5. `POST /BankApi/BankService/ApplicantsStatusCheck` - Basvuru durum sorgulama
6. `POST /BankApi/BankService/ApplicantClosingNotice` - Banka aleyhine karar kapanis bildirimi
7. `GET /BankApi/BankService/GetDocumentsTypesList` - Destek/servis saglik kontrolu

### Akis ozeti

- **Ana akis** (15 dakikada bir):
  - Yeni basvuru/yazi listesi cekilir.
  - Status kodlari `40, 50, 80, 82, 121` olan yeni kayitlar filtrelenir.
  - Operasyon ekibine onay maili gider.
  - Onay beklenir (`approvalTimeoutHour`).
  - Onay varsa basvuru isleme alindi bildirimi yapilir.
  - Dokuman kontrolu yapilir; eksikse akis kesilir ve mail atilir.
  - Durum sorgulanir, banka aleyhine karar varsa kapanis bildirimi gonderilir.
  - Bilgilendirme maili gonderilir.

- **Destekleyici akis** (saatlik + X saat kapisi):
  - Her saat tetiklenir, sadece `hour % xHourControl == 0` ise devam eder.
  - Servis saglik kontrolu calisir.
  - Acik kayitlar icin SLA ve bekleyen operasyon onayi kontrol edilir.
  - Kritik gecikmede eskalasyon maili, uyari durumunda periyodik uyari maili gonderilir.
  - Sart saglanmiyorsa bu dongu no-op olarak sonlanir.

### n8n import sonrasi duzenlenecek alanlar

`Konfigurasyon` node'unda:

- `baseUrl` (test/prod ortamina gore)
- `userName`, `password`
- `opsMail`, `bizMail`
- `xHourControl` (ornek: 4)
- `approvalTimeoutHour` (ornek: 3)
- `slaWarnHour` (ornek: 24)

Email node'lari icin SMTP credentials n8n ortaminda tanimli olmalidir.
