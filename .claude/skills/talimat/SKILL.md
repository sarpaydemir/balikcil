---
name: talimat
description: Bir Balıkçıl ajanına talimat yazar, sızıntı denetiminden geçirir, tam kopyasını talimatlar/ klasörüne kaydeder ve ajanı çalıştırır. İzleyici, kantin başkanı, şüpheci, veri ustası ya da sınav adayı çalıştırılacağı zaman kullanılır.
allowed-tools: Bash, Read, Write, Glob, Grep
argument-hint: [ajan adi] [is]
---

## Mevcut ajanlar

!`ls -1 "${CLAUDE_PROJECT_DIR}/.claude/agents/" 2>/dev/null | sed 's/\.md$//'`

## Şimdiye kadar yazılan talimatlar

!`ls -1 "${CLAUDE_PROJECT_DIR}/talimatlar/" 2>/dev/null | grep -v '^\.gitkeep$' | tail -n 15`

## Saat

!`date -u '+%Y-%m-%d %H:%M UTC'`

## İş

**$ARGUMENTS**

Bir ajan çalıştırmadan önce talimat yazılır ve **tam kopyası saklanır.**
Kullanıcı istediği an sızıntı var mı diye bakabilir (KURALLAR 4).

### 1 · Talimatı yaz

Şu iskeletle:

```
# Talimat — <ajan> · <tarih saat UTC> · <iş adı>

## Kim
<ajan adı ve rolü — tanımında yazılı olanı tekrarlama, sadece hangi rolde
çalıştığını söyle: örn. "izleyici · bakış alanı: fiyatın kendisi", "veri ustası ·
Mod B (kör sınav kartı)">

## Model ve efor
model: <opus/…> · efor: <low/medium/high/xhigh/max>
Gerekçe: <neden bu efor>

## Neye bakabilirsin
<yalnız dosya yolları ve alanlar. HİÇBİR sonuç, tahmin, eşik ya da
"şuna dikkat et" cümlesi olmaz.>

## Neye bakamazsın
<kapalı klasörler — özellikle sinav/ kapalıysa açıkça yaz>

## Çıktı
<hangi dosyaya, hangi biçimde>

## Duvar
Bu klasörün dışındaki hiçbir dosyayı okuma: ne araçla ne komut satırıyla.
`..` ile yukarı çıkma, dışarıyı gösteren mutlak yol kullanma.
```

### 2 · Sızıntı denetimi — talimatı çalıştırmadan önce

Yazdığın talimatı bu gözle **yeniden oku:**

- **Sonuç var mı?** Ajana ne bulacağı söylenmiş mi? Söylenmişse sil (KURALLAR 3).
- **Yönlendirme var mı?** "Şuna dikkat et", "genelde şöyle olur", "bak bakalım
  şu var mı" — hepsi yönlendirmedir, silinir.
- **Eşik var mı?** Talimatta kendi uydurduğun bir sayı varsa sil ya da nereden
  geldiğini yaz.
- **Eski projeden bir şey var mı?** Başka bir laboratuvardan gelen hiçbir
  bulgu, sayı, dosya adı ya da kanaat talimatta olmaz.
- **Model ve efor açıkça yazıldı mı?** (KURALLAR 24)
- **Sınav kapalı mı?** İzleyici, kantin başkanı ve şüpheci için `sinav/` kapalı
  olmalı. Sınav adayı için `notlar/` ve `kantin/` kapalı olmalı.
- **Sınav adayına verilen tarif dışında bir şey var mı?** Tarifsiz aday
  (Tomás) hiçbir yöntem ipucu görmez; tarifli aday (Hana) yalnız donmuş tarifi
  görür. İkisinin **modeli ve eforu aynı olmalı** — yoksa kıyas adil değildir.

### 3 · Kopyayı kaydet

Talimatın **tam metnini**, ajana gönderdiğin hâliyle, şuraya yaz:

```
talimatlar/<YYYY-MM-DD-HHMM>-<ajan>-<is-adi>.md
```

Özet değil, **tam kopya.** Ajana giden metin ile kaydedilen metin aynı olmalı.

### 4 · Çalıştır

Ajanı `Agent` aracıyla, `subagent_type` olarak ajanın adıyla çalıştır. Modeli
ve eforu ajan tanımından gelir; talimatta yazdığın değerden farklıysa tanımı
düzelt, talimatı değil.

10 dakikadan uzun sürecek işi oturum kapansa da ölmeyecek şekilde başlat
(KURALLAR 26).

### 5 · Sonra

- İlk 10 kartta harcanan tokeni ölç, tam koşunun tahminini `DEFTER.md`ye yaz ve
  başlamadan önce kullanıcıya **tek cümleyle** söyle (KURALLAR 25).
- Ajanın raporunda "talimatta yönlendirme gördüm" diyorsa **dur** ve kullanıcıya
  söyle.
- Kaydı `/defter` ile deftere geçir.
