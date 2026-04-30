# Çağrı Merkezi Projesi RFP Dokümanı - Düzenlenmiş ve Özetlenmiş Versiyon

**Doküman Tarihi:** 2026-04-28  
**Versiyon:** V1.1  
**Doküman Tipi:** Teklif Talebi (RFP)  
**Konu:** Rol bazlı yetkilendirme, çoklu güvenlik seviyesi yönetimi ve aktif çağrı bazlı ekran erişim kontrolü

## 1. Yönetici Özeti

Bu RFP, mevcut Çağrı Merkezi uygulamasında ekran, buton ve aktif çağrı güvenlik kontrollerinin daha parametrik, ölçeklenebilir, izlenebilir ve operasyon ekipleri tarafından yönetilebilir hale getirilmesi için yazılım tedarikçilerinden teknik ve ticari teklif almak amacıyla hazırlanmıştır.

Proje kapsamında ön yüz ekran tasarımları, frontend geliştirme, backend servis entegrasyonları, Active Directory entegrasyonu, rol bazlı ekran/buton yetki yönetimi, ekran bazlı çoklu güvenlik seviyesi seçimi, aktif çağrı sırasında güvenlik seviyesine göre ekran açılış kontrolü, audit log altyapısı ve test/UAT destekleri beklenmektedir.

Başarı için kritik beklentiler:

- Yetki ve güvenlik konfigürasyonları kod değişikliği olmadan parametrik yönetilebilmelidir.
- Rol bazlı ekran ve buton yetkileri tutarlı, kolay anlaşılır ve auditlenebilir olmalıdır.
- Aktif çağrı sırasında güvenlik seviyesi uyumsuz ekranlara erişim sunucu tarafında engellenmelidir.
- Yeni ekran, aksiyon ve güvenlik seviyesi tanımları minimum kod bağımlılığı ile eklenebilmelidir.
- Tedarikçi; tasarım, geliştirme, test, geçiş, dokümantasyon ve destek kalemlerini net biçimde fiyatlandırmalıdır.

## 2. Dokümanın Amacı

Bu RFP'nin amacı, mevcut Çağrı Merkezi uygulamasında rol bazlı ekran/buton yetkilendirme, çoklu güvenlik seviyesi yönetimi ve aktif çağrı bazlı erişim kontrolünün parametrik, ölçeklenebilir ve auditlenebilir şekilde geliştirilmesi için outsource yazılım tedarikçilerinden teknik ve ticari teklif toplamaktır.

## 3. Arka Plan ve İş İhtiyacı

Mevcut yapıda rol bazlı buton yetki matrisi operasyonel olarak karmaşık ve bakımı zor durumdadır. Güvenlik seviyesi seçimleri ekran bazında tek değer ile sınırlıdır; yeni iş ihtiyacı ise her ekran için birden fazla güvenlik seviyesinin tanımlanabilmesini gerektirmektedir.

Aktif çağrı sırasında ekran erişimi, çağrının güvenlik seviyesi ile ekranın izinli güvenlik seviyeleri karşılaştırılarak standart hale getirilmelidir. Ayrıca konfigürasyon değişiklikleri kod değişikliği gerektirmeden parametrik olarak yönetilebilmeli, kritik değişiklikler audit kayıtlarıyla izlenebilmelidir.

## 4. Proje Kapsamı

### 4.1 Kapsam İçi

- Çağrı merkezi ön yüz ekranlarının UX/UI tasarımı.
- Frontend geliştirme faaliyetleri.
- Backend servisleri ile entegrasyon (yaklaşık 20 endpoint).
- Active Directory (AD) entegrasyonu.
- Rol bazlı ekran erişim matrisi yönetimi.
- Rol bazlı buton yetki matrisi UX dönüşümü:
  - Rol seçimi,
  - Accordion yapısı,
  - Aksiyon bazında açık/kapalı toggle,
  - Kullanıcı dostu doğrulama ve uyarı mesajları.
- Ekran bazlı güvenlik seviyesi modelinin tekli seçimden çoklu seçime dönüştürülmesi.
- Aktif çağrı güvenlik seviyesi ile ekran erişim kuralının kontrol edilmesi.
- Tüm kuralların parametrik yapıda yönetilmesi.
- Audit log, izlenebilirlik ve raporlama temelinin oluşturulması.
- Birim, entegrasyon, regresyon ve UAT destekleri.
- Fimple ve SIP entegrasyon senaryolarının test kapsamına alınması.

### 4.2 Kapsam Dışı

- CTI/PBX fiziksel altyapı değişiklikleri.
- Kurumsal IAM/SSO mimarisinin yeniden tasarımı.
- CRM dışındaki ürün veya modüllere yönelik geliştirmeler.

## 5. Hedef Çıktılar ve Başarı Kriterleri

- Yetki konfigürasyonu operasyon ekipleri tarafından daha kolay yönetilebilir olmalıdır.
- Aktif çağrı sırasında güvenlik uyumsuzluğu kaynaklı yetkisiz ekran açılışı engellenmelidir.
- Yeni ekran ve aksiyon ekleme süreci minimum kod bağımlılığı ile parametrik ilerlemelidir.
- Kritik konfigürasyon değişiklikleri audit kayıtlarıyla takip edilebilir olmalıdır.
- Yetki ve güvenlik kuralları sunucu tarafında da zorunlu olarak uygulanmalıdır.
- Uygulama ekranları operasyonel kullanımda hızlı, anlaşılır ve hataya karşı yönlendirici olmalıdır.

## 6. Fonksiyonel Gereksinimler

### FR-01 Rol Bazlı Ekran Yetkisi

- Ekranlar tek sayfa yerine ihtiyaca göre çok adımlı akışları desteklemelidir (Örnek: Giriş, Onay, Tamamlandı).
- Her ekranda kullanıcıyı yönlendiren bilgi, uyarı ve doğrulama mesajları bulunmalıdır.
- Her rol için ekran bazlı erişim açık/kapalı olarak tutulabilmelidir.
- Ekran yetkisi ve buton yetkisi arasında tutarlılık kuralı uygulanmalıdır.
- Yetki değişiklikleri kullanıcı, zaman, önceki değer, yeni değer ve işlem sonucu bilgileriyle auditlenmelidir.

### FR-02 Rol Bazlı Buton Yetki UX

- Buton yetki matrisi tüm rollerin aynı tabloda gösterildiği karmaşık modelde olmamalıdır.
- Kullanıcı önce rol seçmelidir.
- Seçilen role ait ekranlar accordion yapısında listelenmelidir.
- Ekran başlıkları alt ok veya benzeri görsel işaret ile açılıp kapanabilmelidir.
- Her aksiyonun sağında yalnızca açık/kapalı durumu gösteren toggle bulunmalıdır.
- Yetki değişikliği kaydedilmeden önce değişiklik özeti kullanıcıya gösterilmelidir.

### FR-03 Güvenlik Seviyesi Çoklu Seçim

- Her ekran için birden fazla güvenlik seviyesi seçilebilmelidir.
- Seçili seviyeler ön izleme alanında görünmelidir.
- Kaydetme sonrası seçimler kalıcı olmalıdır.
- Desteklenen güvenlik seviyesi seti parametrik olarak yönetilebilmelidir.
- Güvenlik seviyesi değişiklikleri audit log kapsamında izlenmelidir.

### FR-04 Aktif Çağrı Ekran Açılış Kontrolü

- Aktif çağrı sırasında ekran açılışı, çağrı güvenlik seviyesi ile ekranın izinli güvenlik seviyeleri karşılaştırılmadan yapılmamalıdır.
- Çağrı güvenlik seviyesi ekranın izinli seviyeleri arasında değilse ekran açılmamalıdır.
- Uyumsuzluk durumunda standart uyarı mesajı gösterilmelidir.
- İş kuralına göre varsayılan güvenli ekrana yönlendirme veya güvenlik seviyesi artırım akışına yönlendirme parametrik olarak desteklenmelidir.
- Erişim reddi olayları audit log ve izleme altyapısına aktarılabilir olmalıdır.

### FR-05 Parametrik Davranışlar

Aşağıdaki davranışlar kod değişikliği olmadan parametrik olarak yönetilebilmelidir:

- Süreç ilerletme script altyapısı.
- Çağrı zorunlu ekran listesi.
- Muaf ekran listesi.
- Varsayılan güvenli ekran.
- Mesaj anahtarları ve metinleri.
- Desteklenen güvenlik seviyesi seti.
- Cache/yayılım politikası.
- Audit kapsamındaki olay tipleri.

## 7. İş Kuralları

- **BR-01:** Ekran yetkisi olmayan role ilgili ekran için aksiyon yetkisi verilemez.
- **BR-02:** Buton yetkisi ekran yetkisinden daha geniş olamaz.
- **BR-03:** Aktif çağrı varken güvenlik seviyesine uygun olmayan ekran açılamaz.
- **BR-04:** Kural ihlali ve erişim reddi durumları auditlenmek zorundadır.
- **BR-05:** Parametre değişikliği sonrası sistem davranışı tanımlı yayılım politikasına göre devreye alınmalıdır (anlık veya cache politikası).
- **BR-06:** Toplu konfigürasyon değişiklikleri transaction mantığı ile tutarlı şekilde tamamlanmalı veya geri alınmalıdır.
- **BR-07:** Eş zamanlı güncellemelerde veri kaybını engellemek için versioning veya optimistic locking yaklaşımı kullanılmalıdır.

## 8. Teknik Beklentiler

### 8.1 Frontend

- Responsive ve operasyon odaklı ekran davranışı.
- Rol seçimli accordion bileşeni.
- Çoklu seçim güvenlik seviyesi komponenti.
- Kullanıcı dostu validasyon ve uyarı mesajları.
- Yetkiye göre buton disable ve tooltip davranışı.
- Değişiklik özeti, kaydetme onayı ve hata durumlarında anlaşılır geri bildirim.

### 8.2 Backend

- Rol, ekran, aksiyon, güvenlik seviyesi ve parametre kaynaklarını merkezi olarak sunma.
- Yaklaşık 20 endpoint ile mevcut servisler veya yeni servis katmanı entegrasyonu.
- Bulk update ve transaction güvencesi.
- Audit log ve raporlanabilir veri modeli.
- Versioning veya optimistic locking yaklaşımı.
- Yetki ve güvenlik kurallarının server tarafında zorunlu olarak uygulanması.
- AD grubu/rol eşleştirme davranışının net tanımlanması.

### 8.3 Veri Modeli Konsepti

Beklenen ana varlıklar ve ilişki yapıları:

- Role
- Screen
- Action
- SecurityLevel
- RoleScreenPermission
- RoleActionPermission
- ScreenSecurityLevel
- ConfigurationParameter
- AuditLog

Tedarikçi teklifinde tablo/alan seviyesinde detaylı veri modeli, migration yaklaşımı ve geri dönüş stratejisi sunulmalıdır.

## 9. Non-Functional Gereksinimler

- **Güvenlik:** Yetki ihlali ve bypass denemeleri server tarafında engellenmelidir.
- **Performans:** Konfigürasyon ekranları operasyonel kullanımda akıcı çalışmalıdır.
- **İzlenebilirlik:** Kritik değişiklikler, erişim reddi olayları ve kural ihlalleri loglanmalıdır.
- **Bakım Kolaylığı:** Yeni ekran ve aksiyon tanımları minimum kod değişikliği ile eklenebilmelidir.
- **Gözlemlenebilirlik:** Kritik olaylar izleme ve uyarı sistemlerine aktarılabilmelidir.
- **Kullanılabilirlik:** Ekranlar operasyon ekiplerinin yoğun kullanım senaryolarına uygun, sade ve hataya karşı yönlendirici olmalıdır.

## 10. Teslimat Kapsamı

Tedarikçiden aşağıdaki teslimatlar beklenmektedir:

- Kaynak kod değişiklikleri (frontend ve backend).
- Veritabanı değişiklikleri ve migration scriptleri.
- Parametre varsayılan değer setleri.
- Teknik dokümantasyon:
  - Kurulum,
  - Konfigürasyon,
  - İşletim,
  - Geri dönüş/rollback yaklaşımı.
- Test dokümanı ve test kanıtları.
- UAT destek paketi.
- Canlıya geçiş destek planı.
- Bilgi aktarımı ve operasyon ekibi eğitimi.

## 11. Test ve Kabul Yaklaşımı

### 11.1 Zorunlu Test Paketleri

- Unit testler.
- Integration testler.
- Regresyon testleri.
- Negatif güvenlik senaryoları.
- UAT senaryoları.
- Fimple ve SIP entegrasyon testleri.

### 11.2 Örnek Kabul Kriterleri

- Rol seçildiğinde yalnızca seçilen role ait aksiyon izinleri görünmelidir.
- Accordion altındaki aksiyon toggle değişiklikleri kaydedildikten sonra kalıcı olmalıdır.
- Ekran güvenlik seviyesi birden fazla değer ile kaydedilebilmelidir.
- Aktif çağrı seviyesi ekranın izinli seviye listesinde değilse ekran açılışı reddedilmelidir.
- Audit log kaydı oluşmadan konfigürasyon update işlemi tamamlanmamalıdır.
- Ekran yetkisi olmayan role aksiyon yetkisi verilmek istendiğinde sistem işlemi engellemelidir.
- Toplu güncelleme kısmen başarısız olursa veri tutarlılığı korunmalıdır.

## 12. Tedarikçi Yanıt Formatından Beklenenler

Teklif veren tedarikçilerin aşağıdaki başlıkları içeren bir yanıt dokümanı sunması beklenir:

- Teknik çözüm yaklaşımı.
- Önerilen UX/UI yaklaşımı ve örnek ekran tasarımları.
- Mimari yaklaşım ve entegrasyon modeli.
- Varsayımlar, bağımlılıklar ve riskler.
- Proje ekibi ve roller.
- Test stratejisi ve kalite güvence yaklaşımı.
- Canlıya geçiş ve geri dönüş planı.
- Bakım, destek, SLA/SLO yaklaşımı.
- Fiyatlandırma kırılımı.
- Referans projeler.

## 13. Tedarikçi Yetkinlik Beklentileri

- Benzer yetkilendirme ve konfigürasyon yönetimi projelerinde referans deneyim.
- Frontend ve backend entegre çalışma kabiliyeti.
- Test otomasyonu ve kalite güvencesi olgunluğu.
- Dokümantasyon disiplini ve analist odaklı iletişim.
- Canlı destek ve issue yönetim süreci.
- Güvenlik, audit ve operasyonel izlenebilirlik konularında deneyim.

## 14. Fiyatlandırma

Fiyatlandırma aşağıdaki kırılımları içermelidir:

- UX/UI tasarım.
- Frontend geliştirme.
- Backend geliştirme ve entegrasyon.
- Veritabanı/migration çalışmaları.
- Test ve kalite güvence.
- UAT ve canlıya geçiş desteği.
- Bakım ve destek.
- Değişiklik yönetimi.

Tedarikçi, kapsam dışı taleplerin nasıl fiyatlandırılacağını ve değişiklik yönetimi sürecinin nasıl işleyeceğini açıkça belirtmelidir. SLA/SLO beklentileri destek modeli ile birlikte sunulmalıdır.

## 15. Değerlendirme Kriterleri

Teklifler aşağıdaki kriterlere göre değerlendirilecektir:

- Teknik uygunluk.
- UX/UI çözüm kalitesi.
- Referans projeler ve alan deneyimi.
- Test, dokümantasyon ve kalite yaklaşımı.
- Fiyat.
- Teslim ve destek yaklaşımı.
- Risk ve bağımlılıkların açıklığı.

## 16. Ekler

### 16.1 Ekran Envanteri - Örnek

- Ana başlık sayısı: 8
- Alt başlık sayısı: 20

Tedarikçi, teklifinde ekran envanterinin nasıl modelleneceğini, yeni ekran/aksiyon ekleme sürecinin nasıl işleyeceğini ve operasyon ekiplerinin konfigürasyonları hangi ekranlar üzerinden yöneteceğini açıklamalıdır.

## 17. Revizyon Notları

Bu versiyonda kaynak RFP metni:

- Dil, imla ve terminoloji açısından düzenlendi.
- Eksik numaralandırma düzeltildi.
- Teklif toplamaya uygun olacak şekilde tedarikçi yanıt formatı eklendi.
- Teknik kapsam, test beklentileri ve kabul kriterleri netleştirildi.
- Audit, transaction, optimistic locking, cache/yayılım politikası ve server-side güvenlik kontrolleri daha belirgin hale getirildi.
