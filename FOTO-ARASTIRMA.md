# 📸 MENÜ FOTOĞRAF ARAŞTIRMASI — telifsiz stok fotoğraflar

> **Durum: ✅ UYGULANDI (3 Ağustos 2026).** 11 fotoğraf indirildi, gözle elendi, tek tipe
> getirildi, `assets/`e kondu, iki HTML dosyasında da devreye alındı, canlıya çıktı.
> Bu dosya artık **hangi karenin nereden geldiğinin kaydı**.

## ✅ SİTEDE KULLANILAN 11 KARE (kesin liste)

| Dosya (`assets/`) | Ürün | Pexels ID | Neden bu |
|---|---|---|---|
| `yemek-tavuk-durum.jpg` | Tavuk Dürüm | **6416559** | Kesilmiş tavuk dürümler üst üste, tavuk eti net görünüyor |
| `yemek-tavuk-sis-durum.jpg` | Tavuk Şiş Dürüm | **9980749** | Tavuk parçalı dürüm, ahşap zemin |
| `yemek-kofte-durum.jpg` | Köfte Dürüm | **36750272** | Koyu ahşap tabakta dürüm + patates |
| `yemek-adana-durum.jpg` | Adana Dürüm | **11286814** | Kırmızı/acılı görünen et, lavaşa sarılı, sıcak ton |
| `yemek-kuzu-sis-durum.jpg` | Kuzu Şiş Dürüm | **15390220** | Çörek otlu lavaş rulolar — en "Türk" duran kare |
| `yemek-pilav-ustu-doner.jpg` | Pilav Üstü Tavuk Döner | **18062062** | Tabakta **tavuk** döner + pilav (18062061 aynı setin *etli* hali, ona dikkat) |
| `yemek-tavuk-sis-servis.jpg` | Tavuk Şiş Servis | **5643427** | Koyu ahşap tahtada tavuk şişler |
| `yemek-kanat-servis.jpg` | Kanat Servis | **31587878** | Kanatlar + közlenmiş biber, lavaş üstünde |
| `yemek-kofte-servis.jpg` | Köfte Servis | **37206707** | Köfte + közlenmiş domates/biber + soğan — birebir Türk sunumu |
| `yemek-adana-servis.jpg` | Adana Servis | **7439809** | Ahşap tabakta Adana, lavaş, ezme, yeşillik |
| `yemek-kuzu-sis-servis.jpg` | Kuzu Şiş Servis | **37206698** | Kuzu şişler, soğan piyazı, koyu ahşap masa |

**Elenenler ve nedeni:** 34106235 (kadraj çok yakın, dürüm şekli kaybolmuş) · 15913640 (tavuk
görünmüyor, peynirli sandviç gibi duruyor) · 5175618 (kanat değil köfte gibi okunuyor) ·
18330008 / 5175625 (bembeyaz zemin, koyu temaya oturmuyor) · 14774691 / 14774690 (yeşil zemin) ·
5779382 (paket kutusu, yemek görünmüyor).

**Nasıl tek tip yapıldı:** `_foto-uretim.py` — 1200×900 (4:3) kırpma, merkez parlaklığı eşitleme,
hafif sıcak ton, sonra kenarların **`#1c140f`** közüne gömülmesi (elips vinyet). Böylece 11 farklı
fotoğrafın birbirini tutmayan masası/duvarı/mermeri kayboldu, hepsi **aynı arka planda** duruyor.

---

## Aşağısı: seçim yapılırken kullanılan araştırma (yedek ID'ler burada)

## Neden bu dosya var

Kullanıcı isteği: *"menüdeki tavuk dürüm görüntüsü falan SVG olarak çok çocuksu kötü duruyor,
internetten telifsiz bulup fotoğrafları değiştirebilir misin, hepsi aynı olsun."*

Bu, PROGRESS.md bölüm 4h'deki **"stok fotoğraf yok"** kararının bilinçli olarak geri alınmasıdır.
Uygulanınca oradaki not güncellenecek (aşağıda "yapılacaklar"da yazılı).

---

## 1. KAYNAK VE LİSANS

**Pexels** seçildi — https://www.pexels.com

- **Pexels License:** ticari kullanım serbest, **atıf (kaynak yazma) zorunlu değil**, ücretsiz.
  Bir restoran sitesi için tam uygun. Lisans metni: https://www.pexels.com/license/
- Yasak olan tek şey: fotoğrafı **olduğu gibi satmak** veya "kendi çektiğim" diye stok siteye
  yeniden yüklemek. Bizim kullanımımız (kendi sitende ürün görseli) serbest.
- Alternatif kaynaklar (gerekirse): Unsplash, Pixabay — ikisi de aynı şekilde ücretsiz/ticari serbest.

**Doğrudan görsel adresi kalıbı** (indirmek için):
```
https://images.pexels.com/photos/ID/pexels-photo-ID.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop
```
`w=1200&h=900` → **4:3**, yani şu anki SVG'lerin (400×300) oranıyla birebir aynı.
Sayfadaki kutu ölçüleri hiç değişmeden yerine oturur.

⚠️ **Ben bu fotoğrafları henüz GÖRMEDİM.** Aşağıdaki seçimler Pexels'in kendi açıklama
metinlerine göre yapıldı. Uygulama aşamasında hepsi indirilip **tek tek bakılacak**, uymayan
olursa yedeğiyle değiştirilecek. O yüzden her ürüne 1 asıl + 2 yedek konuldu.

---

## 2. ÜRÜN → FOTOĞRAF EŞLEŞMESİ (11 ürün)

### 🌯 Dürüm (5 ürün)

| # | Ürün | Asıl seçim (ID) | Ne olduğu | Yedek 1 | Yedek 2 |
|---|---|---|---|---|---|
| 1 | **Tavuk Dürüm** | **27744717** ⭐ | Pexels'te adı birebir *"tavuk dürüm döner"* — közde dürüm, Türk sokak lezzeti | 29306505 | 18330008 |
| 2 | **Tavuk Şiş Dürüm** | **10027451** | Tavuklu dürüm, içinde taze sebze, yakın plan | 9980749 | 14774691 |
| 3 | **Köfte Dürüm** | **36750272** | Etli dürüm, ahşap tabakta, yanında patates | 36750271 | 37322774 |
| 4 | **Adana Dürüm** | **15202777** | Doyurucu Türk dürümü, patates ve sos ile | 9980764 | 5175625 |
| 5 | **Kuzu Şiş Dürüm** | **5779413** | Elde tutulan taze dürüm, içi görünüyor | 5779382 | 14774690 |

### 🍽️ Porsiyon / Servis (6 ürün)

| # | Ürün | Asıl seçim (ID) | Ne olduğu | Yedek 1 | Yedek 2 |
|---|---|---|---|---|---|
| 6 | **Pilav Üstü Tavuk Döner** | **18062062** ⭐ | Türk döneri; tabakta pilav + sebze ile | 18062061 | 19805189 |
| 7 | **Tavuk Şiş Servis** | **32754748** | Izgara tavuk şiş, tabakta, yeşillikle süslü | 32754752 | 5643427 |
| 8 | **Kanat Servis** | **5175618** ⭐ | Izgara kanat, **lavaş üstünde**, taze yeşillik — tema birebir | 11299743 | 31587878 |
| 9 | **Köfte Servis** | **37206707** ⭐ | Türk köftesi; közlenmiş domates, biber, soğan, lavaş | 35366590 | 37331151 |
| 10 | **Adana Servis** | **7439809** ⭐ | Adana kebabı, ahşap tabakta, yeşillik + lavaş (tepeden) | 16260570 | 15873840 |
| 11 | **Kuzu Şiş Servis** | **37206698** | Kuzu kebap, soğan ve domatesle, ahşap masada | 6089832 | 9510363 |

⭐ = açıklaması ürüne birebir oturan, en güvenli seçimler.

**Fotoğraf sayfasını tarayıcıda görmek için:** `https://www.pexels.com/photo/ID/`
(örn. https://www.pexels.com/photo/27744717/ )

### "Hepsi aynı olsun" ne demek — uygulama kuralı
1. Hepsi **aynı oran (4:3)**, aynı piksel ölçüsü (**1200×900**), aynı sıkıştırma.
2. Hepsi **aynı sıcak/koyu tonda** — indirdikten sonra hafif renk düzeltmesiyle birbirine
   yaklaştırılacak (sitenin ateş/köz teması). Biri parlak beyaz stüdyo, öteki karanlık olmayacak.
3. **Aynı fotoğraf iki üründe kullanılmayacak** — 11 ürün, 11 ayrı kare.
4. `index.html` ve `menu.html` **aynı dosyayı** gösterecek (zaten öyle).

---

## 3. UYGULAMA PLANI (bir sonraki oturumda — hepsi tek seferde yapılır)

1. 11 asıl + 22 yedek fotoğraf geçici klasöre indirilir (`scratchpad`), **gözle bakılır**, eleme yapılır.
2. Seçilenler 1200×900 4:3 kırpılır, ~150-250 KB'a sıkıştırılır, ton olarak birbirine yaklaştırılır.
3. `assets/` içine **SVG'lerle aynı isimle, uzantısı `.jpg`** kaydedilir:
   `yemek-tavuk-durum.jpg`, `yemek-tavuk-sis-durum.jpg`, `yemek-kofte-durum.jpg`,
   `yemek-adana-durum.jpg`, `yemek-kuzu-sis-durum.jpg`, `yemek-pilav-ustu-doner.jpg`,
   `yemek-tavuk-sis-servis.jpg`, `yemek-kanat-servis.jpg`, `yemek-kofte-servis.jpg`,
   `yemek-adana-servis.jpg`, `yemek-kuzu-sis-servis.jpg`
4. `index.html` (11 satır) + `menu.html` (11 satır) içinde `.svg` → `.jpg`.
   **Başka hiçbir şeye dokunulmaz** — `width/height/alt/loading` aynı kalır, CSS değişmez.
   Kontrol: `grep -c "yemek-.*\.jpg" index.html menu.html` → ikisi de **11** dönmeli.
5. SVG'ler **silinmez**, `assets/` içinde durur (beğenilmezse tek komutla geri dönülür).
6. ⚠️ **Alttaki dürüstlük notu iki dosyada da değişecek.** Şu an yazan:
   > *"Görseller ürünleri tanıtmak için hazırlanmış çizimlerdir; sunum değişebilir."*

   Artık çizim değil stok fotoğraf olacağı için bu cümle yanlış olur. Yerine:
   > *"Görseller temsilidir; sunum değişebilir."*

   **Bu notu tamamen silme.** Fotoğraflar dükkânın kendi yemeği değil — müşteri tabağı görünce
   "resimdeki gibi değil" demesin diye baştan söylüyoruz. (Amcanın da bilmesi gereken şey bu.)
7. Yerel test (`python -m http.server 8099`) → 22/22 görsel yükleniyor mu, 375px'te taşma var mı,
   konsol temiz mi. Sonra `git add . && git commit && git push`.
8. `PROGRESS.md` güncellenir: bölüm 4h "elle çizilmiş SVG" → "stok fotoğraf" olarak yeniden yazılır,
   oturum günlüğüne satır eklenir, kararın geri alındığı not düşülür.

⚠️ **`assets/` klasörü herkese açık** — indirilen fotoğraflar dışında oraya bir şey sızmasın
(PROGRESS.md bölüm 4 uyarısı hâlâ geçerli).

---

## 4. AKILDA TUTULACAK İKİ ŞEY

- **Bu fotoğraflar dükkânın kendi yemeği değil.** Amcanın "bu bizim tabağımız değil ki" demesi
  ihtimali var — kararı kullanıcı verdi, ama söylenmesi gereken şey bu. Gerçek yemek fotoğrafı
  çekilirse (çekim rehberi: PROGRESS.md bölüm 4b) stoklar tek tek onlarla değiştirilir; dosya
  isimleri aynı olduğu için **HTML'e hiç dokunmadan** üzerine yazmak yeterli.
- **Hero (`dis-cephe.jpg`) ve galeri stok OLMAYACAK.** Mekânın kendi fotoğrafı orada şart —
  dükkânı yanlış tanıtmak olur. Stok sadece menüdeki ürün kartlarında.
