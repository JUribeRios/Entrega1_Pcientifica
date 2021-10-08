#!/bin/bash

directorio="/home/programacion3/JulianUribe/Images720x1280"
script="/home/programacion3/JulianUribe/undistorted.py"

for i in $(ls $directorio)
do

sleep 2
echo "python3 $script --filepath $i" | qsub -l nodes=1:ppn=1 

done
