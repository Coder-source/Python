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
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    retValue, img_thresh = cv2.threshold(img_gray, 100, 200, cv2.THRESH_BINARY)
    cv2.imshow(file, img_thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except ValueError as e:
    print(e)
except:
    import traceback
    tracback.print_exc()
