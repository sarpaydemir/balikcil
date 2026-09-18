# Kurallar

Bu kurallar değişmez. Değişmesi gerekirse önce kullanıcıya sorulur, sonra
`DEFTER.md`ye yazılır.

## A · Duvar — eski projeden hiçbir şey sızmaz

1. Balıkçıl yalnız kendi klasörünü okur. Deponun geri kalanından (eski deneyler,
   durum dosyaları, eski hafıza) dosya, sonuç, not ya da sayı okunmaz,
   kopyalanmaz.
2. Veri sıfırdan, herkese açık kaynaklardan indirilir. Her dosyanın nereden ve
   ne zaman indiği yazılır, parmak izi (SHA-256) alınır. Binance arşivi kendi
   sağlama dosyasıyla doğrulanır.
3. Ajanlara ne arayacakları söylenmez, sadece neye bakabilecekleri söylenir.
   Talimatta hiçbir sonuç, tahmin ya da "şuna dikkat edin" yönlendirmesi olmaz.
4. Her ajana verilen talimatın tam metni `talimatlar/` klasörüne kopyalanır.
   Kullanıcı istediği an sızıntı var mı diye bakabilir.
5. Balıkçıl her zaman **kendi klasöründen açılan bir oturumla** yönetilir.
   Duvar ayarları (`.claude/settings.json`) yalnız öyle açılınca çalışır:
   - üst klasördeki eski kural dosyası yüklenmez
   - eski klasörleri okuma engellenir
   - Balıkçıl'ın hafıza defteri ayrıdır

   Eski projenin oturumundan başlatılan her ajan eski kural dosyasını taşır.
   Bu yüzden Balıkçıl işi oradan yaptırılmaz.

   Ayarların kapatamadığı bir delik var: komut satırından dosya okumak. Orada
   kural 1 geçerlidir ve her talimat bunu açıkça yasaklar.

## B · Kendimizi kandırmamak

6. Önce kural yazılır, sonra sonuç açılır. Sonuca bakıp kural değiştirilmez.
   Değiştirilirse yeni bir kural sayılır, "sonradan" etiketi taşır ve yeniden
   sınanır.
7. Serbest izleme fikir üretir, kanıt üretmez.
8. Her fikir üç parçayla yazılır: ne olunca (tetik), hangi yöne (al ya da sat),
   ne zaman çıkılır (çıkış). Biri eksikse fikir sayılmaz, çünkü sınanamaz.
9. Sınavda coin adı ve tarih gizlidir. Cevap anahtarı sınavdan önce mühürlenir:
   parmak izi `DEFTER.md`ye yazılır.
10. Sınava giren ajan araç kullanamaz, dosya okuyamaz. Araç kullandığı görülen
    kâğıt geçersizdir.
11. Her sonuç üç rakibe karşı ölçülür:
    - yazı-tura
    - basit bir kural: son 24 saat hangi yöne gittiyse o yöne devam
    - hiç izlememiş biri (Tomás)

    Üçünü de geçemeyen bulgu "öğrenildi" sayılmaz.
12. Şans çizgisi uydurulmaz. Cevaplar 1.000 kez karıştırılır, gerçek sonuç en iyi
    %1'in içinde olmalıdır.
13. Aynı saatte birden fazla coinde olan anlar tek olay sayılır. Bütün piyasa
    birlikte kıpırdadıysa bu tek bir olaydır.

## C · Para

14. Para testi masrafla yapılır: alış-satış ücreti, fiyat kayması, fonlama
    ödemesi.
15. Hesap toplayarak değil çarparak büyür. Getiri bileşik hesaplanır. Hesabı
    sıfırlayan tek bir işlem bile ayrıca sayılır.
16. Giriş, işaretten sonraki ilk gerçek fiyattan yapılır. Önceden bilinen bir
    anda (ödeme saati, duyuru anı) mumun açılış fiyatı alış fiyatı sayılmaz,
    çünkü o fiyattan kimse alamaz.
17. Kaldıraç en fazla 5 kat. Tasfiye, mumun en uç fiyatına göre hesaplanır.
18. Sonuç iki zaman yarısında ayrı ayrı gösterilir. Yarının biri kazanıp diğeri
    kaybediyorsa bu bir bulgu değildir.

## D · Dürüstlük

19. Ölçülmemiş sayı yazılmaz. Tahminse sayının hemen yanına "tahmin" yazılır.
20. "Yok" demeden önce nereye bakıldığı ve hangi hatanın alındığı yazılır.
    Bağlantı hatası "veri yok" demek değildir.
21. Teknik arıza bir sonuç değildir.
22. Raporda çözülmemiş şeyler tek tek adıyla sayılır. "Ölçülemedi" asla
    "sorun yok"a dönüşmez.
23. Saat tahmin edilmez, okunur.

## E · Maliyet ve işletme

24. Her görevde model açıkça seçilir. Önce küçük model; orta ya da büyük model
    gerekçesiyle.
25. İlk 10 kartta harcanan token ölçülür. Tam koşunun tahmini `DEFTER.md`ye
    yazılır ve başlamadan önce kullanıcıya tek cümleyle söylenir.
26. 10 dakikadan uzun iş ara kayıtla yazılır ve oturum kapansa da ölmeyecek
    şekilde başlatılır.
27. Sadece herkese açık, belgelenmiş veri kullanılır. Adres tahmin ederek arama
    yapılmaz.
28. İndirmeden önce boş disk alanı kontrol edilir.

## F · Kayıt ve puan defteri

29. Her koşunun bir numarası vardır: girdisinin parmak izi. Aynı girdi aynı
    numarayı ve aynı sonucu verir.
30. Kayıtlar sadece eklenir. Bir numaraya farklı içerik yazılmaya çalışılırsa
    betik durur.
31. Her puan defter biçiminde yazılır:
    - **toplam puan**
    - **artıran işaretler:** her birinin yanında kaç puan kattığı
    - **engeller:** biri bile varsa işlem yok, puan ne olursa olsun
    - **bilinmeyenler:** ölçülemeyen şeyler. Bu satır boş bırakılamaz; gerçekten
      yoksa neden olmadığı yazılır.
32. İtiraz gerekçesiyle yapılır. Gerekçesiz "hayır" sayılmaz; gerekçeli bir
    engeli de kimse aşamaz.
