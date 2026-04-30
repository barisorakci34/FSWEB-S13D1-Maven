# Çağrı Merkezi Projesi RFP Özeti

**Doküman Tarihi:** 2026-04-28  
**Versiyon:** V1.2 - Kısa Özet  
**Amaç:** Ekran tasarımları ve yazılım geliştirme süreçleri için tedarikçilerden teknik/ticari teklif almak.

## 1. Kısa Tanım

Mevcut Çağrı Merkezi uygulamasında rol bazlı ekran ve buton yetkileri operasyonel olarak zor yönetilmektedir. Ayrıca ekran güvenlik seviyesi tek seçimle sınırlı olduğu için aktif çağrı sırasında erişim kontrolü yeterince esnek değildir.

Bu çalışma ile yetki, güvenlik seviyesi ve aktif çağrı erişim kurallarının parametrik, auditlenebilir ve operasyon ekipleri tarafından yönetilebilir hale getirilmesi hedeflenmektedir.

## 2. Ana İş İhtiyacı

- Rol bazlı ekran ve buton yetkileri sade bir yönetim ekranı üzerinden yönetilmelidir.
- Buton yetki matrisi rol seçimi ve accordion yapısı ile daha anlaşılır hale getirilmelidir.
- Her ekran için birden fazla güvenlik seviyesi seçilebilmelidir.
- Aktif çağrı sırasında ekran açılışı, çağrının güvenlik seviyesi ile ekranın izinli seviyeleri karşılaştırılarak kontrol edilmelidir.
- Yetki ve parametre değişiklikleri audit log ile izlenebilmelidir.
- Yeni ekran, aksiyon ve güvenlik seviyeleri minimum kod değişikliğiyle tanımlanabilmelidir.

## 3. Kapsam

### Kapsam İçi

- UX/UI ekran tasarımları.
- Frontend geliştirme.
- Backend servis entegrasyonları (yaklaşık 20 endpoint).
- Active Directory entegrasyonu.
- Rol bazlı ekran ve buton yetki yönetimi.
- Çoklu güvenlik seviyesi seçimi.
- Aktif çağrı bazlı ekran erişim kontrolü.
- Parametrik konfigürasyon altyapısı.
- Audit log, raporlama temeli ve izlenebilirlik.
- Unit, entegrasyon, regresyon ve UAT destekleri.

### Kapsam Dışı

- CTI/PBX fiziksel altyapı değişiklikleri.
- Kurumsal IAM/SSO mimarisinin yeniden tasarımı.
- CRM dışı ürün veya modül geliştirmeleri.

## 4. Temel Fonksiyonel Beklentiler

- Kullanıcı önce rol seçmeli, seçilen role ait ekran ve aksiyon yetkilerini görmelidir.
- Ekran başlıkları accordion olarak açılıp kapanmalıdır.
- Aksiyonlar açık/kapalı toggle ile yönetilmelidir.
- Ekran yetkisi olmayan role buton/aksiyon yetkisi verilememelidir.
- Her ekran için birden fazla güvenlik seviyesi seçilip kaydedilebilmelidir.
- Aktif çağrı seviyesi ekranın izinli seviyeleri arasında değilse ekran açılmamalı ve standart uyarı gösterilmelidir.
- Çağrı zorunlu ekran listesi, muaf ekran listesi, varsayılan güvenli ekran, mesajlar ve güvenlik seviye seti parametrik olmalıdır.

## 5. Teknik Beklentiler

- Responsive ve operasyon odaklı frontend ekranları.
- Rol seçimli accordion bileşeni.
- Çoklu güvenlik seviyesi seçim komponenti.
- Merkezi rol, ekran, aksiyon, güvenlik seviyesi ve parametre servisleri.
- Bulk update, transaction güvenliği ve optimistic locking/versioning.
- Server-side yetki kontrolü.
- Audit log ve raporlanabilir veri modeli.
- AD rol/grup eşleştirme yaklaşımı.

## 6. Önerilen Veri Modeli Başlıkları

- Role
- Screen
- Action
- SecurityLevel
- RoleScreenPermission
- RoleActionPermission
- ScreenSecurityLevel
- ConfigurationParameter
- AuditLog

## 7. Teslimatlar

Tedarikçiden aşağıdaki çıktılar beklenmektedir:

- Kaynak kod değişiklikleri.
- Veritabanı migration scriptleri.
- Parametre varsayılan değerleri.
- Teknik dokümantasyon.
- Test dokümanı ve test kanıtları.
- UAT destek paketi.
- Canlıya geçiş ve rollback planı.
- Bakım/destek modeli ve SLA/SLO yaklaşımı.

## 8. Test ve Kabul Kriterleri

- Rol seçildiğinde sadece ilgili role ait yetkiler görünmelidir.
- Accordion altındaki toggle değişiklikleri kalıcı olmalıdır.
- Bir ekran birden fazla güvenlik seviyesiyle kaydedilebilmelidir.
- Aktif çağrı seviyesi uygun değilse ekran açılışı reddedilmelidir.
- Yetki ihlalleri ve kritik konfigürasyon değişiklikleri auditlenmelidir.
- Toplu güncellemelerde veri tutarlılığı korunmalıdır.

## 9. Tedarikçi Teklifinde Beklenen Başlıklar

- Teknik çözüm yaklaşımı.
- UX/UI tasarım yaklaşımı ve örnek ekranlar.
- Mimari ve entegrasyon modeli.
- Varsayımlar, bağımlılıklar ve riskler.
- Test stratejisi.
- Canlıya geçiş ve rollback planı.
- Proje ekibi ve rol dağılımı.
- Referans projeler.
- Fiyatlandırma kırılımı:
  - UX/UI tasarım,
  - Frontend,
  - Backend,
  - Entegrasyon,
  - Test,
  - UAT/canlı geçiş,
  - Bakım ve destek.

## 10. Değerlendirme Kriterleri

Teklifler aşağıdaki kriterlere göre değerlendirilecektir:

- Teknik uygunluk.
- UX/UI çözüm kalitesi.
- Benzer proje deneyimi.
- Test ve dokümantasyon yaklaşımı.
- Fiyatlandırma netliği.
- Destek ve SLA/SLO modeli.

## 11. Ekran Envanteri Bilgisi

- Ana başlık sayısı: 8
- Alt başlık sayısı: 20

Tedarikçi, teklifinde bu ekran envanterini nasıl modelleyeceğini ve yeni ekran/aksiyon ekleme sürecini nasıl yöneteceğini açıklamalıdır.
