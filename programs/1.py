import pathlib as ph
import numpy as np

data = ph.Path("dataset")
img_list = len(list(data.glob('*/*.jpg')))
print('total count of the img_list is:',img_list)
img_list = len(list(data.glob('*/*.jpeg')))
print('total count of the img_list is:',img_list)
img_list = len(list(data.glob('*/*.png')))
print('total count of the img_list is:',img_list)
img_label = np.array([kabaddi.name for kabaddi in data.glob('*')])
print('img_labels:',img_label)
