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

    RESIZE_WIDTH = 800
    img_height = img.shape[0]
    img_width = img.shape[1]
    if img_width > RESIZE_WIDTH:
        img_resize = cv2.resize(img, (RESIZE_WIDTH, int(RESIZE_WIDTH / img_width * img_height)))
    else:
        img_resize = img

    img_gray = cv2.cvtColor(img_resize, cv2.COLOR_RGB2GRAY)

    CASCADE_FILE = "haarcascade_frontalface_alt.xml"

    haar_cascade = cv2.CascadeClassifier(CASCADE_FILE)
    detection = haar_cascade.detectMultiScale(img_resize, scaleFactor = 1.1,
    minNeighbors = 2, minSize = (30, 30))

    if len(detection) > 0:
        for rect in detection:
            cv2.rectangle(img_resize, tuple(rect[0:2]),
            tuple(rect[0:2] + rect[3:4]), (0, 0, 255), thickness = 2)
    else:
        cv2.putText(img_resize, "no match found", (20, 50), cv2.FONT_HERSHEY_COMPLEX,
        1.0, (0, 0, 255), 2)

    cv2.imshow(file, img_resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except ValueError as e:
    print(e)
except:
    import traceback
    tracback.print_exc()
