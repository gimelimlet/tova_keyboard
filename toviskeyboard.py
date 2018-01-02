import pygame, time
from pygame.locals import *
import secrets


pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pygame Keyboard Test')
#pygame.mouse.set_visible(0)
global keylist
global randoms

keylist = {27:'esc', 282:'f1', 283:'f2', 284:'f3', 285:'f4', 286:'f5', 287:'f6',
           288:'f7', 289:'f8', 290:'f9', 291:'f10', 292:'f11', 293:'f12',
           19:'pause', 316:'prt sc', 277:'insert', 127:'delete', 96:'fractions',
           49:'1', 50:'2', 51:'3', 52:'4', 53:'5', 54:'6', 55:'7', 56:'8', 57:'9',
           48:'0', 45:'+', 61:'´', 8:'backspace', 278:'home', 97:'a', 98:'b', 99:'c',
           100:'d', 101:'e', 102:'f', 103:'g', 104:'h', 105:'i', 106:'j', 107:'k',
           108:'l', 109:'m', 110:'n', 111:'o', 112:'p', 113:'q', 114:'r',           115:'t',
           115:'s', 116:'t', 117:'u', 118:'v', 119:'w', 120:'x', 121:'y', 122:'z',
           91:'å', 39:'ä', 59:'ö', 9:'tab', 301:'caps lock', 304:'shift',
           306:'control', 311:'winkey', 308:'alt', 32:'space', 306:'alt gr',
           319:'rightclick', 305:'rt ctrl', 276:'left', 274:'down', 275:'right',
           60:'bigger than', 280:'pgup', 281:'pgdn', 279:'end', 273:'up',
           303:'rt shift', 47:'dash', 46:'stop', 44:'comma', 93:'umlaut',
           92:'inverted comma'}
randoms = ['titta.mp3', 'tova.mp3', 'error.mp3', 'prutt.mp3', 'hello.mp3',
           'batscatter.mp3', 'camel2.mp3', 'crocodile.mp3', 'bark3.mp3',
           'whale3.mp3']

           
while True:
   pygame.mixer.init()
   for event in pygame.event.get():
      if event.type == KEYUP:
         #print(event.key)
         #print (keylist.get(event.key))
         time.sleep(0.3)
         try:
            soundfile = keylist.get(event.key) + '.mp3'         
            pygame.mixer.music.load(soundfile)
            pygame.mixer.music.play()
         except:
            
            pygame.mixer.music.load(secrets.choice(randoms))
            pygame.mixer.music.play()
            
         

