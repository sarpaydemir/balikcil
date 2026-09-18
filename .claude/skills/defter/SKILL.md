---
name: defter
description: Balıkçıl'ın DEFTER.md dosyasına yeni bir kayıt ekler. Sadece ekler, hiçbir satırı silmez ya da değiştirmez. Saati sistemden okur, tahmin etmez. Bir şey kurulduğunda, bir karar alındığında, bir koşu yapıldığında, bir parmak izi alındığında, bir kural değiştiğinde kullanılır.
allowed-tools: Bash, Read
argument-hint: [kaydin konusu]
---

## Şu anki saat (sistemden okundu)

!`date -u '+%Y-%m-%d %H:%M UTC'`

## Defterin son hâli

!`tail -n 12 "${CLAUDE_PROJECT_DIR}/DEFTER.md"`

## Kayıt uzunluğu (bu kayıttan önce)

!`wc -l < "${CLAUDE_PROJECT_DIR}/DEFTER.md"` satır

## Yapılacak

Konu: **$ARGUMENTS**

`DEFTER.md`ye tek bir kayıt **eklenir.** Kural: *sadece eklenir, hiçbir satır
silinmez* (DEFTER.md'nin kendi başlığı).

1. **Yukarıdaki saati kullan.** Saati tahmin etme, hatırlamaya çalışma, başka
   yerden alma (KURALLAR 23). Yukarıda yazan neyse o.
2. Kaydı şu biçimde yaz:

   ```
   `YYYY-MM-DD HH:MM UTC` · **kısa etiket** · ne oldu. Neye dayanıyor, hangi
   dosya, varsa parmak izi. Ölçülmemiş sayı yazma; tahminse yanına "tahmin" yaz
   (KURALLAR 19).
   ```

3. **Sadece dosyanın sonuna ekle.** Var olan hiçbir satıra dokunma. Ekleme
   işlemini `>>` ile yap, `Write` aracıyla dosyanın tamamını yeniden yazma —
   yeniden yazmak eski satırları kaybetme riski taşır.
4. Ekledikten sonra satır sayısının **arttığını** doğrula. Azaldıysa ya da aynı
   kaldıysa dur ve kullanıcıya söyle.

## Kayda mutlaka girecek şeyler

- Bir **karar** alındıysa: kararı kim verdi (kullanıcı mı, koordinatör mü) ve
  hangi kuralın yerine geçtiği.
- Bir **koşu** yapıldıysa: koşu numarası (girdinin parmak izi) ve çıktı dosyası
  (KURALLAR 29).
- Bir **mühürleme** yapıldıysa: cevap anahtarının parmak izi (KURALLAR 9).
- Bir **kural değiştiyse**: önce kullanıcıya sorulduğuna dair not (KURALLAR başı).
- Bir **tahmin** varsa: yanında "tahmin" kelimesi.
- **Ölçülemeyen** bir şey varsa: adıyla. "Ölçülemedi" asla "sorun yok"a
  dönüşmez (KURALLAR 22).
