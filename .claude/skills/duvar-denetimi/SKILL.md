---
name: duvar-denetimi
description: Balıkçıl'ın duvarını denetler — eski projeden sızıntı, talimatlarda yönlendirme, sınav kartlarına erişim, ayar dosyasındaki yolların doğruluğu. Bir ajan koşusundan sonra, bir sınavdan önce ve kullanıcı "sızıntı var mı" diye sorduğunda kullanılır.
allowed-tools: Bash, Read, Glob, Grep
---

## Ayar dosyası

!`cat "${CLAUDE_PROJECT_DIR}/.claude/settings.json"`

## Proje nerede duruyor

!`pwd`

## Ajan tanımları ve duvar alanları

!`for f in "${CLAUDE_PROJECT_DIR}"/.claude/agents/*.md; do printf '%s: ' "$(basename "$f")"; grep -c 'omitClaudeMd: true' "$f" | tr -d '\n'; printf ' omitClaudeMd · tools: '; grep -m1 '^tools:' "$f" | cut -c8-; done 2>/dev/null`

## Kurulu eklentiler

!`claude plugin list 2>&1 | head -20`

## Talimat kopyaları

!`ls -1 "${CLAUDE_PROJECT_DIR}/talimatlar/" 2>/dev/null | grep -v gitkeep | wc -l` talimat kaydı

---

# Denetim — sırayla yap, her maddeyi raporla

Bu denetim **hiçbir dosyayı değiştirmez.** Sadece bakar ve söyler.
Bulduğun her şeyi "geçti / **düştü**" diye işaretle. Düşen madde varsa
kullanıcıya açıkça söyle ve `DEFTER.md`ye yaz.

## 1 · Ayar yolları gerçekten bu klasörü gösteriyor mu

Yukarıdaki `pwd` ile ayar dosyasındaki yolları karşılaştır:

- `autoMemoryDirectory` bu klasörün içini gösteriyor mu? Göstermiyorsa
  **hafıza duvarın dışına yazılıyor** — düşer.
- `claudeMdExcludes` gerçekten var olan bir dosyayı gösteriyor mu?
- `permissions.deny` yolları hâlâ doğru mu?

Proje taşındıysa bu yolların hepsi bayatlar. **Yolların bayatlaması duvarın
sessizce açılmasıdır:** hata vermez, sadece çalışmaz.

## 2 · Talimatlarda yönlendirme var mı (KURALLAR 3)

`talimatlar/` altındaki her dosyayı bu gözle oku:

- Ajana **ne bulacağı** söylenmiş mi?
- "Şuna dikkat et", "genelde şöyle olur", "bak bakalım şu var mı" gibi bir
  cümle var mı?
- Talimatta koordinatörün uydurduğu bir eşik, sayı ya da süre var mı?
- Model ve efor açıkça yazılmış mı (KURALLAR 24)?

Bulduğun her cümleyi **alıntılayarak** raporla. Sızıntı özetlenmez, gösterilir.

## 3 · Eski projeden iz var mı (KURALLAR 1)

`talimatlar/`, `notlar/`, `kantin/`, `betikler/`, `raporlar/` altında ara:

```
grep -ril -e 'freqtrade' -e 'hyperopt' -e 'research_factory' -e 'user_data' \
  talimatlar notlar kantin betikler raporlar
```

Ayrıca bu klasörün dışını gösteren yol var mı:

```
grep -rn -e '\.\./\.\.' -e '/home/user/freqtrade' talimatlar notlar kantin betikler
```

`DEFTER.md` ve `.claude/settings.json` içinde eski proje adının geçmesi
normaldir (taşıma kaydı ve engel listesi). Diğer her yerde geçmesi **düşer.**

## 4 · Sınav kapalı mı (KURALLAR 9, 10)

- `notlar/` ve `kantin/` altında sınav coinlerinin adı, sınav kart numarası ya
  da cevap anahtarından bir satır var mı?
- İzleyici, kantin başkanı ve şüpheci tanımlarında `sinav/` açıkça kapalı mı?
- `sinav-adayi` tanımında `notlar/` ve `kantin/` kapalı mı? `tools:` listesi
  dosya okuyamayacak kadar dar mı?
- Cevap anahtarının parmak izi `DEFTER.md`ye **sınavdan önce** yazılmış mı?
  Sonra yazılmışsa o sınav geçersizdir.

## 5 · Eklenti skilleri duvarı deliyor mu

Kurulu eklentilerin skill listesine bak. Şunu ara: **geçmiş oturum kayıtlarını,
transkriptleri ya da makinedeki başka projeleri okuyan bir skill var mı?**

- `duckdb-skills` içindeki **`read-memories`** böyle bir skilldir: geçmiş oturum
  kayıtlarını arar. Bu makinede eski projenin oturum kayıtları var.
  **Bu skill Balıkçıl'da çalıştırılmaz.** Ne koordinatör çalıştırır ne ajan.
- Ajan tanımlarının `tools:` listesinde `Skill` **yoktur** — böylece hiçbir ajan
  bir skill çağırıp duvarı dolaşamaz. Bir tanıma `Skill` eklenmişse düşer.

## 6 · Komut satırı deliği (KURALLAR 5)

Ayarlar `Bash` ile dosya okumayı engelleyemez. Bu yüzden:

- Elinde `Bash` olan tek ajan `veri-ustasi` mi? Başka birine verilmişse düşer.
- `talimatlar/` altındaki komutlarda kapsamı klasör dışına taşan bir şey var mı
  (`..`, mutlak yol, kök dizinde `find`)?
- Bu deliği kapatan bir `PreToolUse` hook'u kuruldu mu? Kurulmadıysa bunu
  **her denetimde açık madde olarak yaz** — kapanmamış bir delik unutulmaz.

## 7 · Rapor

Kullanıcıya şu sırayla, sade:

1. Kaç madde geçti, kaç madde düştü.
2. Düşen her madde: ne, nerede, alıntısıyla.
3. Kapanmamış açık delikler, adıyla.
4. Hiçbir şey bulunmadıysa: **nereye bakıldığı** (KURALLAR 20 — "yok" demeden
   önce nereye bakıldığı yazılır).

Sonra kaydı `/defter` ile deftere geçir.
