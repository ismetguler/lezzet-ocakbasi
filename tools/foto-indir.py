import os, urllib.request, concurrent.futures

OUT = os.path.dirname(os.path.abspath(__file__)) + "/cand"
os.makedirs(OUT, exist_ok=True)

# slot -> [primary, backup1, backup2]
SLOTS = {
    "tavuk-durum":       [27744717, 29306505, 18330008],
    "tavuk-sis-durum":   [10027451, 9980749, 14774691],
    "kofte-durum":       [36750272, 36750271, 37322774],
    "adana-durum":       [15202777, 9980764, 5175625],
    "kuzu-sis-durum":    [5779413, 5779382, 14774690],
    "pilav-ustu-doner":  [18062062, 18062061, 19805189],
    "tavuk-sis-servis":  [32754748, 32754752, 5643427],
    "kanat-servis":      [5175618, 11299743, 31587878],
    "kofte-servis":      [37206707, 35366590, 37331151],
    "adana-servis":      [7439809, 16260570, 15873840],
    "kuzu-sis-servis":   [37206698, 6089832, 9510363],
}

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def get(job):
    slot, rank, pid = job
    url = f"https://images.pexels.com/photos/{pid}/pexels-photo-{pid}.jpeg?auto=compress&cs=tinysrgb&w=1400"
    dest = f"{OUT}/{slot}__{rank}__{pid}.jpg"
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=45) as r, open(dest, "wb") as f:
            f.write(r.read())
        return f"OK   {slot} #{rank} {pid} {os.path.getsize(dest)//1024}KB"
    except Exception as e:
        return f"FAIL {slot} #{rank} {pid} :: {e}"

jobs = [(s, i, p) for s, ids in SLOTS.items() for i, p in enumerate(ids)]
with concurrent.futures.ThreadPoolExecutor(8) as ex:
    for line in ex.map(get, jobs):
        print(line)
