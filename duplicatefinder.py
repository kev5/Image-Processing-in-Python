# Copyright 2017 Keval Khara kevalk@bu.edu
# Copyright 2017 Harish N Sathishchandra harishns@bu.edu
# Copyright 2017 Donato Kava dkava@bu.edu

'''Duplicate Finder'''

from os import listdir
import hashlib
import re
import sys
import numpy as np
from skimage import io, color


def crop(image_data):
    '''Cropping Image'''
    gray_image = color.rgb2gray(image_data)
    image = gray_image - 1
    region = np.argwhere(gray_image - 1)
    (y_start, x_start), (y_stop, x_stop) = region.min(0), region.max(0) + 1
    return image[y_start:y_stop, x_start:x_stop]


def compare(temp, img):
    '''Compare Images'''
    for i in range(4):
        image = np.rot90(img, i)
        flipped = np.fliplr(image)
        if np.array_equal(temp, image) or np.array_equal(temp, flipped):
            return True


def main():
    '''Main'''
    answer = []
    files_dict = {}
    files = [file for file in listdir('.') if file.endswith('.png')]

    for file in files:
        img_data = io.imread(file)
        key = np.sum(img_data)
        if key not in files_dict:
            files_dict[key] = {}
            files_dict[key].update({file: [img_data, True]})
        else:
            files_dict[key].update({file: [img_data, True]})

    for key in files_dict:
        for img_1 in files_dict[key]:
            duplicates = []

            if files_dict[key][img_1][1] is True:
                duplicates = [img_1]
                img_data1 = files_dict[key][img_1][0]
                cropped1 = crop(img_data1)
                files_dict[key][img_1][1] = False
                for img_2 in files_dict[key]:
                    if files_dict[key][img_2][1] is True:
                        img_data2 = files_dict[key][img_2][0]
                        cropped2 = crop(img_data2)
                        if compare(cropped1, cropped2):
                            duplicates.append(img_2)
                            files_dict[key][img_2][1] = False

            if len(duplicates) > 0:
                duplicates.sort(key=lambda x: int(re.split(r'(\d+)', x)[1]))
                answer.append(duplicates)

    answer.sort(key=lambda x: int(re.split(r'(\d+)', x[0])[1]))
    result = open(sys.argv[1], 'w')
    for index in answer:
        result.write(' '.join([i for i in index]) + "\n")
    result.close()
    print(hashlib.sha256(open(sys.argv[1], 'rb').read()).hexdigest())


if __name__ == "__main__":
    main()
