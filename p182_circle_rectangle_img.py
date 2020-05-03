import cv2
try:
    img = cv2.imread("girl01.jpg")
    if img is None:
        raise ValueError("File not found")
    cv2.circle(img, (250, 250), 200, (0, 200, 255), 3)
    cv2.rectangle(img, (400, 50), (500, 150), (0, 0, 200), 3, 4)
    cv2.imshow("Photo + Circle + Rectangle", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except ValueError as e:
    print(e)
except:
    import traceback
    tracback.print_exc()
