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

- **CANLI SİTE:** https://ismetguler.github.io/lezzet-ocakbasi/
- **GitHub repo:** https://github.com/ismetguler/lezzet-ocakbasi (public, hesap: `ismetguler`)
- **Yerel klasör:** `C:\Users\ismet\Desktop\newjob\lezzet-ocakbasi\`
- Pages kaynağı: `main` branch, kök (`/`). HTTPS zorunlu.
- Git kimliği: `ismetguler` / `gulerrismet@gmail.com`
- ⚠️ **pages.dev KULLANMA** — Türkiye'de engelli. github.io kullanıyoruz.
- İleride `lezzetocakbasi.com` gibi alan adı alınırsa Pages'e `CNAME` dosyası eklenir.

### Değişiklik yayınlama (ezber komut)
```bash
cd "C:/Users/ismet/Desktop/newjob/lezzet-ocakbasi" && git add . && git commit -m "guncelleme" && git push
```
Push'tan 1–2 dakika sonra canlı site yenilenir. Tarayıcıda görmüyorsan **Ctrl+F5** (sert yenileme).

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

| Dosya adı | Nereye düşer |
|---|---|
| `assets/dis-cephe.jpg` | **HERO — sayfanın en üstü, en önemli foto** (akşam dış cephe) |
| `assets/doner.jpg` | Galeri — "Közde Döner" |
| `assets/kebap.jpg` | Galeri — "Mangal Kebap" |
| `assets/salon.jpg` | Galeri — "Salonumuz" |
| `assets/lavas.jpg` | Galeri — "Lavaş & Garnitür" |
| `assets/ocak.jpg` | Galeri — "Ocakbaşı" |
| `assets/sofra.jpg` | Galeri — "Sofra Keyfi" |

CSS `url(...) , linear-gradient(...)` şeklinde yazıldı: **dosya varsa foto görünür, yoksa eski gradyan görünür.** Kırık resim ikonu çıkmaz.
Hero'da fotoğrafın üstünde koyu katman var → hangi foto konursa konsun yazılar okunur kalır.

---

## 4b. 📷 FOTOĞRAF ÇEKİM REHBERİ (telefonla, profesyonel görünsün)

### Telefon ayarları — bir kere yap, hep açık kalsın
- **Yatay tut** (telefonu yan çevir). Site yatay foto istiyor, dikey çekersen kenarları kesilir.
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

### 🪑 SALON (`salon.jpg`)
- **Müşteri gelmeden önce, mekân tertemiz ve boşken.** Sandalyeler hizalı, masalar açık.
- Köşeden çek — köşeden çekilen mekân daha geniş görünür.
- Tüm ışıklar açık, gündüz ise perdeler açık.

### Sonrası
- Fotoğrafları bilgisayara at → `lezzet-ocakbasi/assets/` klasörüne **tam bu isimlerle** kaydet.
- Boyutlandırma/sıkıştırma gerekirse ben hallederim, sen ham halini koy yeter.
- Emin olamadığın kareler olursa hepsini at, birlikte seçeriz.

---

## 4c. 🌐 ALAN ADI (domain) PLANI

**Sorun:** `ismetguler.github.io/lezzet-ocakbasi` adresi işletme için uygun değil — kartvizite, tabelaya, Google profiline yazılmaz.

**Çözüm: `lezzetocakbasi.com` alınacak.**
- 23 Tem 2026 itibarıyla RDAP kaydında görünmüyor → **boşta.**
- Maliyet: yılda yaklaşık 300–600 TL (sadece alan adı). **Hosting yine bedava kalıyor** — GitHub Pages'te durmaya devam eder.
- Nereden: Türkiye'den Natro / İsimtescil / Turhost, yurtdışından Namecheap. (İlk yıl indirimli, 2. yıl tam fiyat — yenileme fiyatına bak.)
- ⚠️ `.com.tr` ALMA — vergi levhası/marka belgesi ister, uğraştırır. Düz `.com` yeterli ve daha tanıdık.

**Bağlama adımları (alan adı alındıktan sonra):**
1. Alan adı panelinde DNS'e 4 adet **A kaydı** ekle (`@` için):
   `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
2. Bir de **CNAME kaydı**: `www` → `ismetguler.github.io`
3. Repo köküne `CNAME` adında dosya (uzantısız), içine tek satır: `lezzetocakbasi.com` → commit + push
4. GitHub → repo → Settings → Pages → Custom domain'e `lezzetocakbasi.com` yaz → Save
5. DNS yayılınca (birkaç saat) **"Enforce HTTPS"** kutusunu işaretle
6. Sonra: Google işletme profiline site adresi olarak bunu ekle + `index.html` içindeki JSON-LD/OG etiketlerindeki adresleri güncelle

**Ücretsiz ara çözüm (alan adı alınmayacaksa):** GitHub'da `lezzetocakbasi` adında yeni bir hesap açılıp repo oraya taşınırsa adres `lezzetocakbasi.github.io` olur. Bedava ama `.com` kadar ciddi durmaz.

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

## 6. SIRADA / BEKLEYEN ⏳

- [ ] **Gerçek fotoğraflar** — kullanıcı çekecek → `assets/` (çekim rehberi: bölüm 4b)
      Öncelik sırası: `dis-cephe.jpg` (akşam) → `ocak.jpg` → `doner.jpg` → `sofra.jpg` → `salon.jpg` → `kebap.jpg` → `lavas.jpg`
- [ ] **`lezzetocakbasi.com` alan adı** — boşta görünüyor, alınıp bağlanacak (adımlar: bölüm 4c)
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
