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
    MAX_CORNERS = 80
    QUALITY_LEVEL = 0.01
    MIN_DISTANCE = 5.0
    corners = cv2.goodFeaturesToTrack(img_gray, MAX_CORNERS, QUALITY_LEVEL, MIN_DISTANCE)
    for corner_info in corners:
        corner_x, corner_y = corner_info.ravel()
        cv2.circle(img, (corner_x, corner_y), 1, (0, 200, 255), -1)
        cv2.circle(img, (corner_x, corner_y), 8, (0, 200, 255))
    cv2.imshow(file, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except ValueError as e:
    print(e)
except:
    import traceback
    tracback.print_exc()
