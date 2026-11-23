import cv2

img = cv2.imread(r"Dataset\frames\thermal\146_00008082.png")

x = 389
y = 110
w = 65
h = 60

padding = 30

crop = img[
    max(0, y-padding):y+h+padding,
    max(0, x-padding):x+w+padding
]

cv2.imwrite("wild_boar_crop.png", crop)

print("Crop saved!")