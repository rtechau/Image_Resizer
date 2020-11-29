import os
from PIL import Image


image_folder = '/path/to/image/folder'

def resizer():
    for root, subdirs, files in os.walk(image_folder):
        for item in files:
            if item.endswith('png'):
                img = Image.open(f'{root}/{item}')
                half = 0.5
                resized_img = img.resize([int(half * s) for s in img.size])
                resized_img.save(f'{root}/Resized_{item}')
                os.remove(f'{root}/{item}')
                print(f'{item}: all done!')

resizer()