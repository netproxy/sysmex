import os
import sys


images = []
labels = []


def traverse_dir(path):
    for file_or_dir in os.listdir(path):
        abs_path = os.path.abspath(os.path.join(path, file_or_dir))
        print(abs_path)
        if os.path.isdir(abs_path):  # dir
            traverse_dir(abs_path)
        else:                        # file
            if file_or_dir.endswith('.eml'):
                image = read_image(abs_path)
                #cv2.imwrite('/mnt/c/Dell/c.jpg',image)
                images.append(image)
                labels.append(path)
    
    return images, labels


