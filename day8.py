import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint

with open('day8.txt') as fin:
    contents = fin.read()

width = 25
height = 6

pix_per_layer = width * height
num_layers = int(len(contents) / pix_per_layer)

layer_list = list()
for _ in range(num_layers):
    layer_list.append(contents[:pix_per_layer])
    contents = contents[pix_per_layer:]

min_zero_cnt = None
min_zero_product = None
final_image = None

for layer in layer_list:
    zeroes = layer.count('0')
    ones = layer.count('1')
    twos = layer.count('2')

    if not min_zero_cnt:
        min_zero_cnt = zeroes
        min_zero_product = ones * twos
    elif zeroes < min_zero_cnt:
        min_zero_cnt = zeroes
        min_zero_product = ones * twos
                
    if not final_image:
        final_image = list(layer)
    else:
        for idx, val in enumerate(layer):
            if int(final_image[idx]) == 2:
                final_image[idx] = val
    
image_array = list()
cur_row = list()
for i, c in enumerate(final_image):
    if i % width == 0 and i > 0:
        image_array.append(cur_row)
        cur_row = list()
    cur_row.append(int(c))
image_array.append(cur_row)
pprint(image_array)

plt.imshow(image_array)
plt.show()