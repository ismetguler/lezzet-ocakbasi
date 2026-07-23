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
| `assets/doner.jpg` | Galeri — "Közde Döner" |
| `assets/kebap.jpg` | Galeri — "Mangal Kebap" |
| `assets/salon.jpg` | Galeri — "Salonumuz" |
| `assets/lavas.jpg` | Galeri — "Lavaş & Garnitür" |
| `assets/ocak.jpg` | Galeri — "Ocakbaşı" |
| `assets/sofra.jpg` | Galeri — "Sofra Keyfi" |

CSS `url(...) , linear-gradient(...)` şeklinde yazıldı: **dosya varsa foto görünür, yoksa eski gradyan görünür.** Kırık resim ikonu çıkmaz.
Fotoğraf önerisi: yatay (4:3), en az 1200px genişlik, ~300KB altı, iyi ışık.

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

- [ ] **Gerçek fotoğraflar** — kullanıcı çekecek/toplayacak → `assets/` (bkz. bölüm 4)
- [ ] **Menü + fiyatlar** — amcadan gelince doldurulacak
- [ ] Google işletme profiline iyi fotoğraflar + menü linki (site adresi) eklemek
- [ ] (ops.) Özel alan adı
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
| 2026-07-23 | Bu dosya proje hafızasına dönüştürüldü; saatler 11:30–22:00 olarak düzeltildi (ikisi de teyitli); galeri foto slotları fallback'li hale getirildi. **Henüz push edilmedi.** |
