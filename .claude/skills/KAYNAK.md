# Skiller — nereden geldi

Bu klasördeki skillerin çoğu **başkalarının yazdığı, hazır skillerdir.** Sıfırdan
yazılan üç tanesi Balıkçıl'ın kendi kurallarını kodlar; onların karşılığı hazır
ekosistemde yok.

Her dosyanın SHA-256 parmak izi `PARMAK-IZLERI.txt` içindedir (KURALLAR 2).
Kaynaklar **commit'e sabitlenmiş** hâlde indirildi; böylece aynı girdi aynı
sonucu verir (KURALLAR 29). Depo güncellenirse bizim kopyamız değişmez —
bilerek böyle.

---

## Dışarıdan alınanlar

### agiprolabs/claude-trading-skills · MIT · commit `981e1d7`
`https://github.com/agiprolabs/claude-trading-skills`
Lisans metni: `LICENSE-agiprolabs.md` · Telif: AGIPro

Deponun **68 skillinden 6'sı** alındı. Tamamı kurulmadı: eklenti olarak her
oturuma ~4.016 token ekliyordu ve içindeki 60 skill (Solana MEV, kripto vergi,
hava durumu piyasası, DEX likidite) bu laboratuvarın alanı değil. Daha kötüsü,
`slippage-modeling` skilli Solana AMM matematiği anlatıyor; Binance süresiz
vadeli sözleşmede masraf sorulduğunda yanlış alandan cevap verme riski vardı
(KURALLAR 14).

| skill | neye yarıyor | hangi adım |
|---|---|---|
| `walk-forward-validation` | zaman serisine uygun bölme, purging, embargo, aşırı-uyum tespiti | 6 · 8 |
| `ohlcv-processing` | yeniden örnekleme, boşluk doldurma, aykırı değer, kaynak birleştirme | 2 |
| `correlation-analysis` | çapraz varlık korelasyonu, rejime göre korelasyon | KURALLAR 13 |
| `vectorbt` | vektörleştirilmiş geriye dönük test, parametre taraması | 8 |
| `market-microstructure-traditional` | emir defteri dinamiği, fiyat oluşumu, uygulama kalitesi, CEX–DEX farkı | 3 · 8 |
| `portfolio-analytics` | getiri ve risk ölçümü, zirveden düşüş, yuvarlanan analiz | 8 |

**Dikkat — `walk-forward-validation` iki sabit eşik taşıyor:**
"DSR below 0.95" ve "PBO above 0.50". Bunlar Balıkçıl'ın kuralı **değildir.**
Balıkçıl'ın şans çizgisi KURALLAR 12'de yazılıdır: cevaplar 1.000 kez
karıştırılır, gerçek sonuç en iyi %1'in içinde olmalıdır. **Çelişme hâlinde
KURALLAR kazanır.** DSR/PBO'yu geçme şartına eklemek istenirse bu bir kural
değişikliğidir: önce kullanıcıya sorulur, sonra `DEFTER.md`ye yazılır.

### shakeebshaan/claude-code-quant-skills · MIT · commit `6b39f8f`
`https://github.com/shakeebshaan/claude-code-quant-skills`
Lisans metni: `LICENSE-shakeebshaan.txt` · Telif: Shaan Shaik

| skill | neye yarıyor | kime |
|---|---|---|
| `strategy-critique` | 18 soruluk düşmanca inceleme: avantaj gerçek mi, karşı tarafta kim kaybediyor, neden arbitraj bunu yemedi, hangi rejimde kırılır | Viktor |
| `backtest-review` | geriye dönük testi denetler: geleceği görme, aşırı uyum, gerçekçi olmayan varsayım, rejim bağımlılığı | Viktor · Mateo |
| `data-scrub` | veri denetimi: eksik mum, saat dilimi kayması, bayat tik, yinelenen zaman damgası, hayatta kalma yanlılığı | Mateo |

`strategy-critique` Viktor'un beş sorusunu genişletir, **yerine geçmez.**
Viktor'un kırmızı damgası ve gerekçe zorunluluğu (KURALLAR 32) onun tanımında
kalır.

---

## Eklenti olarak kurulanlar (kopyalanmadı, `--scope project`)

| eklenti | kaynak | içerik | yük |
|---|---|---|---|
| `duckdb-skills` 0.2.4 | resmî marketplace · DuckDB Foundation · SHA sabitli | `read-file` `query` `attach-db` `convert-file` `s3-explore` `spatial` `duckdb-docs` `install-duckdb` `read-memories` | ~995 tok |
| `quantitative-trading` 1.2.3 | `wshobson/agents` · MIT · Seth Hobson | skiller: `backtesting-frameworks` `risk-metrics-calculation` · ajanlar: `quant-analyst` `risk-manager` | ~365 tok |

**`read-memories` Balıkçıl'da çalıştırılmaz.** Geçmiş oturum kayıtlarını arar;
bu makinede eski projenin oturum kayıtları var (KURALLAR 1). Yasak
`duvar-denetimi` skillinin 5. maddesinde kayıtlı.

**`quant-analyst` ve `risk-manager` ajanları Balıkçıl'ın ekibi değildir.**
Ekip `EKIP.md`de yazılıdır ve on isimdir. Bu iki ajan eklentiyle birlikte geldi;
kullanılmaz. Koordinatör bunları çalıştırırsa EKIP'in dışına çıkmış olur.

---

## Balıkçıl'a özel yazılanlar

Bunların hazır karşılığı ekosistemde aranıp bulunamadı: hepsi bu laboratuvarın
kendi kurallarını kodluyor.

| skill | hangi kural |
|---|---|
| `defter` | `DEFTER.md`ye sadece ekler, saati sistemden okur (KURALLAR 23, 30) |
| `talimat` | talimatı yazar, sızıntı denetiminden geçirir, tam kopyasını `talimatlar/` altına kaydeder (KURALLAR 3, 4, 24) |
| `duvar-denetimi` | duvarı denetler: sızıntı, yönlendirme, sınav erişimi, bayat ayar yolları (KURALLAR 1–5) |

---

## Kullanım sınırı — önemli

Bu skillerin hepsi **mekanik** iş içindir: betik yazmak, veri hazırlamak,
ölçmek, denetlemek. İkisi (`strategy-critique`, `backtest-review`) eleştiri
içindir.

**Hiçbiri izleyici talimatı yazarken kullanılmaz.** İzleyiciye ne arayacağı
söylenmez, yalnız neye bakabileceği söylenir (KURALLAR 3). Koordinatör bir
skilli okuyup ondan çıkardığı fikri izleyici talimatına koyarsa, laboratuvarın
duvarını kendi eliyle delmiş olur. Skiller Mateo'nun betiklerine, Greta'nın
ölçümüne ve Viktor'un eleştirisine hizmet eder.

Ajan tanımlarının hiçbirinde `Skill` aracı yoktur: hiçbir ajan bir skill
çağırıp bu sınırı dolaşamaz.
