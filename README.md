# Balıkçıl — izleme laboratuvarı

**Kod adı:** Balıkçıl · **Klasör:** `projects/balikcil` (proje deposunun içinde)

Balıkçıl suyun içinde saatlerce kıpırdamadan durur. Hiçbir şey yapmaz, sadece
izler. Suyu anladığında bir kez vurur.

Bu laboratuvar da öyle çalışır. Alım satım yapmaz, önce izler: coin sakinken ne
oluyor, sert hareketten önce ne oluyor, borsa bu sırada ne yapıyor, dünyada ne
oluyor.

**Amaç bir puanlama sistemi.** Puan bir çizginin üstündeyse al, başka bir
çizgideyse sat (short), aradaysa bir şey yapma. Puanın nereden geleceğini
izleyerek buluruz, tahminle değil.

## Neden duvar var

Eski laboratuvarda aylarca çalıştık, kafamızda bir sürü kanaat birikti. Bu
kanaatler yeni izleyicilerin gözünü boyamasın diye Balıkçıl aynı deponun içinde
ama bir duvarın arkasında durur:

- üst klasördeki eski kural dosyası yüklenmez
- eski deney klasörleri ve durum dosyaları okunamaz
- Balıkçıl'ın kendi hafıza defteri vardır
- veri sıfırdan indirilir

Duvar `.claude/settings.json` içindedir ve **yalnız Balıkçıl bu klasörden
açılınca çalışır.** Ayrıntısı `KURALLAR.md`de.

## Akış — yedi adım

1. **Çekiliş.** Coinler kurayla seçilir: 10 coin izlemeye, 20 coin sınava, geri
   kalanı para testine.
2. **Hazırlık.** Veri indirilir. Her coinin büyük hareket anları ve sakin anları
   bulunur. Her an için tek sayfalık bir kart yazılır. Bunu betik yapar, yapay
   zekâ değil.
3. **Serbest izleme.** Dört izleyici 10 coinin kartlarını okur. Hareketin öncesini
   de sonrasını da görürler ve not alırlar.
4. **Kantin.** İzleyiciler birbirinin notunu okuyup tartışır. Şüpheci her fikre
   saldırır. Kantin başkanı ayakta kalan fikirleri kurala çevirir.
5. **Kör sınav.** Sınav coinlerinden kartlar gösterilir, ama sadece hareketin
   öncesi. Coin adı ve tarih gizlidir. Kurallar "ne olacak" diye tahmin eder.
   Hiç izlememiş biri ve basit bir kural da aynı sınava girer.
6. **Para testi.** Sınavı geçen kural, hiç görülmemiş yüzlerce coinde
   masraflarıyla denenir.
7. **Rapor.** Önce sade, sonra teknik.

**Serbest izleme fikir üretir, kanıt üretmez.** Kanıt yalnız 5. ve 6. adımdan
gelir.

## Dosyalar

- `EKIP.md` — kim kimdir, ne yapar, ne yapamaz
- `KURALLAR.md` — değişmez kurallar
- `TAKTIKLER.md` — adım adım nasıl yapılır
- `DEFTER.md` — ne zaman ne oldu; sadece eklenir, hiçbir satır silinmez
- `CLAUDE.md` — bu klasörde açılan yapay zekâ oturumunun ilk okuyacağı yer
- `.claude/settings.json` — duvar ayarları

İlk iş olarak kurulacak klasörler: `veri/` · `kartlar/` · `notlar/` · `kantin/` ·
`sinav/` · `talimatlar/` · `betikler/` · `raporlar/`

## Durum

`2026-09-13` kuruldu, `2026-09-14` proje deposunun içine taşındı ve duvar
ayarları eklendi. Hiçbir veri indirilmedi, hiçbir ajan çalışmadı.

**Sonra eklenecek:** izleme ekranı. Kartlar, notlar, oylar ve itirazlar tek
sayfada görünecek.
