import pygame
import os
import select
import read
inp = input('>>>')
useParser = True
while inp != 'exit':

    if inp == 'enable parser' or inp == 'ep':
        useParser = True

    if inp == 'disenable parser' or inp == 'dp':
        useParser = False

    if inp.find('file=') == 0:
        file_name = inp[6:]
        pygame.image.save(select.get_area(file_name), 'temp1.png')
        text = read.name('temp1.png', useParser=useParser)
        print(text)
    inp = input('>>>')
os.remove("temp1.png")
