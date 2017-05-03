# -*- coding: utf-8 -*-
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont


def getSize(text, font):
  testImg= PIL.Image.new("RGB", (1,1))
  testDraw= PIL.ImageDraw.Draw(testImg)
  return testDraw.textsize(text, font)


if __name__ == "__main__":
  fontname= "Arial.ttf"
  fontsize= 12
  text= "hello world\nnew line1\nnew line2"

  colorText= "black"
  #colorOutline= "red"
  colorBackground= "white"

  font= PIL.ImageFont.truetype(fontname, fontsize)
  width, height= getSize(text, font)
  img= PIL.Image.new("RGB", (width+1000, height+1000), colorBackground)
  d= PIL.ImageDraw.Draw(img)
  d.text((2, height/2), text, fill=colorText, font=font)
  #d.rectangle((0, 0, width+3, height+3), outline= colorOutline)

  img.save("/Users/mrt/Desktop/Code/derp.png")
