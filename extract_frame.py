import cv2

video = cv2.VideoCapture("bambi_downloads/146_matched_processed.mp4")

frame_number = 8082

video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

ret, frame = video.read()

if ret:
    cv2.imwrite("frame8082.png", frame)
    print("Saved frame8082.png")

video.release()