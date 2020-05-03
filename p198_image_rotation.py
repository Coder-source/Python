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
    img_height = img.shape[0]
    img_width = img.shape[1]
    img_center = (int(img_width / 2), int(img_height / 2)) #Calculation of the center
    img_rotate = cv2.getRotationMatrix2D(img_center, 20.0, 1.0)
    effect = cv2.warpAffine(img, img_rotate, (img_width, img_height))
    cv2.imshow(file, effect)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except ValueError as e:
    print(e)
except:
    import traceback
    tracback.print_exc()
