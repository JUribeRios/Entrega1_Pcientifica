#!/home/programacion3/.linuxbrew/bin/python3

from math import sqrt,pow,atan
import numpy as np
import time
from PIL import Image
import argparse


ap= argparse.ArgumentParser()
ap.add_argument("-f", "--filepath", required=True)
args= ap.parse_args()

image= Image.open('/home/programacion3/JulianUribe/Images720x1280/'+args.filepath)
#image= Image.open('/home/programacion3/JulianUribe/WIN_20210528_18_18_45_Pro.jpg')
img= np.array(image)
img= img[:,:,0]

fila=720
columna=1280

halfWidth = fila / 2
halfHeight = columna / 2
strength = 2.3
correctionRadius = sqrt(pow(fila, 2) + pow(columna, 2)) / strength

dstImage=np.array(img)

start= time.time()

for i in range(fila):
    
    for j in range(columna):
        
        newX = i - halfWidth 
        newY = j - halfHeight
        
        distance = sqrt(pow(newX, 2) + pow(newY, 2))
        r = distance / correctionRadius
        
        if r == 0.0:          
            theta= 1
        else:
            theta = atan(r) / r

        sourceX = round(halfWidth + theta*newX);
        sourceY = round(halfHeight + theta * newY);
        
        dstImage[i][j] = img[sourceX][sourceY]
        
total= time.time() - start
print(total)

pil_image= Image.fromarray(dstImage)
pil_image.save('/home/programacion3/JulianUribe/Resultado/'+args.filepath)
#pil_image.save('/home/programacion3/JulianUribe/Result.png')


