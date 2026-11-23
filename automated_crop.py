import cv2
import os

annotations = [
    (1893, 263, 898, 41, 38),
    (1973, 268, 806, 41, 38),
    (2073, 265, 689, 41, 38),
    (2153, 242, 342, 41, 54),
    (2213, 224, 133, 41, 54),
]

os.makedirs("track2555/thermal", exist_ok=True)
os.makedirs("track2555/rgb", exist_ok=True)

padding = 15

for frame, x, y, w, h in annotations:

    thermal_path = f"track2555/thermal/146_{frame:08d}.png"
    rgb_path = f"track2555/rgb/146_{frame:08d}.png"

    print("Loading:", thermal_path)

    thermal = cv2.imread(thermal_path)
    rgb = cv2.imread(rgb_path)

    if thermal is None:
        print("Could not load:", thermal_path)
        continue

    if rgb is None:
        print("Could not load:", rgb_path)
        continue

    left = max(0, x - padding)
    top = max(0, y - padding)
    right = x + w + padding
    bottom = y + h + padding

    thermal_crop = thermal[top:bottom, left:right]
    rgb_crop = rgb[top:bottom, left:right]

    cv2.imwrite(
        f"track2555/thermal_crop_{frame}.png",
        thermal_crop
    )

    cv2.imwrite(
        f"track2555/rgb_crop_{frame}.png",
        rgb_crop
    )

    print(f"Saved crops for frame {frame}")

print("Done!")