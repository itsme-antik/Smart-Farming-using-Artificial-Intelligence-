# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 06:24:40 2019

@author: Antik
"""

from gtts import gTTS
import pyglet
import time
text='There is a person infront of you'
texttospeech = gTTS(text=text, lang='en')
filename = 'voice.mp3'
texttospeech.save(filename)
music = pyglet.media.load(filename, streaming=False)
music.play()
time.sleep(music.duration)