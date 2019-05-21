#!/usr/bin/env python
import math
import time
import os
import random
from microdotphat import *
import datetime
import time

time.sleep(30) # delay to connect to the BT speaker

clear()
show()
fill(1)
show()

set_brightness(1)
          
######### Intro ########################            
  
speed = 4
strings = ["The", " Joker", "Will", "   See", "You", "Now!", "   "]

string = 0
shown = True

os.system('mpg321 /home/pi/Joker/6.mp3 &') # intro talk
time.sleep(3.5)

repeat = 400

################ code from Pimoroni examples #######################
# Start time. Phase offset by math.pi/2
start = time.time()

while repeat > 0:
    # Fade the brightness in/out using a sine wave
    b = (math.sin((time.time() - start) * speed) + 1) / 2
    set_brightness(b)

    # At minimum brightness, swap out the string for the next one
    if b < 0.002 and shown:
        clear()
        write_string(strings[string], kerning=False)

        string += 1
        string %= len(strings)

        show()
        shown = False

    # At maximum brightness, confirm the string has been shown
    if b > 0.998:
        shown = True

    # Sleep a bit to save resources, this wont affect the fading speed
    time.sleep(0.02)
    repeat = repeat - 1

time.sleep(1)
###########################################################################
def joker_says():

    ### clock ###
    clear()
    t = datetime.datetime.now()
    if t.second % 2 == 0:
        set_decimal(2, 1)
        set_decimal(4, 1)
    else:
        set_decimal(2, 0)
        set_decimal(4, 0)
    write_string(t.strftime('%H%M%S'), kerning=False)
    show()
    time.sleep(0.05)
    
    ### Joker speaking ###
    play_speech = random.randrange(1, 1500)#increase the 1500 for less insults
    #print (play_speech) #test remove this
    if play_speech < 10:
        joker_sayings = random.randrange(0, 12)
        print (joker_sayings)
        file_name_to_play = str(joker_sayings) + ".mp3"
        #print (file_name_to_play)
        fill(1)
        show()
		os.system('mpg321 ' + '/home/pi/Joker/' + file_name_to_play + ' &')
        time.sleep(8)
        clear()
        show()
    else:
        pass

while True:
    joker_says()
