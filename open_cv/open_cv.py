import cv2
import numpy as np

# ekran boyutu
height, width = 500, 500
canvas = np.zeros((height, width, 3), dtype=np.uint8)


start_point = (50, 50)
end_point = (400, 400)
center = (250, 250)
radius = 100
color = (0, 255, 0)  #yesil
thickness = 3

while True:
    cv2.imshow("Canvas", canvas)
    key = cv2.waitKey(1) & 0xFF  

    if key == ord('d'):
        # Dikdörtgen çiz
        cv2.rectangle(canvas, start_point, end_point, color, thickness)
    elif key == ord('y'):
        # Daire çiz
        cv2.circle(canvas, center, radius, color, thickness)
    elif key == ord('l'):
        # Çizgi çiz
        cv2.line(canvas, start_point, end_point, color, thickness)
    elif key == ord('s'):
        # Kaydet
        cv2.imwrite("canvas.png", canvas)
        print("Resim kaydedildi: canvas.png")
    elif key == ord('q'):
        # Çýkýþ
        break

cv2.destroyAllWindows()

