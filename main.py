#!/usr/bin/env python

import os, sys
from PIL import Image

size = 64, 64
_64pixel = os.path.join(os.path.dirname(os.path.abspath(__file__)), "64x64")
_128pixel = os.path.join(os.path.dirname(os.path.abspath(__file__)), "128x128")
_crop= os.path.join(os.path.dirname(os.path.abspath(__file__)), "cropped")
#create thumnail
if not os.path.exists(_64pixel):
  os.makedirs(_64pixel)
    
for file in os.listdir("input"):
  if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") :       
    if file.endswith(".jpg"):
      outfile = os.path.splitext(file)[0] + ".jpg"
    if file.endswith(".jpeg"):       
      outfile = os.path.splitext(file)[0] + ".jpeg"
    if file.endswith(".png"):               
      outfile = os.path.splitext(file)[0] + ".png"
    newFolder = os.path.join(_64pixel, outfile)   
    try:
      img = Image.open("input/" +file)
      img.thumbnail(size)
      
      img.save(newFolder, "PNG")
    except IOError, ioe:
      print "cannot resize",file
      print str(ioe)

#scale up image
if not os.path.exists(_128pixel):
  os.makedirs(_128pixel)

for file in os.listdir('input'):
  if file.endswith(".png") :       

    outfile = os.path.splitext(file)[0] + ".png"
    newFolder = os.path.join(_128pixel, outfile)                    
    try:
      img = Image.open("input/" + file)
      img = img.resize((128,128), Image.ANTIALIAS)
      img.save(newFolder, "PNG")
    except IOError, ioe:
      print "cannot resize",file
      print str(ioe)

# #crop image to (48x48)
if not os.path.exists(_crop):
  os.makedirs(_crop)

for file in os.listdir('./input'):
  if file.endswith(".png"):       
    outfile = os.path.splitext(file)[0] + ".png"
    newFolder = os.path.join(_crop, outfile)                    
    left = 6
    top = 6
    right = 66
    bottom = 66
    try:
      img = Image.open("input/" +file)
      img = img.crop((left, top, right, bottom))
      img.save(newFolder, "PNG")
    except IOError, ioe:
      print "cannot crop",file
      print str(ioe)
  