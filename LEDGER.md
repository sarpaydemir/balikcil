# Ledger — append-only, no line is ever deleted

> Entries up to 2026-09-18 are in Turkish, because that was the laboratory's
> language at the time. From the "working language" entry onward, entries are in
> English. No record line was translated or touched — only this heading was.

`2026-09-13 11:00 UTC` · **kuruluş** · Kod adı Balıkçıl. README, EKIP, KURALLAR,
TAKTIKLER yazıldı. Kura numarası `20260913` yazıldı; çekiliş yapılmadı. Veri
indirilmedi, ajan çalışmadı.

`2026-09-13 11:00 UTC` · **koordinatör beyanı** · Bu dosyaları yazan koordinatör
eski projeden geliyor (`freqtrade_hyperopt`) ve oradaki bulguları biliyor.
Kurallara eski projeden hiçbir sonuç konmadı, yalnız yöntem dersleri
(kör sınav, bileşik hesap, masraf, tek olay sayımı, mum açılışı dolum değildir)
yazıldı. Kullanıcı incelemesi bekleniyor.

`2026-09-14 11:01 UTC` · **taşıma ve duvar** · Kullanıcı kararıyla
`/home/user/project-balikcil` → `freqtrade_hyperopt/projects/balikcil`.
Duvar `.claude/settings.json` ile kuruldu: üst `CLAUDE.md` dışlandı, eski
klasörleri okuma engellendi, hafıza defteri ayrıldı. Duvar yalnız bu klasörden
açılan oturumda çalışır; komut satırından okuma ayarla kapanmaz (KURALLAR 5).

`2026-09-14 11:01 UTC` · **dışarıdan alınanlar** · Kullanıcı kararıyla
`immortalhowwl/gptheist` reposundan iki şey alındı: puan defteri biçimi
(puan · artıran işaretler · engeller · bilinmeyenler) ve tekrarlanabilir,
değiştirilemez koşu kaydı (KURALLAR 29–32). Üçüncüsü olan izleme ekranı sonraya
bırakıldı (TAKTIKLER 10). O reponun eşikleri alınmadı.

`2026-09-18 19:39 UTC` · **ajanlar kuruldu** · `.claude/agents/` altına beş tanım yazıldı:
`veri-ustasi` (Mateo · efor high), `izleyici` (Ingrid · Kenji · Amara · Lukas,
bakış alanı talimattan gelir · medium), `kantin-baskani` (Sofia · high),
`supheci` (Viktor · xhigh), `sinav-adayi` (Hana ve Tomás, farkı yalnız talimat
yaratır · medium, `maxTurns: 1`). Hepsinde model `opus`, hepsinde
`omitClaudeMd: true` — ajanlar kendi tanımlarındaki duvar metnini okur, üst
CLAUDE.md dosyalarını hiç görmez. Tanımların hiçbirinde `Skill` aracı yok:
böylece bir ajan skill çağırıp duvarı dolaşamaz. `Bash` yalnız
`veri-ustasi`de var (KURALLAR 5 deliği oraya sıkıştırıldı).

`2026-09-18 19:39 UTC` · **kullanıcı kararı · model tavanı** · Kullanıcı kararıyla bütün
ajanlarda model `opus`. Bu, EKIP.md'deki "önce küçük model" ve KURALLAR 24'ün
"önce küçük" sırasının yerine geçer; ayrım artık model boyuyla değil **efor
seviyesiyle** yapılır. TAKTIKLER 4'teki pilot da buna göre değişir: aynı 10
kart küçük/orta model yerine **medium ve high efor** ile okunup karşılaştırılır.
Token maliyeti ölçülmedi (KURALLAR 25 hâlâ açık borç).

`2026-09-18 19:39 UTC` · **ajan sayısı ödünü** · Kullanıcı beş ajan istedi; EKIP.md'de yapay
zekâ olan sekiz isim var (Greta betiktir). Dört izleyici tek tanımda birleşti
(bakış alanı talimattan gelir, her koşu ayrı bağlamda çalışır), Hana ve Tomás
tek tanımda birleşti (EKIP zaten "model ikisinde aynı" diyordu — aynı tanım bunu
yapısal olarak garanti eder). **Nadia ayrı tanım olarak yazılmadı;** işi
`veri-ustasi`nin "Mod B · kör sınav kartı" moduna kondu. Mod B'de `notlar/` ve
`kantin/` kesinlikle kapalıdır ve her koşu ayrı bağlamda başladığı için o koşu
fikirleri hiç görmez. EKIP.md'nin harfine uymak istenirse Nadia altıncı tanım
olarak ayrılmalıdır — **açık madde.**

`2026-09-18 19:39 UTC` · **skiller** · Kullanıcı uyarısıyla önce var olanlar araştırıldı.
Resmî marketplace (`claude-plugins-official`) ve `anthropics/skills` deposunda
Balıkçıl'ın çekirdek ihtiyaçlarına (kör sınav düzeni, değiştirilemez koşu
kaydı, sızıntı denetimi) karşılık gelen hazır skill **yok.** Kurulan tek şey:
`duckdb-skills@claude-plugins-official` sürüm 0.2.4, DuckDB Foundation, kaynak
SHA'ya sabitli, **kapsam: project** (duvarın içinde kalır, eski projenin
oturumlarına bulaşmaz). Dokuz skill getirir; oturuma sürekli eklediği yük
~995 token (ölçüm aracın kendi bildirimi). **`read-memories` skilli Balıkçıl'da
çalıştırılmaz:** geçmiş oturum kayıtlarını arar, bu makinede eski projenin
oturum kayıtları vardır. Bu yasak `duvar-denetimi` skillinin 5. maddesinde
kayıtlıdır.

Projeye özel yazılan üç skill (`.claude/skills/`): `defter` (deftere sadece
ekleyen, saati sistemden okuyan kayıt), `talimat` (talimatı yazar, sızıntı
denetiminden geçirir, tam kopyasını `talimatlar/` altına kaydeder, sonra ajanı
çalıştırır — KURALLAR 3, 4, 24), `duvar-denetimi` (sızıntı ve duvar denetimi).
Ölçüm ve koşu kaydı için skill **yazılmadı**, çünkü yöntem zaten KURALLAR 11–12,
29–31 ve TAKTIKLER 7'de yazılı; ikinci kez yazmak çelişki üretirdi.

Hazır kullanılacak, yeniden yazılmayacak skiller: `dataviz` (raporlar ve
TAKTIKLER 10 ekranı), `xlsx` · `pdf` · `docx` (rapor dosyaları),
`code-review` · `simplify` · `security-review` (Mateo'nun betikleri),
`loop` · `schedule` (KURALLAR 26 uzun koşular), `update-config` (ayar ve hook),
`skill-creator` (yeni skill), `claude-api` (model ve maliyet bilgisi),
`artifact-*` (ileride izleme ekranı).

`2026-09-18 19:39 UTC` · **klasörler ve yetki** · `veri/ kartlar/ notlar/ kantin/ sinav/
talimatlar/ betikler/ raporlar/` kuruldu (boş, `.gitkeep` ile). Klasör kök
kullanıcısına aitti ve yazılamıyordu; yetkiyi kullanıcı düzeltti. Hiçbir veri
indirilmedi, hiçbir ajan çalıştırılmadı.

`2026-09-18 19:39 UTC` · **açık maddeler** · (1) `.claude/settings.json` içindeki
`autoMemoryDirectory` ve `claudeMdExcludes` yolları
`freqtrade_hyperopt/projects/balikcil`i gösteriyor, proje ise
`/home/user/balikcil`de — hafıza duvarın dışına yazıyor, düzeltilmedi.
(2) Komut satırı deliğini kapatacak `PreToolUse` hook'u kurulmadı; bu oturumda
ayar değiştirme yetkisi yoktu. (3) Klasör git deposu değil, kayıtların
değiştirilemezliği yalnız dosya disiplinine dayanıyor. (4) Nadia ayrı tanım
değil. (5) Token maliyeti ölçülmedi.

`2026-09-18 19:50 UTC` · **skiller · düzeltme ve dışarıdan alım** · Kullanıcı uyarısı:
"Amerika'yı yeniden keşfetmeye gerek yok, insanlar skilleri zaten yazmışlar."
Bir üstteki skill kaydı bu yüzden **eksiktir**: o kayıt yazıldığında yalnız
resmî marketplace ve `anthropics/skills` taranmıştı; topluluk ekosistemi
taranmamıştı. Tarandı ve karşılığı olan skiller bulundu.

**Eklenti olarak kurulan (kapsam: project):** `quantitative-trading` 1.2.3
(`wshobson/agents`, MIT, Seth Hobson) — `backtesting-frameworks` skilli
geleceği görme, hayatta kalma yanlılığı, işlem masrafı ve eğitim/doğrulama/test
ayrımını kapsıyor, **hiçbir sabit eşik ya da strateji kanaati taşımıyor.**
Oturum yükü ~365 token. Yanında iki ajan geldi (`quant-analyst`,
`risk-manager`); **bunlar EKIP'in dışındadır ve kullanılmaz.**

**Kurulup geri kaldırılan:** `trading-skills` 1.0.0
(`agiprolabs/claude-trading-skills`, MIT). 68 skill, oturum yükü ölçüldü:
**~4.016 token.** Kaldırma gerekçesi yalnız maliyet değil — içindeki
`slippage-modeling` skilli Solana AMM matematiği anlatıyor ve Binance süresiz
vadeli sözleşmede masraf sorulduğunda yanlış alandan cevap verme riski taşıyor
(KURALLAR 14). 60 skill bu laboratuvarın alanı değil.

**Yerine seçilerek alınan 6 skill** (commit `981e1d7`e sabitli, MIT, telif
AGIPro): `walk-forward-validation`, `ohlcv-processing`,
`correlation-analysis`, `vectorbt`, `market-microstructure-traditional`,
`portfolio-analytics`. İlk seçimde `market-microstructure` alınmıştı; içi
okununca Solana DEX akışı olduğu görüldü ve kardeş skill
`market-microstructure-traditional` (emir defteri, fiyat oluşumu, CEX–DEX
farkı) ile değiştirildi.

**`shakeebshaan/claude-code-quant-skills`ten 3 skill** (commit `6b39f8f`e
sabitli, MIT, telif Shaan Shaik): `strategy-critique` (18 soruluk düşmanca
inceleme — Viktor'un beş sorusunu genişletir, yerine geçmez), `backtest-review`,
`data-scrub`.

Dışarıdan alınan 38 dosyanın SHA-256 parmak izi
`.claude/skills/PARMAK-IZLERI.txt` içinde; kaynak, commit, lisans ve kullanım
sınırı `.claude/skills/KAYNAK.md` içinde. Lisans metinleri yanlarında duruyor.

**Tespit edilen çelişme:** `walk-forward-validation` iki sabit eşik taşıyor
("DSR below 0.95", "PBO above 0.50"). Bunlar Balıkçıl'ın kuralı değildir;
şans çizgisi KURALLAR 12'de yazılıdır (1.000 karıştırma, en iyi %1). Çelişme
hâlinde KURALLAR kazanır. DSR/PBO'yu geçme şartına eklemek bir **kural
değişikliğidir** ve önce kullanıcıya sorulur — **açık madde.**

Sıfırdan yazılan skill sayısı üçte kaldı (`defter`, `talimat`,
`duvar-denetimi`); ölçüm ve koşu kaydı için skill yazılmadı, yöntem zaten
KURALLAR 11–12, 29–31 ve TAKTIKLER 7'de yazılı.

**Bağlayıcı sınır:** bu skillerin hiçbiri izleyici talimatı yazarken
kullanılmaz. Skiller Mateo'nun betiklerine, Greta'nın ölçümüne ve Viktor'un
eleştirisine hizmet eder; izleyiciye ne arayacağı söylenmez (KURALLAR 3).
Ajan tanımlarının hiçbirinde `Skill` aracı yok — bu sınır yapısal olarak da
kapalı.
