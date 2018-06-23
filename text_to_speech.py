# Import the required module for text
# to speech conversion
from gtts import gTTS
# The text that you want to convert to audio
mytext =input("enter text to convert into speech")

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

# Playing the converted file
import pygame as pg
pg.mixer.init(27100,-16,2,2048)#freequency=44100(default)
# unsigned 16 bit
# 1 is mono, 2 is stereo
# number of samples (experiment to get best sound)(2048)
music_file = "welcome.mp3"
pg.mixer.music.load(music_file)
print("===========================   Developed by Teja Thammineni   ==========================")
clock = pg.time.Clock()
pg.mixer.music.play()
while pg.mixer.music.get_busy():
    clock.tick(30)