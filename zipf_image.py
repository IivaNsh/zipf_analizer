from PIL import Image
import matplotlib.pyplot as plt
from collections import Counter

#/home/ivanush/Pictures/alena-aenami-horizon-1k.jpg
#/home/ivanush/Pictures/Screenshot_20221225_02dkmsd5929.png
#/home/ivanush/Pictures/ef32583c76bd7a7a97593c443c964c64.jpg
#koni.jpeg
#juan.jpg

file_path = input()

img = Image.open(file_path)

pixel_data = img.load()

#print(pixel_data[0,0])

red = Counter()
green = Counter()
blue = Counter()

rs, gs, bs, = [], [], []

for y in range(img.height):
    for x in range(img.width):
        rs.append(pixel_data[x,y][0])
        gs.append(pixel_data[x,y][1])
        bs.append(pixel_data[x,y][2])

red = Counter(rs)
green = Counter(gs)
blue = Counter(bs)


#plt.plot( list(range(len(red.items()))), sorted(list(red.values()), reverse=1), color ='red')
#plt.plot( list(range(len(green.items()))), sorted(list(green.values()), reverse=1), color= 'green')
#plt.plot( list(range(len(blue.items()))), sorted(list(blue.values()), reverse=1), color='blue')




x, ax = plt.subplots(2)
ax[0].plot( list(range(len(red.items()))), sorted(list(red.values()), reverse=1), color ='red')
ax[0].plot( list(range(len(green.items()))), sorted(list(green.values()), reverse=1), color= 'green')
ax[0].plot( list(range(len(blue.items()))), sorted(list(blue.values()), reverse=1), color='blue')

red_s = sorted(red.items(),key=lambda x: x[0], reverse=1)
green_s = sorted(green.items(),key=lambda x: x[0], reverse=1)
blue_s = sorted(blue.items(),key=lambda x: x[0], reverse=1)

nums = img.width*img.height

pred = [v[0] for v in red_s]
pgreen = [v[0] for v in green_s]
pblue = [v[0] for v in blue_s]

vred = [v[1]/nums for v in red_s]
vgreen = [v[1]/nums for v in green_s]
vblue = [v[1]/nums for v in blue_s]

#ax[1].plot( pred, vred,'o', color ='red')
#ax[1].plot( pgreen, vgreen,'o', color= 'green')
#ax[1].plot( pblue, vblue,'o', color='blue')

ax[1].plot( pred, vred, color ='red')
ax[1].plot( pgreen, vgreen, color= 'green')
ax[1].plot( pblue, vblue, color='blue')



#plt.figure()
#plt.subplot(1)
#plt.plot( list(range(len(red.items()))), sorted(list(red.values()), reverse=1))
#plt.subplot(2)
#plt.plot( list(range(len(green.items()))), sorted(list(green.values()), reverse=1))
#plt.subplot(3)
#plt.plot( list(range(len(blue.items()))), sorted(list(blue.values()), reverse=1))


plt.show()