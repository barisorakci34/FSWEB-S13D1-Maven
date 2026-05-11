# ITSM TKBB Gunluk OPS Otomasyon Analiz Notu

Bu dokuman, `itsm_tkbb_daily_ops_flow.drawio` dosyasindaki akis icin analist ozeti ve uygulama kurallarini tarif eder.

## Amac

ITSM uzerinde gunluk calisan bir task ile TKBB BankApi basvurularini otomatik izlemek, belirli basvuru durumlarinda OPS ekibine ITSM taski ve e-posta uretmek, OPS cevabini yine ITSM uzerinden alip ilgili TKBB servisini cagirmak.

## Ana akis

1. ITSM scheduler gunluk job'u baslatir.
2. Entegrasyon servisi konfigurasyon, SLA esikleri ve acik ITSM tasklarini okur.
3. `LoginBank` ile token alinir.
4. `BankService` veya `GetApplicantPaginatedList` ile aksiyon bekleyen basvurular cekilir.
5. Acik ITSM kayitlari icin `ApplicantsStatusCheck` ile guncel durum senkronize edilir.
6. Kayitlar `applicantNumber` ile tekillestirilir ve status/SLA kurallari uygulanir.
7. Aksiyon gerektiren durumlarda ITSM taski create/update edilir, belgeler eklenir, OPS'e alert ve e-posta gonderilir.
8. OPS yanitini ITSM taskina ekler.
9. ITSM otomasyonu yanit tipine gore TKBB bilgi guncelleme veya kapanis bildirim servisini cagirir.

## Durum bazli aksiyon matrisi

| Durum | Anlam | ITSM aksiyonu | OPS alert | Servis aksiyonu |
| --- | --- | --- | --- | --- |
| 40 | Basvuru Banka Gonderim Listesinde | Yeni task ac/guncelle | P3 | Banka isleme aldi bildirimi icin `PUT /BankService` |
| 50 | Basvuru Bankaya Gonderildi | Task ac/guncelle | P3 | OPS inceleme taski |
| 80 | Banka ek bilgi gonderim listesinde | Ek bilgi taski, beklenen belge alanlari | P2 | OPS cevabi hazir olunca `POST /BankService` bilgi guncelleme |
| 82 | Ara karar verilen basvuru | Ara karar taski, karar metni ve ekler | P2/P1 | Gereken cevap/belge servisi cagrilir |
| 121 | Hakem Heyeti karari bankaya iletildi | Karar uygulama taski | P1 | OPS is aksiyonundan sonra `POST /ApplicantClosingNotice` |
| 122 | Geciken islem bildirimi | Eskalasyon taski | P1 + yonetici maili | Gecikme kapanana kadar tekrar alert |
| 123 | Kapanan basvuru | ITSM taskini kapat | Yok | Sadece senkronizasyon |

## ITSM task alanlari

- `applicantNumber` ve `applicantNo`
- TKBB status kodu ve aciklamasi
- `bankResponseEndDate` ve SLA kalan sure
- Basvuru konusu, mesaj ve beklenen belge tipleri
- OPS atama grubu, oncelik, alarm seviyesi
- OPS cevap metni
- OPS yukledigi dokumanlar
- Cagrilacak servis tipi: bilgi guncelleme veya kapanis bildirimi
- Entegrasyon sonuc kodu ve hata mesaji

## E-posta/alert icerigi

- Basvuru numarasi ve ITSM task linki
- TKBB status kodu/aciklamasi
- Son cevap tarihi ve SLA durumu
- Beklenen OPS aksiyonu
- Gerekli dokuman listesi
- Hata/eskalasyon varsa teknik sonuc kodu

## Hata yonetimi

- HTTP `401/403`: token veya yetki problemi olarak teknik OPS alert'i acilir.
- HTTP `400/404`: veri veya endpoint kontrolu icin entegrasyon incident'i acilir.
- HTTP `500`: retry loglanir, tekrar eden hata icin OPS teknik alert'i uretilir.
- `resultCode 101/102/104`: basvuru/veri islenemedi seklinde ITSM kaydina yazilir.
- `resultCode 103`: basvuru cevabi isleme alindi olarak basarili sonuc kaydedilir.

## Tasarim notlari

- Tekillik anahtari `applicantNumber` olmalidir; ayni basvuru icin tekrar task acilmamali, mevcut task guncellenmelidir.
- OPS yaniti ITSM uzerinden alinmali; mail yaniti kaynak sistem olarak kabul edilmemelidir.
- 122 durumunda alarm seviyesi otomatik P1'e yukseltilmeli ve yonetici dagitim listesine eskalasyon yapilmalidir.
- 10 MB ustu dokumanlar icin once dokuman listesi, sonra `GetApplicantDocumentFile` ile dosya cekilmelidir.
