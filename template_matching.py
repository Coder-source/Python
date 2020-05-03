import sys
import cv2

if len(sys.argv) < 3:
    print("Designate two image files!")
    sys.exit()

file = sys.argv[1]
file_templ = sys.argv[2]

try:
    img = cv2.imread(file)
    img_template = cv2.imread(file_templ)

    if (img is None) or (img_template is None):
        raise ValueError("File not found!")

    result_match = cv2.matchTemplate(img, img_template, cv2.TM_CCOEFF_NORMED)

    cv2.imshow("Template Matching", result_match)
    cv2.waitKey(0)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result_match)

    top_left = max_loc
    bottom_right = (top_left[0] + img_template.shape[1], top_left[1] + img_template.shape[0])

    cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 2)

    cv2.imshow(file, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except ValueError as e:
    print(e)
except:
    import traceback
    tracback.print_exc()
