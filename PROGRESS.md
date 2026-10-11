# 🔥 LEZZET OCAKBAŞI — PROJE HAFIZASI

> **Bu dosya projenin tek hafızası.** Sohbet kapansa, token bitse, aylar sonra dönülse
> buradan devam edilir. **Her değişiklikte bu dosya güncellenir.**
> Son güncelleme: **2026-08-03**

---

## 1. İŞLETME BİLGİLERİ (canlı gerçek)

| Alan | Değer |
|---|---|
| Ad | Lezzet Ocakbaşı |
| Tür | Ocakbaşı / Mangal / Dönerci |
| Adres | Mevlana Mah., 38280 Talas / Kayseri |
| Telefon | (0352) 431 44 00 |
| Google puanı | 4,4 ★ (52 yorum) |
| **Çalışma saati** | **Her gün 11:30 – 22:00** ✅ ikisi de teyitli (23 Tem 2026) — kapanış Google'dan, açılış amcadan |
| Plus Code | PH27+RW Talas, Kayseri |
| Sahibi | Kullanıcının amcası |
| Google işletme profili | Amcanın kendi bilgisayarında Google hesabıyla giriş yapılmış durumda — saatler oradan düzenlendi ✅ |

---

## 2. YAYIN / ERİŞİM

- **🌐 CANLI SİTE (ASIL ADRES):** **https://lezzetocakbasi.netlify.app**
- Yedek adres (GitHub Pages, açık kalsın): https://ismetguler.github.io/lezzet-ocakbasi/
- **GitHub repo:** https://github.com/ismetguler/lezzet-ocakbasi (public, hesap: `ismetguler`)
- **Yerel klasör:** `C:\Users\ismet\Desktop\newjob\lezzet-ocakbasi\`
- **Netlify:** site adı `lezzetocakbasi`, GitHub hesabıyla giriş yapılıyor (ayrı Netlify şifresi YOK).
  Repoya bağlı → her push otomatik yayınlanır. Ayarlar `netlify.toml` dosyasında, panelde bir şey seçmeye gerek yok.
- Pages kaynağı (yedek): `main` branch, kök (`/`). HTTPS zorunlu.
- Git kimliği: `ismetguler` / `gulerrismet@gmail.com`
- ⚠️ **pages.dev KULLANMA** — Türkiye'de engelli (23 Tem 2026'da test edildi, bağlantı reddedildi).

### Değişiklik yayınlama (ezber komut)
```bash
cd "C:/Users/ismet/Desktop/newjob/lezzet-ocakbasi" && git add . && git commit -m "guncelleme" && git push
```
Push'tan 1–2 dakika sonra **hem Netlify hem GitHub Pages** kendiliğinden yenilenir. Tarayıcıda değişikliği görmüyorsan **Ctrl+F5** (sert yenileme).

### Yerel önizleme
```bash
cd "C:/Users/ismet/Desktop/newjob/lezzet-ocakbasi" && python -m http.server 8099
```
→ http://127.0.0.1:8099

---

## 3. TEKNİK YAPI

```
lezzet-ocakbasi/
├── index.html      → tüm içerik + SEO meta + JSON-LD (Restaurant schema)
├── menu.html       → QR MENÜ sayfası (tek dosya, kendi CSS/JS'i içinde)
├── styles.css      → tema, animasyonlar, responsive, FOTO SLOTLARI
├── script.js       → scroll reveal, mobil menü, sayaçlar, köz partikülleri, menü sekmeleri
├── assets/         → fotoğraflar buraya (şu an BOŞ)
├── netlify.toml    → Netlify ayarları (build yok, önbellek başlıkları)
├── DUKKAN-GOREV.md → dükkan ziyareti görev listesi (telefondan bakılıyor)
└── PROGRESS.md     → bu dosya (proje hafızası)
```

- Saf HTML + CSS + JS. Framework yok, build yok → her yerde barınır, çok hızlı.
- Tema: **ateş/köz (ember)** — koyu antrasit zemin + turuncu/kırmızı sıcak tonlar.
- Tek sayfa: Hero → Hakkında → Menü → Galeri → Yorumlar → İletişim/Harita → Footer.
- Mobil öncelikli responsive (375px'te test edildi, taşma yok).

---

## 4. NASIL DÜZENLENİR (kritik bilgi — burayı oku)

### 🚨 ASSETS KLASÖRÜNE ŞİFRE/ÖZEL BELGE FOTOĞRAFI KOYMA
`assets/` klasöründeki her şey **GitHub'da herkese açık** ve `lezzetocakbasi.netlify.app/assets/dosyaadi.jpg`
adresinden internete servis edilir. 2 Ağustos 2026'da amcanın **Gmail şifrelerinin yazılı olduğu defter fotoğrafı**
yanlışlıkla buraya atılmıştı, push edilmeden fark edilip çıkarıldı.
**Kural: assets/ klasörüne sadece siteye konacak yemek/mekân fotoğrafı girer.** Şifre, fatura, kimlik, defter → asla.
Push etmeden önce her seferinde `assets/` içine bir bak.

### 📸 Fotoğraf eklemek → EN KOLAY İŞ
`assets/` klasörüne şu **tam isimlerle** at, başka hiçbir şey yapmana gerek yok:

| # | Dosya adı | Nereye düşer | Ne çekilecek |
|---|---|---|---|
| ⭐ | `assets/dis-cephe.jpg` | **HERO — sayfanın en üstü, en önemli foto** | Dükkân dıştan, akşam mavi saatte |
| 1 | `assets/doner.jpg` | Galeri — "Közde Döner" | Döner kesilirken, bıçak+et yakın |
| 2 | `assets/usta.jpg` | Galeri — "Ustanın Elinden" | Usta iş başında, elleri/şiş görünsün |
| 3 | `assets/kebap.jpg` | Galeri — "Mangal Kebap" | Tabakta servis kebap, 45° |
| 4 | `assets/ocak.jpg` | Galeri — "Ocakbaşı" | Ocağın kendisi, kor ve alev |
| 5 | `assets/mangal.jpg` | Galeri — "Köz Başında" | Mangalda pişen etler, yakın |
| 6 | `assets/sofra.jpg` | Galeri — "Sofra Keyfi" | Donatılmış masa, tepeden |
| 7 | `assets/dis-masa.jpg` | Galeri — "Dışarıda Oturmak" | Dış masalar, akşamüstü ışıkta |
| 8 | `assets/salon.jpg` | Galeri — "Salonumuz" | Temiz/boş salon, köşeden |
| 9 | `assets/lavas.jpg` | Galeri — "Lavaş & Garnitür" | Lavaş, salata, garnitür yakın |

**Galeri 3×3 tam ızgara (9 kutu).** Hepsi dolarsa mükemmel görünür; eksik kalanlar gradyan olarak durur, kırık görünmez.

**📌 2 Ağustos 2026 itibarıyla assets/ içinde ne var:**

| Dosya | Durum |
|---|---|
| `dis-cephe.jpg` | ✅ Hero fotoğrafı + `og:image`. **Düzenlenmiş hali** (aşağıya bak), 2048×865. |
| `kampanya-afis.jpg` | ✅ Kampanya afişi — kampanya bölümünde gösteriliyor. Web için 1600px'e küçültüldü. |
| `_ham-dis-cephe-1.jpg` | Ham çekim #1 (dokunulmamış). Yedek. |
| `_ham-dis-cephe-2.jpg` | Ham çekim #2 (dokunulmamış). **Yayındaki foto bundan üretildi.** |
| `_menu-fiyat-referans.jpg` | Dükkandaki A4 fiyat listesinin fotoğrafı. **Siteye konmuyor**, fiyatları buradan okuduk. |
| Galeri 9 slot | ❌ Boş — galeri bölümü bu yüzden geçici kapatıldı (bkz. 4f). |

> Başında `_` olan dosyalar siteye konmayan çalışma dosyalarıdır.

### 🖼️ Dış cephe fotoğrafına ne yapıldı (2 Ağu 2026)
Kullanıcının isteği: **"insanları o fotodan sil, kötü görüntü olmasın."** Yapılanlar:
1. **Ham çekim #2 temel alındı** — #1 ile aynı kadraj ama sahnedeki kişiler çok daha az yer kaplıyordu,
   yani silinecek alan küçüktü → sonuç temiz çıktı. (#1 ile denendi, silinen yerler bulanık leke bıraktı.)
2. **Alttan kırpıldı (1536 → 865 px).** Tabureye oturan adam, sağdaki adamın gövdesi ve afiş arkasındaki
   ayaklar bu satırın altında kalıyordu. Alt taraf zaten bomboş karo zemindi — kırpmak kadrajı da sıkılaştırdı.
3. Bantta kalan 3 kişi **inpaint** ile silindi (ayakta duran adam, camdaki tezgahtaki kişi, sağdaki adamın kafası).
4. Gece çekimi olduğu için hafif ışık/kontrast düzeltmesi (CLAHE) yapıldı.

⚠️ Silinen yerlerde çok yakından bakınca hafif yumuşama var — normal boyutta ve hero'daki koyu katman
altında fark edilmiyor. Tekrar üretmek gerekirse: script `_ham-dis-cephe-2.jpg`'den çalışır, kırpma satırı `CUT=865`.

⚠️ Foto **gece ve karanlık** çekilmiş. "Mavi saat" (gün batımından 20–30 dk sonra, ~20:35–21:00) çekimi
çok daha iyi olur — **ve o saatte dükkânın önü boşken çekilirse bu silme işine hiç gerek kalmaz.**

CSS `url(...) , linear-gradient(...)` şeklinde yazıldı: **dosya varsa foto görünür, yoksa eski gradyan görünür.** Kırık resim ikonu çıkmaz.
Hero'da fotoğrafın üstünde koyu katman var → hangi foto konursa konsun yazılar okunur kalır.

---

## 4b. 📷 FOTOĞRAF ÇEKİM REHBERİ (telefonla, profesyonel görünsün)

### ⚠️ YATAY / DİKEY KURALI (sık sorulan)
- **Site için YATAY şart.** Hero ve galeri yatay alanlar; dikey foto konursa üstü-altı kesilir.
- **Ama her kareyi iki kez çek: önce yatay, sonra aynı yerden dikey.** İki saniyelik iş.
  - Yatay → bu site
  - Dikey → Instagram/WhatsApp durumu, Google işletme profili
- Tek istisna yok; dolu sofra ve tepeden çekimlerde bile yatay çek, kare gibi dursa da olur.

### Telefon ayarları — bir kere yap, hep açık kalsın
- **Yatay tut** (telefonu yan çevir).
- **Izgara/Grid'i aç** (Ayarlar → Kamera → Izgara). Çizgileri düz tutmak için.
- **Flaş KAPALI** — her zaman. Flaş yemeği yağlı, mekânı ucuz gösterir.
- **HDR açık.**
- Objektifi **gömlek ucuyla sil** — telefon kamerası hep yağlı olur, en sık yapılan hata bu.
- **Zoom yapma.** Yaklaşman gerekiyorsa ayağınla yaklaş. Zoom görüntüyü bozar.
- 1x lens kullan (0.5x geniş açı mekânı çarpıtır, sadece dar salon için).

### 🌆 DIŞ CEPHE (`dis-cephe.jpg`) — en önemli kare
- **Saat çok kritik: "mavi saat".** Gün batımından **20–30 dakika sonra.** Temmuz'da Kayseri'de gün batımı ~20:15 → **20:35 – 21:00 arası çek.**
  - Neden: gökyüzü daha lacivert (siyah değil), tabela ve iç ışıklar yanmış durumda. Reklam fotoğraflarının tamamı bu ışıkta çekilir.
  - Zifiri karanlıkta çekme → gökyüzü kapkara delik olur, ucuz durur.
- Çekmeden önce: **dükkânın BÜTÜN ışıklarını aç** (tabela, iç, varsa dış aydınlatma), masaları topla/düzelt, önündeki çöp kovası–kasa–araba varsa çektir, camları sil.
- Karşı kaldırıma geç, dükkânı tam karşıdan al. Tabela net okunsun.
- **Telefonu göğüs–göz hizasında ve YERE PARALEL tut.** Yukarı doğru eğersen bina arkaya devriliyormuş gibi çıkar.
- Ekranda **tabelaya bir kere dokun** (odak+pozlama kilitlenir), sonra parmağını yukarı-aşağı kaydırıp **pozlamayı biraz kıs** ki tabela yazısı patlamasın, okunur kalsın.
- **Nefesini tut, 2 saniye kıpırdama** — akşam çekiminde en büyük düşman titreme. Varsa bir duvara/direğe yaslan.
- Aynı kareden **en az 5 tane** çek, sonra en netini seçeriz.
- Bonus: içeride birkaç kişi otururken çek — dolu mekân her zaman daha davetkâr durur (yüzler net görünüyorsa izin al).

### 🔥 OCAK / USTA (`ocak.jpg`)
- Közün başında usta et çevirirken, **yandan ve yakından.** Alevler ve kor görünsün.
- Ortam ışığını kısma — ocağın kendi turuncu ışığı zaten sıcak duruyor, en güzel kare bu olur.
- Hareket var, o yüzden bol bol çek; 10 karenin 2'si net çıkar.

### 🥙 YEMEK KARELERİ (`doner.jpg`, `kebap.jpg`, `lavas.jpg`, `sofra.jpg`)
- **Gündüz, pencere kenarında çek.** Tavandaki sarı lamba yemeği hasta gösterir. Doğal ışık şart.
- Işık **yandan** gelsin (pencere solunda/sağında olsun), arkandan değil — arkadan gelirse gölgen tabağa düşer.
- Tabağı servis etmeden önce **kenarındaki damlaları peçeteyle sil.** Bir saniyelik iş, farkı çok büyük.
- İki açıdan çek, ikisini de gönder:
  1. **45 derece** (masaya oturmuş biri gibi bak) → kebap, döner için en iyi.
  2. **Tam tepeden** (tabak/sofra düz yukarıdan) → dolu sofra, lavaş-garnitür için en iyi.
- Arka planı sadeleştir: ketçap şişesi, telefon, peçetelik, anahtar → kadraj dışına.
- `doner.jpg` için: **döner kesilirken, bıçak ve etin dönerken** çek. Hareket iştah açar.
- `sofra.jpg` için: masayı tam donat (kebap + lavaş + salata + ayran), tepeden çek.

### 👨‍🍳 USTA & MANGAL (`usta.jpg`, `mangal.jpg`) — kullanıcının kendi fikri, çok iyi kareler
- **`usta.jpg`:** usta şişleri çevirirken **yandan**, elleri ve ateş aynı karede olsun. Yüzü net görünüyorsa izin al; sadece eller/şiş de yeter, hatta bazen daha iyi durur.
- **`mangal.jpg`:** mangalın üstündeki etlere **yakın plan**, dumanı ve közü yakala.
- Ocağın turuncu ışığı zaten sıcak duruyor, ayrıca ışık ayarlama. **Flaş asla.**
- Hareket var → **10-15 kare çek**, birkaçı net çıkar. Seri çekim (deklanşöre basılı tut) kullan.

### 🪑 DIŞ MASALAR (`dis-masa.jpg`) — kullanıcının kendi fikri, reklam açısından değerli
- **Akşamüstü**, dış cephe çekiminden hemen önce (hava henüz tamamen kararmadan).
- Masalar kurulu, sandalyeler düzgün, üstünde birkaç şey olsun (çay bardağı, peçetelik).
- Varsa üstteki ışıklar/tenteler açık olsun.
- Alçaktan çek — masa hizasından bakınca "otur da yiyelim" hissi veriyor.

### 🪑 SALON (`salon.jpg`)
- **Müşteri gelmeden önce, mekân tertemiz ve boşken.** Sandalyeler hizalı, masalar açık.
- Köşeden çek — köşeden çekilen mekân daha geniş görünür.
- Tüm ışıklar açık, gündüz ise perdeler açık.

### Sonrası
- Fotoğrafları bilgisayara at → `lezzet-ocakbasi/assets/` klasörüne **tam bu isimlerle** kaydet.
- Boyutlandırma/sıkıştırma gerekirse ben hallederim, sen ham halini koy yeter.
- Emin olamadığın kareler olursa hepsini at, birlikte seçeriz.

---

## 4d. 🔥 KAMPANYA BÖLÜMÜ (sayfanın en üstü — hero'nun hemen altı)

Kullanıcının isteği: **kampanya oldukça siteye en başa konacak.**
`index.html` içinde `<section class="promo" id="kampanya">` bloğu. Değiştirilecek 4 şey:

| Ne | Nerede |
|---|---|
| Başlık | `<h2 class="promo-title"><span class="promo-kg">1 KG</span> Tavuk Kanat</h2>` |
| Yanındakiler | `<ul class="promo-extras">` içindeki `<li>` satırları |
| Fiyat | `<div class="promo-price"><b>450</b><span>₺</span></div>` |
| Afiş fotoğrafı | `assets/kampanya-afis.jpg` dosyasının üzerine yenisini yaz (aynı isimle) |

- **Kampanya bitince:** bu `<section>`'ı komple sil **+** navbardaki `<a href="#kampanya" class="nav-hot">Kampanya</a>` satırını sil **+** hero'nun altındaki `scroll-hint` linkini `#hakkinda`'ya çevir.
- Afiş fotoğrafı `loading="eager"` — sayfanın üstünde olduğu için bilerek böyle, lazy yapma.
- Mobilde otomatik tek sütuna düşüyor (860px altı), test edildi.

---

## 4f. 🖼️ GALERİ BÖLÜMÜ — ŞU AN KAPALI

Fotoğraflar çekilmediği için 9 kutunun hepsi boş gradyan görünüyordu; **2 Ağu 2026'da geçici olarak
yorum satırına alındı** (silinmedi). Fotoğraflar `assets/`e atılınca **açmak için tek iş:**

1. `index.html` → `GALERİ — GEÇİCİ OLARAK KAPALI` yorumunun altındaki `<section>` bloğunun `<!--` ve `-->` işaretlerini sil
2. Navbarda `GALERİ LİNKİ` yorumundaki `<a href="#galeri">Galeri</a>` satırını da aç

CSS (`.g-doner`, `.g-usta` … ) ve dosya isimleri olduğu gibi duruyor, onlara dokunulmadı.
Hangi dosya nereye düşüyor → yukarıdaki tablo. Çekim rehberi → bölüm 4b.

---

### 🍽️ Menü fiyatı değiştirmek — ⚠️ ARTIK **İKİ** DOSYADA
Fiyatlar 3 Ağustos 2026'dan beri hem ana sayfada hem QR menü sayfasında geçiyor.
**Birini değiştirip diğerini unutma.**

| Dosya | Nerede | Ne değişecek |
|---|---|---|
| `index.html` | `<section class="section menu" id="menu">` | `<span class="menu-price-tag">140 ₺</span>` (görselin sağ altındaki rozet) |
| `menu.html` | `<section data-panel="durum">` / `"servis"` | `<div class="price">140 <span>₺</span></div>` |
| `baski/masa-menu-a5.html` | ürün satırları | `<div class="fiyat">140<small> ₺</small></div>` — **değişirse yeniden bastırılacak** |
| `baski/masa-karti.html` | kampanya kutusu | `<div class="tutar">450<small> ₺</small></div>` |

- Ürün blokları: `index.html`'de `<article class="menu-item" data-cat="...">`, `menu.html`'de `<article class="item">`.
- Kategoriler (2 tane): **`durum`** / **`servis`**. Sekme `data-cat` değerleri ürünlerdekiyle birebir aynı olmalı.
- `script.js` ana sayfada ilk sekmeyi otomatik seçer. `menu.html`'in kendi küçük scripti var (dosyanın içinde, en altta).
- Tarih notunu iki dosyada da güncelle: `Fiyatlar 2 Ağustos 2026 tarihlidir.`

### 📱 `menu.html` — QR MENÜ SAYFASI (3 Ağu 2026)
Masadaki QR kod buraya bakacak. **Kasıtlı olarak tek dosya**: harici CSS/JS/font yok,
zayıf internette bile anında açılsın diye. Sadece yemek SVG'leri dışarıdan geliyor (~5 KB/adet).
- Yapısı: başlık → yapışkan sekmeler → kampanya kutusu → ürün listesi → altta sabit "Paket Sipariş / Ana Sayfa" çubuğu.
- Ana sayfadan bağlantı: menü bölümünün altındaki **"📱 Telefonda Aç · Sade Menü"** butonu.
- **QR kod için kullanılacak adres: `https://lezzetocakbasi.netlify.app/menu`**
  Netlify "pretty URLs" özelliği `menu.html` linkini canlıda otomatik `/menu`'ye çeviriyor.
  İkisi de 200 dönüyor (3 Ağu 2026'da doğrulandı); QR'a **uzantısız** olanı bas, daha temiz görünür.
- ⚠️ Görsellerde `loading="lazy"` **KULLANMA** — sekmeyle gizlenen paneldeki lazy görseller tarayıcıda hiç yüklenmiyor (3 Ağu 2026'da test edilip görüldü). Dosyalar zaten minicik.
- Kampanya bitince: `<section class="promo">` bloğunu burada da sil (ana sayfadakiyle birlikte).

### 🖨️ BASILI MENÜ — `baski/` klasörü (3 Ağu 2026)

**Amcanın uyarısı:** *"bizim müşteriler QR bilmez, direkt elle bir şey verelim."* Haklı — bu yüzden
asıl menü **basılı**, QR sadece köşede duran bir ikram. Site QR'ı zorlamıyor.

**A4 neden seçilmedi:** A4 masada kocaman durur, tabak/bardak arasında yer bulamaz, ilk yağ
lekesinde çöpe gider ve elden ele dolaşınca kıvrılır. **A5 (yarısı)** tam el boyu, çift taraflı
kullanılınca 11 ürün rahat sığıyor, lamine edilince silinip yıllarca kullanılıyor.

| Dosya | Ne | Kağıt |
|---|---|---|
| `baski/masa-menu-a5.html` | Çift taraflı masa menüsü — ön: Dürüm + kampanya, arka: Porsiyon/Servis + telefon + QR | **A5, çift taraflı, mat lamine** |
| `baski/qr-menu.svg` / `.png` | QR kodu, `https://lezzetocakbasi.netlify.app/menu` adresine bakar | SVG matbaa için, PNG 1800px |

❌ **Masa kartı (dik duran katlanır kart) İPTAL** — kullanıcı istemedi (3 Ağu 2026): *"masa kartı olmasın, direkt masa menüsü olsun."*
`baski/masa-karti.html` silindi. QR zaten A5'in arka yüzünde duruyor, kayıp yok. İleride istenirse
git geçmişinden (`e1aa69c`) geri alınabilir.

### 🚨 BASKIDAN ÖNCE OKU — İÇECEK RİSKİ (3 Ağu 2026)
**Menüde içecek YOK.** Ayran, kola, su, salata, ezme, çorba fiyatları hâlâ bilinmiyor (bkz. bölüm 6).
Lamine baskının geri dönüşü yoktur — içecekler sonradan eklenirse **basılan her nüsha çöp olur.**

Bu yüzden A5'in arkasına şu satır kondu: *"İçecek, salata ve ezme fiyatları için sorunuz."*
Menü eksik görünmüyor, ama kalıcı çözüm değil.

**Karar:** kullanıcı içecek fiyatlarını amcadan öğrenecek. Öğrenilince menüye eklenip
**ondan sonra** tam sayıda bastırılacak. Acilse önce **3-5 adet deneme** bastırılır, gerisi beklenir.

**💰 Tahmini maliyet (3 Ağu 2026 araştırması — kesin değil, teklif alınacak):**

| Yol | Adet | Tahmini birim | Not |
|---|---|---|---|
| Mahalle kırtasiyesi (baskı + lamine) | 10–30 | **~40–80 ₺** | Az adet için mantıklı, hemen alırsın |
| Matbaa (kuşe + mat selefon) | 100 | **~10–20 ₺** | Toplamda ucuz ama 100 adet fazla, fiyat değişince hepsi çöp |

Bir ocakbaşı için **kırtasiye yolu doğru** — az bastır, fiyat değişince yenile.
Kaynak: [100 adet A4 4-renk menü ≈ 800–1.500 ₺](https://altinkayamatbaa.com/blog/restoran-menu-baski-rehberi),
[A5 laminasyon filmi 100'lü ≈ 275–490 ₺](https://www.akakce.com/laminasyon-kagidi/a5-laminasyon-filmi.html) (sadece malzeme, işçilik hariç).

**Kaç adet:** masa sayısı × 1,5 (yukarı yuvarla) + 3 yedek.
Neden 1,5: kalabalık masada tek menü elden ele dolaşıyor, sipariş yavaşlıyor. Yedek: yırtılan/kaybolan için.
**Kullanıcı kararı 3 Ağu 2026: 4-5 adet yeterli** (dükkan masa yoğunluğu düşük, paket ağırlıklı).

### 🛡️ KORUMA YÖNTEMİ — laminasyon mu, şeffaf dosya mı? (3 Ağu 2026 araştırması)

Kullanıcının sorusu: *"kâğıdı şeffaf bir şeyin içine koyuyorlardı, o daha mı ucuz?"*
Gördüğü şey ya **poşet/L dosya** ya da **menü kabı (pleksi/PVC menü kılıfı)**. Karşılaştırma:

| Yöntem | Birim (tahmini) | 5 adet | Artı / Eksi |
|---|---|---|---|
| **Laminasyon** ✅ seçilen | ~20–40 ₺ | ~100–200 ₺ | Tam kapalı, silinir, su/yağ geçmez, sert durur. Değişince yenisi basılır. |
| Poşet / L dosya | ~3–8 ₺ | ~15–40 ₺ | En ucuz **ama üstü açık** → ocakbaşı buharı ve yağ içine giriyor, kâğıt kıvrılıyor, çizilen naylon puslanıyor. Ucuz duruyor. |
| Menü kabı (pleksi/PVC) | ~100–300 ₺ | ~500–1.500 ₺ | Şık ama bu iş için fazla masraflı; 5 menü için mantıksız. |

**Karar: laminasyon.** 5 adette poşet dosyayla arasındaki fark ~150 ₺ — o kadar para için
ocakbaşında yağ çeken, kıvrılan bir menüye razı olunmaz. Lamine olan silinip yıllarca kullanılıyor.

⚠️ Kırtasiyede **A5 laminasyon poşeti bulunmayabilir** — çoğu yerde A4 var. Sorun değil:
A4 poşete koyup lamine ettir, sonra kenarından kestir. **Kenarda 3-5 mm şeffaf pay bırakılsın**,
tam kenardan kesilirse lamine su alır ve açılmaya başlar.

**Tahmini toplam (5 adet):** renkli çift taraflı baskı ~75–150 ₺ + laminasyon ~100–200 ₺ = **~200–350 ₺.**
Kesin değil, Kayseri'de değişir — kırtasiyede önce fiyat sorulacak.
Kaynak (malzeme maliyeti çapası): [A5 laminasyon filmi 100'lü ≈ 275–490 ₺](https://www.akakce.com/laminasyon-kagidi/a5-laminasyon-filmi.html),
[A4 kalın poşet dosya 100'lü ≈ 522 ₺](https://www.akakce.com/poset-dosya.html).

**Baskı adımları:** Chrome'da aç → `Ctrl+P` → kağıt boyutunu seç → kenar boşlukları
**Yok** → **"Arka plan grafikleri" kutusunu İŞARETLE** (bu unutulursa renkler basılmaz, en sık yapılan
hata) → PDF olarak kaydet → matbaaya PDF'i ver.

**Kırtasiyede söylenecek cümle:**
> "Bu PDF'i **A5 boyutunda, çift taraflı, renkli** basar mısınız? Sonra da **A5 laminasyon**
> yapalım, mat olsun. Kağıt **170-200 gram kuşe** olsun, ince kağıt lamine içinde kırışıyor."

Kontrol: baskı elimize gelince **arka yüz ön yüzle aynı hizada mı** bak (çift taraflı baskıda
kayma olur). Kaymışsa bastırma, düzelttir.

⚠️ QR yeniden üretilecekse: `python -m pip install segno`, sonra `segno.make(url, error='h')`.
Hata düzeltme **H (%30)** seçildi — kod yağ/leke/çizik alsa bile okunmaya devam eder, masa menüsünde şart.

### 🎨 YEMEK GÖRSELLERİ — ✅ ARTIK STOK FOTOĞRAF (3 Ağu 2026)

**Canlıdaki durum bu.** 11 ürünün görseli `assets/yemek-*.jpg` — Pexels'ten alınmış telifsiz
fotoğraflar, hepsi tek tip hale getirildi. Seçim listesi ve gerekçeler:
**[`FOTO-ARASTIRMA.md`](FOTO-ARASTIRMA.md)** (hangi ürüne hangi Pexels ID'si konduğu orada).

| Konu | Değer |
|---|---|
| Kaynak / lisans | **Pexels** — ticari kullanım serbest, atıf zorunlu değil |
| Ölçü | **1200×900 (4:3)**, ~90–160 KB, progressive JPEG |
| Ortak arka plan | Kenarlar **`#1c140f`** közüne gömüldü (elips vinyet + kenarda hafif odak kaybı) |
| Ortak ton | Merkez parlaklığı eşitlendi (hedef 132), hafif sıcaklık + kontrast + doygunluk |
| Üretim scriptleri | `tools/foto-indir.py` (Pexels'ten indirir) → `tools/foto-uretim.py` (tek tipe getirir) |

**Tekrar üretmek gerekirse** (ör. bir kare beğenilmedi):
```bash
cd tools && python foto-indir.py && python foto-uretim.py && cp final/*.jpg ../assets/
```
`tools/foto-uretim.py` içindeki **`PICKS`** listesi tek doğruluk kaynağı: her satır
`(dosya adı, Pexels ID, dikey odak 0–1, yakınlaştırma)`. Bir kareyi değiştirmek =
o satırdaki ID'yi değiştirip scripti tekrar çalıştırmak, sonra `final/*.jpg` → `assets/`.
Yedek ID'ler `FOTO-ARASTIRMA.md` tablosunda duruyor.

⚠️ **Neden vinyet:** 11 farklı stok fotoğrafın masası/duvarı/mermeri birbirini tutmuyordu.
Kullanıcının isteği *"arka planlar hepsinde aynı olsun"* idi → kenarlar tek renge gömülüp
ortada sadece yemek bırakıldı. Yeni bir görsel eklenirse **aynı scriptten geçirilmeli**,
yoksa set bozulur.

- `.menu-shot` (index) zaten `aspect-ratio:4/3` → kırpma yok, birebir oturuyor.
  `.item .shot` (menu.html) 122px dar kutu, `object-fit:cover` ile yanlardan kırpıyor — sorun değil,
  yemek ortada. İki kutunun arka plan rengi de `#1a1512`, vinyetle kaynaşıyor.
- **Eski SVG çizimler silinmedi**, `assets/yemek-*.svg` olarak duruyor. Geri dönmek istenirse
  iki dosyada `.jpg"` → `.svg"` yeterli.
- **Gerçek yemek fotoğrafı çekilirse:** aynı isimle (`yemek-tavuk-durum.jpg` vb.) üzerine yaz,
  **HTML'e hiç dokunma.** Çekim rehberi bölüm 4b.
- ⚠️ Bu fotoğraflar **dükkânın kendi yemeği değil.** Menünün altındaki
  *"Görseller temsilidir; sunum değişebilir."* notu bu yüzden var — **silme.**

<details>
<summary>Eski durum (3 Ağu 2026 sabahı, artık geçerli değil) — elle çizilmiş SVG'ler</summary>

Kullanıcının (o günkü) kararı: **stok fotoğraf yok** (dükkanın kendi yemeği değil, müşteriyi yanıltır).
Ürünler internetten araştırılıp her biri için **sıfırdan SVG çizim** yapıldı. Ateş/köz temasına uygun,
koyu zemin + turuncu köz ışığı + tabak/lavaş/közlenmiş domates-biber/sumaklı soğan.

| Dosya (`assets/`) | Ürün |
|---|---|
| `yemek-tavuk-durum.svg` | Tavuk Dürüm |
| `yemek-tavuk-sis-durum.svg` | Tavuk Şiş Dürüm |
| `yemek-kofte-durum.svg` | Köfte Dürüm |
| `yemek-adana-durum.svg` | Adana Dürüm |
| `yemek-kuzu-sis-durum.svg` | Kuzu Şiş Dürüm |
| `yemek-pilav-ustu-doner.svg` | Pilav Üstü Tavuk Döner |
| `yemek-tavuk-sis-servis.svg` | Tavuk Şiş Servis |
| `yemek-kanat-servis.svg` | Kanat Servis |
| `yemek-kofte-servis.svg` | Köfte Servis |
| `yemek-adana-servis.svg` | Adana Servis |
| `yemek-kuzu-sis-servis.svg` | Kuzu Şiş Servis |

- Hepsi `viewBox="0 0 400 300"` (4:3), metin içermez → dile bağlı değil, her boyutta net.
- Her dosyanın gradient id'leri kendine özgü ön ekli (`td…`, `ks…`, `as…`) → ileride sayfaya inline gömülürse çakışmaz.
- **Gerçek fotoğraf geldiğinde:** `index.html`/`menu.html` içindeki `src="assets/yemek-*.svg"` satırını `.jpg`'ye çevirmek yeterli, başka hiçbir şeye dokunma.
- İki sayfada da altta dürüst not var: *"Görseller ürünleri tanıtmak için hazırlanmış çizimlerdir; sunum değişebilir."* **Bu notu silme** — çizimle gerçek sunum farklı olabilir, müşteriye baştan söylüyoruz.

</details>

- Ürün açıklamaları araştırmaya göre yenilendi (Adana'nın zırhla çekilmesi, kanadın közde 20-25 dk pişmesi, köftenin dinlendirilmesi gibi) — **bunlar hâlâ geçerli, fotoğraf değişikliğinden etkilenmedi.** Dükkanın yanında ne verdiğini bilmediğimiz için "yanında şu gelir" iddiası yazılmadı; amcadan öğrenilince eklenebilir.

### 📋 GÜNCEL MENÜ (2 Ağustos 2026 — dükkandaki A4 listeden)

**Dürüm**

| Ürün | Fiyat |
|---|---|
| Tavuk Dürüm | 140 ₺ |
| Tavuk Şiş Dürüm | 150 ₺ |
| Köfte Dürüm | 240 ₺ |
| Adana Dürüm | 240 ₺ |
| Kuzu Şiş Dürüm | 280 ₺ |

**Porsiyon / Servis**

| Ürün | Fiyat |
|---|---|
| Pilav Üstü Tavuk Döner | 200 ₺ |
| Tavuk Şiş Servis | 300 ₺ |
| Kanat Servis | 300 ₺ |
| Köfte Servis | 480 ₺ |
| Adana Servis | 480 ₺ |
| Kuzu Şiş Servis | 550 ₺ |

**Kampanya:** 1 KG Tavuk Kanat + salata + lavaş + ezme = **450 ₺**

❌ **Et Dürüm ve Hatay Usulü Dürüm ARTIK YAPILMIYOR** (kullanıcıdan teyitli, 2 Ağu 2026).
Tabelada hâlâ yazıyorlar ama menüye **eklenmeyecek**. Fotoğraftaki tabelada göründükleri için ileride
"bunlar eksik" diye eklenmesin — bilerek yok.

⚠️ **Fiyatı hâlâ bilinmeyenler (amcaya sorulacak):** ayran / içecek, salata, ezme, çorba ayrı fiyatları.
Listede olmadığı için siteye konmadı — uydurma fiyat yazılmadı.

### 🕐 Saat değiştirmek → 4 yerde geçiyor, HEPSİNİ değiştir
1. `index.html` JSON-LD → `"openingHours": "Mo-Su 11:30-22:00"` (satır ~43)
2. Hero istatistik → `<b data-count="22">` (satır ~89)
3. Hakkında metni + `<li>🕙 Her gün 22:00'ye kadar</li>` (satır ~102, ~106)
4. İletişim → "Çalışma Saatleri · Her gün 11:30 – 22:00" (satır ~269)

Kontrol komutu: `grep -n "11:30\|22:00" index.html` → 4 satır dönmeli.

---

## 4c. 🌐 SİTE ADRESİ PLANI — NETLIFY

**Sorun:** `ismetguler.github.io/lezzet-ocakbasi` işletme adresi olamaz — kartvizite, tabelaya, Google profiline yazılmaz.

### ✅ KARAR (23 Tem 2026): ÜCRETSİZ → `lezzetocakbasi.netlify.app`
Kullanıcı kararı: para verilmeyecek, uğraş olmayacak, adreste sadece işletme adı görünsün yeter.

**Erişim testi (23 Tem 2026, kullanıcının TR bağlantısından, tarayıcıyla):**

| Alan adı | Sonuç |
|---|---|
| `github.io` | ✅ açılıyor |
| `netlify.app` | ✅ açılıyor |
| `vercel.app` | ✅ açılıyor |
| `pages.dev` | ❌ **ENGELLİ** — bağlantı reddedildi. **KULLANMA.** |

**Neden Netlify, github.io taşıma değil:** GitHub yolu yeni hesap + e-posta doğrulama + repo transferi + collaborator ayarı istiyordu (6 adım, 2 hesap). Netlify **mevcut GitHub hesabıyla giriş** kabul ediyor → yeni hesap yok. Push akışı da aynı kalıyor: `git push` → Netlify otomatik yayınlıyor.

**Kurulum adımları:**

| # | Adım | Kim yapar |
|---|---|---|
| 1 | netlify.com → **"Log in with GitHub"** (mevcut `ismetguler` hesabı, yeni hesap AÇMA) | **Kullanıcı** |
| 2 | Add new site → **Import an existing project** → GitHub → `lezzet-ocakbasi` reposunu seç | Kullanıcı |
| 3 | Build ayarları **BOŞ BIRAK** (build command yok, publish directory boş/kök). Site saf HTML, derleme yok. → Deploy | Kullanıcı |
| 4 | Site settings → **Change site name** → `lezzetocakbasi` yaz | Kullanıcı |
| 5 | Adresi kontrol et: `https://lezzetocakbasi.netlify.app` | Kullanıcı |
| 6 | `index.html` içindeki OG / canonical / JSON-LD adreslerini yeni adrese çevir | **Geliştirici** |
| 7 | Google işletme profiline site adresi olarak bunu yaz | Kullanıcı |

⚠️ Adım 4'te isim doluysa `lezzetocakbasitalas` dene.
⚠️ GitHub Pages KAPATILMIYOR — `ismetguler.github.io/lezzet-ocakbasi` yedek olarak arka planda kalsın, zararı yok.
- İş akışı değişmiyor: dosya düzenle → `git push` → Netlify 1-2 dk'da yayınlar.
- Netlify ücretsiz plan: 100 GB/ay trafik. Bir ocakbaşı sitesi için pratikte sınırsız.

### 💰 İLERİDE İSTENİRSE (ücretli, ERTELENDİ): `lezzetocakbasi.com`
- 23 Tem 2026 itibarıyla RDAP'ta kayıtlı değil → **boşta.** (Sonra bakılırsa tekrar kontrol et, kapılmış olabilir.)
- Yılda ~300–600 TL, sadece alan adı — hosting yine bedava kalır (Netlify'da durur).
- Nereden: Natro / İsimtescil / Turhost / Namecheap. Yenileme fiyatına bak, ilk yıl indirimlidir.
- ⚠️ `.com.tr` ALMA — vergi levhası/marka belgesi ister. Düz `.com` yeterli.
- **Kullanıcının asıl çekincesi:** yenilemeyi unutup adresi kaptırmak. Ücretsiz adreste bu risk yok, o yüzden ertelendi.
- Alınırsa: Netlify → Domain management → Add custom domain → Netlify'ın verdiği DNS kayıtlarını alan adı paneline gir. Ücretsiz SSL otomatik gelir. Yani bugünkü kurulum boşa gitmiyor.

---

## 5. YAPILDI ✅

- [x] index.html iskeleti + tüm bölümler
- [x] styles.css — tema, animasyonlar, responsive
- [x] script.js — scroll reveal, mobil menü, sayaçlar, köz partikülleri, menü sekme filtresi
- [x] SEO / Open Graph / JSON-LD (Restaurant schema)
- [x] Mobil test (375×812) — yatay taşma yok, hamburger menü çalışıyor
- [x] GitHub Pages'te yayına alındı — v1 CANLI
- [x] **Google işletme profilinde saatler düzeltildi (amcanın bilgisayarından)** — 23 Tem 2026
- [x] **Sitedeki saatler 11:00–03:00 → 11:30–22:00 olarak güncellendi (4 yer + JSON-LD)** — 23 Tem 2026
- [x] **Açılış saati amcadan teyit alındı: 11:30, her gün** — 23 Tem 2026
- [x] **Galeri foto slotları hazırlandı** — assets/'e dosya atınca otomatik devreye giriyor — 23 Tem 2026
- [x] **NETLIFY'A GEÇİLDİ — asıl adres artık `lezzetocakbasi.netlify.app`** (ücretsiz, HTTPS otomatik, TR'den erişim doğrulandı) — 23 Tem 2026
- [x] **Adres etiketleri güncellendi** — canonical + og:url + JSON-LD `url` yeni adrese çevrildi — 23 Tem 2026
- [x] **GERÇEK MENÜ + FİYATLAR GİRİLDİ** — 11 ürün, 2 sekme (Dürüm / Porsiyon-Servis) — 2 Ağu 2026
- [x] **KAMPANYA BÖLÜMÜ AÇILDI** — hero'nun hemen altında, afiş fotoğrafı + 450 ₺ + paket sipariş butonu — 2 Ağu 2026
- [x] **Dış cephe fotoğrafı geldi** — hero arka planında canlı, `og:image` etiketi açıldı (WhatsApp'ta link atınca artık görsel çıkıyor) — 2 Ağu 2026
- [x] **Amcanın Google hesabının şifresi değiştirildi** (dükkanda birlikte yapıldı) — 2 Ağu 2026
- [x] **11 ürün için elle çizilmiş SVG yemek görseli yapıldı** — ana sayfadaki menü görselli karta dönüştü — 3 Ağu 2026
- [x] **Ürün açıklamaları araştırmaya göre yenilendi** (Adana/zırh, kanat/köz süresi, köfte/dinlendirme vb.) — 3 Ağu 2026
- [x] **`menu.html` QR menü sayfası yapıldı** — tek dosya, telefon öncelikli, altta sabit sipariş çubuğu — 3 Ağu 2026
- [x] **SVG çizimler → telifsiz stok FOTOĞRAF** (Pexels, 11 ürün), hepsi aynı koyu köz arka planına oturtuldu — 3 Ağu 2026

## 6. SIRADA / BEKLEYEN ⏳

> 🏪 **Dükkan ziyareti görev listesi ayrı dosyada: [`DUKKAN-GOREV.md`](DUKKAN-GOREV.md)** — telefondan açılıp sırayla işaretlenecek.

### 🚨 EN ACİL: Google hesabı — YARIM KALDI (2 Ağu 2026)
Şifre dükkanda **değiştirildi ✅**, ama işlem tamamlanmadı:
**Amcanın telefonuna Google'dan bir bildirim gitti; "4" rakamına dokunup onaylaması gerekiyor.**
Amca bunu tek başına yapamıyor → **onun yanına gidip birlikte yapılacak, ilk iş bu.**
Onaylanmazsa doğrulama yarım kalır ve hesap yine riskte olur.
⚠️ Dükkandaki PC'de **çıkış yapma, çerez temizleme yok.**
⚠️ Yeni şifre `assets/` klasörüne, repoya, hiçbir proje dosyasına YAZILMAZ (bkz. bölüm 4 baştaki uyarı).

### 🎯 ANA HEDEF: QR MENÜ
Menü tek sayfa (telefonda güzel açılan) → QR kod üret → masalara koy.
**Satış argümanı (amcaya anlatılacak):** fiyat değişince QR yeniden basılmıyor, sadece site güncelleniyor. Basılı menü masrafı ve derdi bitiyor.


- [ ] **Gerçek fotoğraflar** — kullanıcı çekecek → `assets/` (çekim rehberi: bölüm 4b)
      **Galeri 9 slota çıkarıldı** (kullanıcı usta + mangal + dış masa da çekecek).
      Öncelik: `dis-cephe.jpg` (akşam) → `usta.jpg` → `doner.jpg` → `mangal.jpg` → `dis-masa.jpg` → `sofra.jpg` → `ocak.jpg` → `kebap.jpg` → `salon.jpg` → `lavas.jpg`
- [ ] **Eksik fiyatlar amcaya sorulacak** — Et Dürüm, Hatay Usulü Dürüm (ikisi de tabelada yazıyor ama A4 listede yok), ayran/içecek, salata, ezme, çorba
- [x] ~~**Menü ayrı tek sayfa yapılacak** (`menu.html`)~~ ✅ **YAPILDI 3 Ağu 2026**
- [x] ~~**QR kod üretilecek**~~ ✅ **YAPILDI 3 Ağu 2026** — `baski/qr-menu.svg` + `.png`, `/menu` adresine bakıyor
- [ ] **🚨 ÖNCE: İÇECEK / SALATA / EZME / ÇORBA FİYATLARI** — kullanıcı amcadan öğrenecek.
      **Baskının önündeki tek engel bu.** Gelince menüye eklenecek (4 dosya: index, menu.html, A5, PROGRESS).
- [ ] **🎯 SONRA: A5 masa menüsü bastırılacak** — `baski/masa-menu-a5.html` → PDF → kırtasiye.
      **4-5 adet, A5 çift taraflı renkli, mat laminasyon.** Tahmini ~200–350 ₺. (Bkz. bölüm 4g.)
- [ ] ⏸️ **RAFA KALDIRILDI: tezgah üstü / duvar panosu** (A3–A2) — kullanıcı kararı 3 Ağu 2026:
      *"içecekler orada yazmıyor, onları da öğrenince yaparız."* İçecek fiyatları gelince tekrar gündeme gelecek.
      Gerekçe duruyor: dönerci trafiğinin çoğu tezgahta, masaya oturmayan müşteri A5'i hiç görmüyor.
- [ ] **Fotoğraf düzenleme** — kırpma, boyut, ışık/renk, üzerine yazı ekleme (geliştirici yapacak, kullanıcı ham çekecek)
- [ ] **WhatsApp sipariş butonu** — numara varsa
- [ ] **Hakkında bölümü gerçek bilgilerle** — kuruluş yılı, ustanın hikâyesi, et tedariki
- [ ] **Google profili düzeltmeleri** — site adresi, kategori, hizmetler, ödeme yöntemleri (DUKKAN-GOREV.md A4)
- [ ] Google işletme profiline iyi fotoğraflar + site adresi eklemek
- [ ] (ops.) WhatsApp sipariş butonu
- [ ] (ops.) Gerçek Google yorumlarını isim/tarihle güncellemek

---

## 7. ÖNEMLİ NOTLAR / TUZAKLAR

- **Ekran görüntüsü aracı timeout veriyor:** köz/alev animasyonları sürekli döndüğü için tarayıcı sabit kare yakalayamıyor. **SİTE HATASI DEĞİL.** Gerçek kullanıcıda sorun yok.
- **"Telefonda farklı görünüyor":** kasıtlı responsive tasarım, hata değil.
- Yorum bölümündeki metinler Google yorumlarından derleme; birebir alıntı değil.
- Kullanıcının isteği: **demo değil, gerçek yayın.** Animasyonlar "şekilli şukullu" olsun.

---

## 8. OTURUM GÜNLÜĞÜ

| Tarih | Ne yapıldı |
|---|---|
| 2026-07-11 | Site sıfırdan yazıldı, test edildi, GitHub Pages'te yayına alındı (v1 canlı) |
| 2026-07-23 | Bu dosya proje hafızasına dönüştürüldü; saatler 11:30–22:00 olarak düzeltildi (ikisi de teyitli); galeri foto slotları fallback'li hale getirildi → **push edildi, canlıda** (`b500e35`) |
| 2026-07-23 | Hero'ya `dis-cephe.jpg` foto slotu açıldı (koyu okunurluk katmanıyla); foto çekim rehberi (4b) ve alan adı planı (4c) yazıldı |
| 2026-07-23 | Adres kararı: **ücretsiz yol**, `.com` ertelendi. TR erişim testi yapıldı (pages.dev engelli, netlify/vercel/github.io açık) → **Netlify seçildi** (yeni hesap gerektirmediği için) |
| 2026-07-23 | Yeni yol haritası: menü çıkarma → tek sayfa menü → **QR kod** → masalara. Fotoğraf düzenleme (yazı ekleme dahil) geliştiriciye devredildi. Google hesabı şifresizlik riski tespit edildi → `DUKKAN-GOREV.md` yazıldı |
| 2026-07-23 | Galeri 6 → **9 slot** (3×3) yapıldı: usta, mangal, dış masa kareleri eklendi. Yatay/dikey kuralı ve yeni çekim notları 4b'ye yazıldı |
| 2026-08-02 | 🚨 Amcanın **şifre defteri fotoğrafı** yanlışlıkla `assets/`e atılmış, push edilmeden çıkarıldı → bölüm 4'e kalıcı uyarı yazıldı |
| 2026-08-02 | ✅ **Gerçek menü + fiyatlar girildi** (dükkandaki A4 listeden okundu). Sekmeler `doner/kebap/baslangic/icecek` → `durum/servis` oldu; `script.js` artık ilk sekmeyi otomatik seçiyor |
| 2026-08-02 | ✅ **Kampanya bölümü açıldı** (hero'nun altı, id=`kampanya`): afiş fotoğrafı + "1 KG Tavuk Kanat" + salata/lavaş/ezme + 450 ₺ + paket sipariş butonu. Navbara "🔥 Kampanya" linki eklendi. Nasıl düzenlenir → bölüm 4d |
| 2026-08-02 | ✅ **Dış cephe fotoğrafı hero'ya kondu**, `og:image` açıldı. Yerel test: menü sekmeleri, kampanya kartı, mobil 375px — taşma yok, hata yok |
| 2026-08-02 | ✅ **Galeri bölümü geçici kapatıldı** (fotoğraf yok, boş gradyan duruyordu) — yorum satırına alındı, açma talimatı bölüm 4f |
| 2026-08-02 | ✅ **Dış cephe fotoğrafından insanlar silindi** (kullanıcı isteği): ham çekim #2 temel alındı, alttan kırpıldı, kalan 3 kişi inpaint'lendi, ışık düzeltildi. Hamlar `_ham-*` olarak saklandı. Detay bölüm 4 |
| 2026-08-03 | 🔧 **Masa kartı iptal edildi** (kullanıcı: "direkt masa menüsü olsun"), **duvar panosu rafa kaldırıldı** (içecekler bilinmiyor). A5'in arkasına *"İçecek, salata ve ezme fiyatları için sorunuz"* satırı eklendi. Baskı fiyat araştırması ve kırtasiyede söylenecek cümle bölüm 4g'ye yazıldı. **Baskı, içecek fiyatları gelene kadar bekliyor** |
| 2026-08-03 | ✅ **QR kod üretildi** (`baski/qr-menu.svg`/`.png`, hata düzeltme H) + **basılı menü yapıldı**: `baski/masa-menu-a5.html` (A5 çift taraflı) ve `baski/masa-karti.html` (masada dik duran katlanır kart). Amcanın "müşterimiz QR bilmez" uyarısı üzerine kurgu değişti: **asıl menü basılı, QR köşede duran ikram.** A4 yerine A5 seçildi (gerekçe: bölüm 4g). Tarayıcıda ölçüldü: A5 iki yüz de 210mm'e tam oturuyor, kart iki yüzü 148,5mm, taşma yok |
| 2026-08-03 | 🚨 **`assets/` klasörünün hiç repoda olmadığı fark edildi** (`?? assets/`). Yani `dis-cephe.jpg` ve `kampanya-afis.jpg` 2 Ağu'da "canlıya alındı" yazılmasına rağmen **push edilmemiş, canlıda hiç görünmemiş.** Bu commit'le eklendi, canlıda doğrulandı. Ayrıca `.gitignore` yazıldı: `assets/_*` (ham çekimler + A4 fiyat listesi fotoğrafı) artık repoya giremiyor |
| 2026-08-03 | ✅ **YAYINLANDI** (`8802390`). Canlı doğrulama: `/menu` 200, 11/11 görsel yükleniyor, ana sayfada hero fotoğrafı ve kampanya afişi ilk kez gerçekten görünüyor, 375px'te taşma yok |
| 2026-08-03 | ✅ **11 ürün tek tek araştırıldı ve her biri için elle SVG çizim yapıldı** (`assets/yemek-*.svg`). Kullanıcı kararı: stok fotoğraf yok, gerçek fotoğraf beklenmiyor, çizim. Ana sayfadaki menü görselli 3'lü karta çevrildi (fiyat görselin üstünde rozet), açıklamalar araştırmaya göre yeniden yazıldı. **`menu.html` QR menü sayfası yapıldı.** Tarayıcıda test: 11/11 görsel yükleniyor, sekmeler çalışıyor, 375px'te taşma yok, konsol temiz. ⚠️ Fiyatlar artık İKİ dosyada — bkz. bölüm 4e |
| 2026-08-03 | 🖼️ **KARAR DEĞİŞTİ: SVG çizimler → stok fotoğraf.** Kullanıcı çizimleri *"çocuksu, kötü duruyor"* buldu. Pexels'ten (telifsiz, ticari serbest) 41 aday indirildi, kontakt sayfası yapılıp **gözle elendi**, 11 kare seçildi. Kullanıcı isteği *"arka planlar hepsinde aynı olsun"* → 1200×900 4:3 kırpma + merkez parlaklığı eşitleme + kenarların `#1c140f` közüne gömülmesi (`_foto-uretim.py`). İki HTML'de `.svg`→`.jpg` (11+11), alt not *"çizimlerdir"* → *"temsilidir"* oldu. SVG'ler silinmedi. Test: 12/12 görsel yükleniyor, konsol temiz, 375px'te taşma yok, `.menu-shot` 4:3 birebir oturuyor |
| 2026-07-23 | ✅ **Netlify kurulumu tamamlandı — https://lezzetocakbasi.netlify.app CANLI.** HTTPS, saatler, tüm bölümler, telefon linki tarayıcıyla doğrulandı. Adres etiketleri yeni adrese çevrildi. Sıradaki: fotoğraflar |
