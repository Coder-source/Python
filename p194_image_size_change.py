import sys
import cv2
if len(sys.argv) < 2:
    print("Designate the file you would like to display!")
    sys.exit() #Terminate the command because no files are designated.
file = sys.argv[1]
try:
    img = cv2.imread(file)
    if img is None:
        raise ValueError("File not found!")
    RESIZE_SCALE = 0.5 #magnification
    img_height = img.shape[0]
    img_width = img.shape[1]
    effect = cv2.resize(img, (int(img_width * RESIZE_SCALE), int(img_height * RESIZE_SCALE)))
    cv2.imshow(file, effect)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except ValueError as e:
    print(e)
except:
    import traceback
    tracback.print_exc()
