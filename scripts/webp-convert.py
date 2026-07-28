import os
from PIL import Image

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src", "images")
converted = errors = 0

for dirpath, _, filenames in os.walk(root):
    for fname in filenames:
        if not fname.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
            continue

        src = os.path.join(dirpath, fname)
        basename = os.path.splitext(fname)[0]
        dst = os.path.join(dirpath, basename + ".webp")

        if os.path.exists(dst):
            print(f"SKIP (exists): {fname}")
            continue

        try:
            img = Image.open(src)
            img.save(dst, "WEBP", quality=85)
            os.remove(src)
            print(f"OK: {fname} -> {basename}.webp")
            converted += 1
        except Exception as e:
            print(f"ERR: {fname}: {e}")
            errors += 1

print(f"\nDone: {converted} converted, {errors} errors")
