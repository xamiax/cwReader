import pyaudio
import numpy as np

p = pyaudio.PyAudio()

volume = 0.5     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 5.0   # in seconds, may be float
f = 500.0        # sine frequency, Hz, may be float

ditduration = 0.2   # in seconds, may be float
dahduration = 3*ditduration   # in seconds, may be float
sigpauseduration = ditduration   # in seconds, may be float
charpauseduration = 3*ditduration   # in seconds, may be float
wordpauseduration = 7*ditduration   # in seconds, may be float



# generate samples, note conversion to float32 array
samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

dit = (np.sin(2*np.pi*np.arange(fs*ditduration)*f/fs)).astype(np.float32)
dah = (np.sin(2*np.pi*np.arange(fs*dahduration)*f/fs)).astype(np.float32)
sigpause = (np.sin(2*np.pi*np.arange(fs*sigpauseduration)*0/fs)).astype(np.float32)
charpause = (np.sin(2*np.pi*np.arange(fs*charpauseduration)*0/fs)).astype(np.float32)
wordpause = (np.sin(2*np.pi*np.arange(fs*wordpauseduration)*0/fs)).astype(np.float32)

c = np.hstack((dah,sigpause,dit,sigpause,dah,sigpause,dit,charpause))


# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

# play. May repeat with different volume values (if done interactively)
stream.write(volume*dah)
stream.write(volume*sigpause)
stream.write(volume*dit)
stream.write(volume*sigpause)
stream.write(volume*dah)
stream.write(volume*sigpause)
stream.write(volume*dit)
stream.write(volume*charpause)
stream.write(volume*dah)
stream.write(volume*sigpause)
stream.write(volume*dah)
stream.write(volume*sigpause)
stream.write(volume*dit)
stream.write(volume*sigpause)
stream.write(volume*dah)
stream.write(volume*charpause)


stream.stop_stream()
stream.close()

p.terminate()
