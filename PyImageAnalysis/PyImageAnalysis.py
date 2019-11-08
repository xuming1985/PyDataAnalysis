from PIL import Image
from pylab import *

from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=14)
figure()

im = Image.open('./images/t1.jpg')
gray()
subplot(121)
title(u'原图',fontproperties=font)
imshow(im)

pil_im = Image.open('./images/t1.jpg').convert('L')
subplot(122)
title(u'灰度图',fontproperties=font)
axis('off')
imshow(pil_im)

show()
