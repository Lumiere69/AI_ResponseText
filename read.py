from PIL import Image as pil
from selenium import webdriver
import pytesseract as pt
import cv2
import search

def name(file, useParser=True):

    img = cv2.imread(file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text =pt.image_to_string(img)
    data = pt.image_to_data(img)
    img = cv2.resize(img, dsize=(0, 0), fx=5, fy=5)


    for i, el in enumerate(data.splitlines()):
      if i == 0:
        continue

      el = el.split()
      try:
        # Создаем подписи на картинке
        x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
        cv2.rectangle(img, (x*5, y*5), ((w + x)*5, (h + y)*5), (0, 0, 255), 1)
        cv2.putText(img, el[11], (x*5, y*5), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)
      except IndexError:
          pass
    # Отображаем фотоw
    img = pil.fromarray(img)
    img.show()
    img.save("output.png")

    massive = text.split("\n")

    #parser
    if useParser:
        parser = search.Parser()
        parser.all(massive)
    return text