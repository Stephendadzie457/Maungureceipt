from PIL import Image
import numpy as np

img = Image.open("assets/logo-mark'.png").convert("RGB")
arr = np.array(img).astype(int)
orange = np.array([235, 120, 40])
dist = np.linalg.norm(arr - orange, axis=2)
mask = dist > 60
h, w = mask.shape
rgba = np.zeros((h, w, 4), dtype=np.uint8)
rgba[:, :, :3] = arr
rgba[:, :, 3] = np.where(mask, 255, 0)
result = Image.fromarray(rgba, "RGBA")
result.save("assets/logo-mark-clean.png", "PNG")
print("Saved logo-mark-clean.png", result.size)