import os
import glob
from PIL import Image

print('START--->')

print('Image Resize--->')

for path in glob.glob('./original/*.jpg'):
    filename = os.path.basename(path)
    img = Image.open(f'./original/{filename}')
    img = img.convert('RGB')
    img_resize = img.resize((78, 100))
    img_resize.save(f'./conv/{filename}')

print('RESIZE--->OK!')

print('END--->')
