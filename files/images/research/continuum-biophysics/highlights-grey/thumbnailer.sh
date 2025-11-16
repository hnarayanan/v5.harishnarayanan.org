#!/bin/sh

for i in *.png
do
echo "Processing image: $i"
convert  -thumbnail 150 $i thumbnails/$i
done