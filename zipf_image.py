from PIL import Image
import matplotlib.pyplot as plt
from collections import Counter

#/home/ivanush/Pictures/alena-aenami-horizon-1k.jpg
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


plt.plot( list(range(len(red.items()))), sorted(list(red.values()), reverse=1), color ='red')
plt.plot( list(range(len(green.items()))), sorted(list(green.values()), reverse=1), color= 'green')
plt.plot( list(range(len(blue.items()))), sorted(list(blue.values()), reverse=1), color='blue')

#plt.figure()
#plt.subplot(1)
#plt.plot( list(range(len(red.items()))), sorted(list(red.values()), reverse=1))
#plt.subplot(2)
#plt.plot( list(range(len(green.items()))), sorted(list(green.values()), reverse=1))
#plt.subplot(3)
#plt.plot( list(range(len(blue.items()))), sorted(list(blue.values()), reverse=1))


plt.show()