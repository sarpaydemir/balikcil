# Taktikler — adım adım

## 0 · Dönem ve evren

- **Dönem:** 2025-09-01 → 2026-08-31. Bir şey bulunursa sonra
  2024-09-01 → 2025-08-31 döneminde ikinci kez sınanır.
- **Evren:** bu dönemde işlem görmüş bütün Binance USDT süresiz vadeli
  sözleşmeleri. Liste bugünkü borsadan değil arşivden (`data.binance.vision`)
  kurulur, böylece dönem içinde ölen coinler de dahil olur.

## 1 · Çekiliş

- Coinler dört gruba ayrılır:
  - **büyük / orta / küçük:** dönemdeki günlük işlem hacminin ortancasına göre
    üçe bölünür
  - **yeni:** ilk işlemi dönem içinde olan
- **Kura numarası:** `20260913`. Çekilişten önce yazıldı, değiştirilmez.
- **İzleme:** 10 coin (3 büyük · 3 orta · 2 küçük · 2 yeni)
- **Sınav:** başka 20 coin (6 · 6 · 4 · 4)
- **Para testi:** geri kalan bütün coinler
- Hangi coinin hangi gruba düştüğü `DEFTER.md`ye yazılır. İzleyiciler sınav ve
  para testi coinlerinin adını görmez.

## 2 · Anlar

- Saatlik kapanış fiyatları kullanılır.
- **Büyük hareket anı:** coinin 24 saat içinde en çok yükseldiği ya da düştüğü
  yerler.
  - Her coin için yılın en büyük 20'si alınır.
  - Birbirine 48 saatten yakın iki andan sadece büyüğü sayılır.
  - Yıl boyu işlem görmemiş coinde bu sayı ömrüyle orantılı azalır: her 18 günde
    bir an.
- **Sakin an:** büyük anlarla aynı sayıda, rastgele seçilir. Herhangi bir büyük
  hareketten en az 72 saat uzakta olur.
- Bir anın başlangıcı, 24 saatlik hareketin başladığı saattir.

## 3 · Kart

Her an için tek sayfa. İki bölümü var:

- **Öncesi:** başlangıçtan önceki 24 saat, saat saat; artı önceki 7 günün tek
  satırlık özeti.
- **Sonrası:** başlangıçtan sonraki 24 saat. Sadece serbest izlemede gösterilir,
  sınavda asla.

**Kartta olanlar** (verisi varsa):
- fiyat, hacim, işlem sayısı, alıcı-satıcı baskısı
- açık pozisyon, uzun/kısa oranları (5 dakikalık arşiv)
- fonlama oranı, ödeme aralığı ve değişimi
- emir defteri derinliği (sadece an günleri indirilir; dosyalar büyük)
- Binance ve Kore borsası duyuruları (listeleme, listeden çıkarma, uyarı)
- bitcoin ve ethereum, aynı saatlerde
- Amerika açıklama takvimi (enflasyon, istihdam, faiz kararı)
- Vikipedi'de sayfaya bakan kişi sayısı (günlük)
- varsa ilgili tahmin pazarının fiyatı

**Kartta olmayanlar**, çünkü geçmişi yok ya da erişilemiyor: Google aramaları,
Reddit, Twitter, kaldıraç sınırının geçmişi, dünya haber arşivi. Haber arşivine
bu makineden bağlanılamadı; bir yol bulunursa eklenir.

Sayılar yuvarlanır, kart kısa tutulur. Yapay zekâ ham saniyeleri hiç görmez.

## 4 · Serbest izleme

- **Pilot:** aynı 10 kartı hem küçük hem orta model okur. Not kalitesi ve token
  farkı `DEFTER.md`ye yazılır, model buna göre seçilir.
- Dört izleyici (Ingrid, Kenji, Amara, Lukas) 10 coinin bütün kartlarını okur.
  Her biri kendi baktığı yerden not alır.
- Kartlar karışık sırayla verilir: büyük anlar ve sakin anlar iç içe.
- Not biçimi: `kart no · ne gördüm · bence neden · ne kadar eminim (1–5)`.
  Kart numarası olmayan not sayılmaz.

## 5 · Kantin

- **Tur 1:** herkes notlarını `kantin/` klasörüne yazar.
- **Tur 2:** herkes diğer üçünün notlarını okur ve kart numarası vererek katılır
  ya da karşı çıkar.
- **Viktor** her fikre saldırır.
- **Sofia** ayakta kalanları yazar:
  - (a) **mekanik kurallar:** tetik · yön · çıkış; betikle ölçülebilir
  - (b) **puan tarifi:** hangi işaret kaç puan, hangi puanda al, hangi puanda sat.
    Defter biçiminde yazılır (KURALLAR 31).
- En fazla iki tur yapılır. Sonra kantin kitabı donar ve parmak izi
  `DEFTER.md`ye yazılır.

## 6 · Kör sınav

- Nadia sınav coinlerinden 400 kart hazırlatır: 200 büyük hareket öncesi,
  200 sakin an. Kartlarda sadece "öncesi" bölümü bulunur.
- **Gizlenenler:**
  - coin adı
  - tarih ve saat
  - fiyatın kendisi (100'den başlayan bir sayıya çevrilir)
  - duyurudaki coin adı
  - Vikipedi sayısının kendisi (coinin kendi ortalamasına oranı verilir)
  - açıklama takvimindeki tarih
- Cevap anahtarı ayrı dosyaya yazılır. Parmak izi sınavdan önce `DEFTER.md`ye
  geçer.
- **Sınava girenler** (hepsi aynı 400 kartı alır):
  1. Hana, Sofia'nın puan tarifiyle
  2. Tomás, tarifsiz, sadece sağduyuyla
  3. Greta, Sofia'nın mekanik kurallarını betikle uygular
  4. basit kural: son 24 saatin yönü devam eder
  5. yazı-tura
- **Cevap biçimi:** `kart no · yükselir / düşer / sakin kalır · güven 0–100`.
  Hana ve Greta her kart için puan defterini de doldurur: puan, artıran
  işaretler, engeller, bilinmeyenler.

## 7 · Puanlama (Greta)

- İki soru sorulur:
  1. Büyük hareketleri sakin anlardan ayırabildi mi?
  2. Büyük hareketlerde yönü bildi mi?
- **Şans çizgisi:** cevaplar 1.000 kez karıştırılır; en iyi %1'in sınırı çizgidir.
- Aynı saatte birden çok kartta görünen an tek olay sayılır.
- Her sınav ve para koşusu numarasıyla kaydedilir, kayıt değiştirilemez
  (KURALLAR 29–30).
- **Geçme şartı** (sonuçtan önce yazıldı): tarifli kâğıt (Hana ya da Greta)
  - şans çizgisini geçer, **ve**
  - Tomás'ı geçer, **ve**
  - basit kuralı geçer.

  Rakipleri geçip geçmediği de karıştırma yöntemiyle, %1 sınırında sınanır.

## 8 · Para testi

- Sadece sınavı geçen kurallar girer.
- Para testi coinlerinde (izlenmemiş, sınava da girmemiş), bütün dönem boyunca,
  betikle koşulur. Yalnız kuralın kullandığı veri indirilir.
- **Giriş:** işaretten sonraki saatin ilk fiyatı.
- **Masraf** (varsayım): her taraf %0,05 ücret + %0,05 kayma, gidiş-dönüş %0,20.
  Fonlama gerçek ödemelerle hesaplanır.
- **Rakip:** aynı sayıda ve aynı süreli, rastgele zamanlı işlemler (1.000 kez).
- **Ölçülenler:**
  - bileşik getiri ve günlük karşılığı
  - iki zaman yarısı ayrı ayrı
  - zirveden en kötü düşüş
  - hesabı sıfırlayan işlem sayısı
  - 1x, 3x ve 5x kaldıraç
- **Geçme şartı:**
  - bileşik getiri iki yarıda da artıda, **ve**
  - rastgele rakibin %99'unu geçiyor, **ve**
  - 5 kata kadar en az bir kaldıraçta hesap sıfırlanmıyor.
- **Pusula:** günde %1. Bu bir geçme notu değil, nerede durduğumuzu gösterir.

## 9 · Rapor

- Önce sade: ne sorduk, ne çıktı, ne anlama geliyor, sırada ne var.
- Sonra teknik: sayılar, dosya yolları, parmak izleri.
- Açık kalan her şey adıyla sayılır.

## 10 · Ekran (sonra)

Kartlar, notlar, oylar ve itirazlar tek sayfada izlenecek. Laboratuvar ilk
sonuçlarını verdikten sonra yapılacak.
