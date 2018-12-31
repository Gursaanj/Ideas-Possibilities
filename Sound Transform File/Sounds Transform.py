import numpy as np
import matplotlib.pyplot as plt 
import scipy as sp
import scipy.io.wavfile as io ## To be able to import and alter wav sound files

#Replace the file with whatever wav file you want (make sure it is in the same)
#folder. Make sure to correct the name in line 10 with the name of the wav file

# rate in BPM and data is a file size component in terms of amplitude
rate, data = io.read("Monster_Growl.wav")

time = np.arange(0,data.size)

# This speeds up the wav file by playing the same data by cutting the time by 2
# this is done by only gathering every even indexed piece of data

def Quicken(q):
    sped_up = q[::2]
    return sped_up

Quicker = Quicken(data)
io.write("Quickened_version.wav", rate, Quicker)

# This Deepens the wav file by playing the same data along a longer period
# This is by copying and placing a similar piece of data after every indexed 
# entry

def Deepen(d):
    deepened = d.repeat(1.5)
    return deepened

Deep_low = Deepen(data)
io.write("Elongated_version.wav", rate, Deep_low)

#This Demonizes the wav file by playing it backwards at the same rate

def Demonize(d):
    Demon = d[::-1]
    return Demon

Demon_voice = Demonize(data)
io.write("Demonic_playback.wav", rate, Demon_voice)