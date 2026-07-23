# 🔥 LEZZET OCAKBAŞI — PROJE HAFIZASI

> **Bu dosya projenin tek hafızası.** Sohbet kapansa, token bitse, aylar sonra dönülse
> buradan devam edilir. **Her değişiklikte bu dosya güncellenir.**
> Son güncelleme: **2026-07-23**

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
├── styles.css      → tema, animasyonlar, responsive, FOTO SLOTLARI
├── script.js       → scroll reveal, mobil menü, sayaçlar, köz partikülleri, menü sekmeleri
├── assets/         → fotoğraflar buraya (şu an BOŞ)
└── PROGRESS.md     → bu dosya
```

- Saf HTML + CSS + JS. Framework yok, build yok → her yerde barınır, çok hızlı.
- Tema: **ateş/köz (ember)** — koyu antrasit zemin + turuncu/kırmızı sıcak tonlar.
- Tek sayfa: Hero → Hakkında → Menü → Galeri → Yorumlar → İletişim/Harita → Footer.
- Mobil öncelikli responsive (375px'te test edildi, taşma yok).

---

## 4. NASIL DÜZENLENİR (kritik bilgi — burayı oku)

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

### 🍽️ Menü fiyatı girmek
`index.html` içinde `MENU-PLACEHOLDER` yorumunu ara.
Her ürün: `<article class="menu-item" data-cat="...">`
Kategoriler: `doner` / `kebap` / `baslangic` / `icecek`
Fiyat için `<span class="price">—</span>` içindeki tireyi sil, fiyatı yaz.

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
| 6 | `index.html` içindeki OG / canonical / JSON-LD adreslerini yeni adrese çevir | **Claude** |
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

## 6. SIRADA / BEKLEYEN ⏳

- [ ] **Gerçek fotoğraflar** — kullanıcı çekecek → `assets/` (çekim rehberi: bölüm 4b)
      **Galeri 9 slota çıkarıldı** (kullanıcı usta + mangal + dış masa da çekecek).
      Öncelik: `dis-cephe.jpg` (akşam) → `usta.jpg` → `doner.jpg` → `mangal.jpg` → `dis-masa.jpg` → `sofra.jpg` → `ocak.jpg` → `kebap.jpg` → `salon.jpg` → `lavas.jpg`
- [ ] **`og:image` etiketini aç** — `dis-cephe.jpg` eklenince `index.html` head'indeki yorumlu 2 satırın işaretini kaldır (WhatsApp'ta link önizlemesinde büyük görsel çıkar)
- [ ] **Menü + fiyatlar** — amcadan gelince doldurulacak
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
| 2026-07-23 | Galeri 6 → **9 slot** (3×3) yapıldı: usta, mangal, dış masa kareleri eklendi. Yatay/dikey kuralı ve yeni çekim notları 4b'ye yazıldı |
| 2026-07-23 | ✅ **Netlify kurulumu tamamlandı — https://lezzetocakbasi.netlify.app CANLI.** HTTPS, saatler, tüm bölümler, telefon linki tarayıcıyla doğrulandı. Adres etiketleri yeni adrese çevrildi. Sıradaki: fotoğraflar |
