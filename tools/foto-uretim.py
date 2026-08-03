"""11 stok fotoyu tek tip hale getirir.

Hedef: her karede AYNI arka plan. Farklı stok fotoğrafların masası/duvarı/mermeri
birbirini tutmuyor; o yüzden kenarlar tek bir koyu renge (#1c140f) tamamen
gömülüyor ve ortada sadece yemek kalıyor. Sonuç: 11 kare aynı setten çıkmış gibi.
"""
import os, glob
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = BASE + "/final"
os.makedirs(OUT, exist_ok=True)

W, H = 1200, 900
BG = np.array([28.0, 20.0, 15.0])       # ortak arka plan — site temasının közü
WARM = np.array([1.035, 1.0, 0.945])    # hafif sıcaklık (abartısız)
TARGET_LUM = 132.0                       # merkezdeki yemeğin ortak parlaklığı

# slot -> (pexels id, dikey odak, yakınlaştırma)
PICKS = [
    ("yemek-tavuk-durum",      6416559,  0.50, 1.02),
    ("yemek-tavuk-sis-durum",  9980749,  0.50, 1.05),
    ("yemek-kofte-durum",      36750272, 0.50, 1.05),
    ("yemek-adana-durum",      11286814, 0.50, 1.00),
    ("yemek-kuzu-sis-durum",   15390220, 0.42, 1.05),
    ("yemek-pilav-ustu-doner", 18062062, 0.62, 1.15),
    ("yemek-tavuk-sis-servis", 5643427,  0.50, 1.05),
    ("yemek-kanat-servis",     31587878, 0.50, 1.05),
    ("yemek-kofte-servis",     37206707, 0.50, 1.00),
    ("yemek-adana-servis",     7439809,  0.50, 1.08),
    ("yemek-kuzu-sis-servis",  37206698, 0.50, 1.05),
]


def find_src(pid):
    hits = glob.glob(f"{BASE}/cand/*__{pid}.jpg") + glob.glob(f"{BASE}/cand2/*__{pid}.jpg")
    if not hits:
        raise FileNotFoundError(pid)
    return hits[0]


def crop_43(im, focus, zoom):
    r = max(W / im.width, H / im.height) * zoom
    im = im.resize((max(W, int(im.width * r)), max(H, int(im.height * r))), Image.LANCZOS)
    left = (im.width - W) // 2
    top = int((im.height - H) * focus)
    return im.crop((left, top, left + W, top + H))


def grade(im):
    """Sadece parlaklık eşitleme + hafif sıcaklık. Renkleri soldurmuyoruz — yemek iştah açsın."""
    a = np.asarray(im, dtype=np.float32)

    # parlaklık ölçümü MERKEZDEN (kenarlar zaten karartılacak, ortalamayı bozmasın)
    c = a[H // 4:3 * H // 4, W // 4:3 * W // 4]
    lum = float((c @ np.array([0.299, 0.587, 0.114], dtype=np.float32)).mean())
    scale = float(np.clip(TARGET_LUM / max(lum, 1e-3), 0.82, 1.30))

    a = np.clip(a * scale * WARM, 0, 255)
    im = Image.fromarray(a.astype(np.uint8))

    im = ImageEnhance.Contrast(im).enhance(1.10)
    im = ImageEnhance.Color(im).enhance(1.14)
    im = ImageEnhance.Sharpness(im).enhance(1.15)
    return im


def unify_bg(im):
    """Kenarları tamamen ortak arka plan rengine gömer — 11 karede birebir aynı çerçeve."""
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    # elips mesafesi: 0 = merkez, 1 = kenar ortası
    d = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)

    m = np.clip((d - 0.52) / 0.42, 0, 1) ** 1.25   # 0.94'ten sonra tam arka plan
    m = np.asarray(Image.fromarray((m * 255).astype(np.uint8)).filter(
        ImageFilter.GaussianBlur(40)), dtype=np.float32) / 255.0
    m3 = m[..., None]

    a = np.asarray(im, dtype=np.float32)
    # kenara doğru hafif odak kaybı — geçiş daha doğal dursun
    blur = np.asarray(im.filter(ImageFilter.GaussianBlur(6)), dtype=np.float32)
    a = a * (1 - m3 * 0.7) + blur * (m3 * 0.7)
    a = a * (1 - m3) + BG * m3
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


for slot, pid, focus, zoom in PICKS:
    im = Image.open(find_src(pid)).convert("RGB")
    im = unify_bg(grade(crop_43(im, focus, zoom)))
    dest = f"{OUT}/{slot}.jpg"
    im.save(dest, quality=84, optimize=True, progressive=True)
    print(f"{slot:26s} <- {pid:>9}   {os.path.getsize(dest)//1024:>4} KB")
