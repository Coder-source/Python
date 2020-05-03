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
    MOSAIC_SCALE = 0.1 #reduction ratio
    img_height = img.shape[0]
    img_width = img.shape[1]
    mosaic = cv2.resize(img, (round(img_width * MOSAIC_SCALE),
    round(img_height * MOSAIC_SCALE)), interpolation=cv2.INTER_NEAREST)
    mosaic = cv2.resize(mosaic, (img_width, img_height),
    interpolation=cv2.INTER_NEAREST)
    cv2.imshow(file, mosaic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except ValueError as e:
    print(e)
except:
    import traceback
    tracback.print_exc()
