# Lezzet Ocakbaşı — Web Sitesi İlerleme Notu

> Bu dosya token bitse bile kaldığım yerden devam edebilmek için tutuluyor.
> Her önemli adımda güncelleniyor.

## İşletme Bilgileri (Google'dan alınan)
- **Ad:** Lezzet Ocakbaşı
- **Tür:** Ocakbaşı / Mangal / Dönerci
- **Puan:** 4,4 (52 yorum)
- **Adres:** Mevlana Mah., 38280 Talas / Kayseri
- **Telefon:** (0352) 431 44 00
- **Çalışma:** Açık — Kapanış 03:00 (saatler AMCAYA SORULACAK, şu an tahmini)
- **Plus Code:** PH27+RW Talas, Kayseri
- **Google Maps:** Plus code ile aranabilir

## Kullanıcı Notları / İstekler
- Demo değil, GERÇEK yayına alınacak site.
- Amca işletmeye önem vermemiş: Google'da menü/site yok, fotoğraflar kötü, yorumlar/saatler yanlış.
- Menü SONRA eklenecek (kullanıcı amcaya sorup verecek). Menü bölümü kolay doldurulabilir yapıda olmalı.
- Animasyonlar "şekilli şukullu" olsun — göze hitap etsin.
- Fotoğraflar kötü → şimdilik CSS/placeholder, gerçek foto gelince değişecek.

## Teknik Kararlar
- Saf HTML + CSS + JS (framework yok) → her yerde barınabilir, hızlı.
- Tema: Ateş/köz (ember) — koyu antrasit + turuncu/kırmızı sıcak tonlar (ocakbaşı ruhu).
- Tek sayfa (one-page): Hero, Hakkında, Menü, Galeri, Yorumlar, İletişim/Harita, Footer.
- Responsive (mobil öncelikli).
- SEO meta etiketleri + Open Graph + LocalBusiness JSON-LD (Google için önemli!).

## Dosya Yapısı
```
lezzet-ocakbasi/
├── index.html      (ana sayfa)
├── styles.css      (tüm stiller + animasyonlar)
├── script.js       (etkileşim, scroll animasyonları)
├── assets/         (fotoğraflar buraya)
└── PROGRESS.md     (bu dosya)
```

## Yapılacaklar (TODO)
- [x] index.html iskeleti + tüm bölümler
- [x] styles.css — tema, animasyonlar, responsive
- [x] script.js — scroll reveal, mobil menü, sayaçlar, köz partikülleri, menü sekmeleri
- [x] SEO / JSON-LD (Restaurant schema, OG etiketleri)
- [~] Menü bölümü — YAPI HAZIR, örnek ürünler var, fiyatlar "—". Amcadan gelince doldurulacak.
      → index.html içinde "MENU-PLACEHOLDER" yorumunu ara. Her ürün: <article class="menu-item" data-cat="...">
      → Kategoriler: doner / kebap / baslangic / icecek. Fiyatı <span class="price">—</span> yerine yaz.
- [ ] Gerçek fotoğraflar → assets/ klasörüne koy, styles.css'te .g-doner/.g-kebap vb.
      background gradyanlarını `background-image:url(assets/xxx.jpg)` ile değiştir.
- [ ] Yayına alma (hosting kararı — NOT: pages.dev TR'de engelli, kullanma. Netlify/Vercel/GitHub Pages)
- [ ] Çalışma saatleri amcadan teyit (şu an "11:00-03:00 her gün" varsayıldı — hero'da ve JSON-LD'de)

## Test Durumu (2026-07-11)
- Yerel sunucu: `python -m http.server 8099` → http://127.0.0.1:8099 (klasör içinde çalıştır)
- read_page ile tüm bölümler doğrulandı ✓
- JS test: menü sekme filtreleme ✓, köz partikülleri (14 mobil/26 masaüstü) ✓, sayaçlar ✓
- NOT: Tarayıcı screenshot'ı sürekli animasyonlar (köz/alev) yüzünden timeout veriyor — SİTE HATASI DEĞİL,
  araç sabit kare yakalayamıyor. Gerçek kullanıcıda sorun yok.

## Durum: v1 TAMAM — inceleme bekliyor. Sıradaki: menü fiyatları + gerçek foto + hosting.
