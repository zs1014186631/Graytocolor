import numpy as np
from PIL import Image


im_r = Image.open(r'D:\yuantu\f.png')
im_rr = Image.fromarray(np.uint8(im_r))
print(im_rr.mode)
t = im_rr.convert("L")
print(t.mode)
im_rrr = Image.fromarray(np.uint8(t))    #原来是im_rrr = Image.fromarray(np.uint8(t)*255)
print(im_rrr.mode)
im_rrr.save(r'D:\yuantu\convert_model6.png')
im_rrr
