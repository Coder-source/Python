import os
import shutil
import glob
from PIL import Image
import numpy as np
from skimage import io
from sklearn.cluster import KMeans

print('START--->')

print('Initialize--->')
for path in glob.glob('./conv/*.jpg'):
    print('Convert File Delete --> ' + path)
    os.remove(path)

for path in glob.glob('./group/'):
    shutil.rmtree(path)
    print('Grouping Directory Delete --> ' + path)

print('Image Resize--->')
for path in glob.glob('./original/*.jpg'):
    filename = os.path.basename(path)
    img = Image.open(f'./original/{filename}')
    img = img.convert('RGB')
    img_resize = img.resize((78, 100))
    img_resize.save(f'./conv/{filename}')

print('RESIZE--->OK!')

feature = np.array([
    io.imread(path)
    for path in glob.glob('./conv/*.jpg')
])

print('Data Create--->OK!')

feature = feature.reshape(len(feature), -1).astype(np.float64)

print('Data Adjust--->OK!')

model =KMeans(n_clusters = 4).fit(feature) # Execution of K-means
print("KMeans--->OK!")

labels = model.labels_ #Heed the "_" at the end of the line.
for label, path in zip(labels, glob.glob("./conv/*.jpg")):
    filename = os.path.basename(path).replace(".jpg", "") + ".jpg"
    os.makedirs(f"./group/{label}", exist_ok = True) #Preparation of a group folder
    shutil.copyfile(f"./original/{filename}", f"./group/{label}/{filename}")
    print(label, filename)

print('END--->')
