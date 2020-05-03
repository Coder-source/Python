import cv2
try:
    img = cv2.imread("girl01.jpg") #Define the image file.
    if img is None:
        raise ValueError("File not found")
    cv2.imshow("Photo", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except ValueError as e:
    print(e)
except:
    import traceback
    traceback.print_exc()
