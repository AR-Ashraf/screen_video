import numpy as np
import cv2
from PIL import ImageGrab

fourcc = cv2.VideoWriter_fourcc('X', '2', '6', '4')  # you can use other codecs as well.
size = (ImageGrab.grab()).size
out = cv2.VideoWriter('output.mp4', fourcc, 5.0, size)
while True:
    img = ImageGrab.grab()
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
out.release()
cv2.destroyAllWindows()
