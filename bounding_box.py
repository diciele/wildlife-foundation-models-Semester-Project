import cv2

img = cv2.imread(r"test3291\thermal\146_00003291.png")

x = 779
y = 19
w = 46
h = 60

cv2.rectangle(
    img,
    (x, y),
    (x + w, y + h),
    (0, 255, 0),
    2
)

cv2.imwrite("thermal_boxed_frame.png", img)

print("Saved boxed_frame.png")