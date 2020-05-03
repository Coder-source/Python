import cv2
try:
    img = cv2.imread("girl01.jpg") #Define the image file.
    if img is None:
        raise ValueError("File not found")
    cv2.putText(img, "When do you drink a smoothie?", (20, 50),
    cv2.FONT_HERSHEY_COMPLEX, 1.1, (0, 0, 255), 2)
    cv2.imshow("Photo + Text", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except ValueError as e:
    print(e)
except:
    import traceback
    traceback.print_exc()
