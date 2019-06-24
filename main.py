import mysql.connector
from scipy.io.wavfile import read
import pyaudio
import numpy as np
import wave
import datetime
from scipy import signal
import matplotlib.pyplot as plt


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
 database="FingerprintingDatabase"
)

def saveFingerprint():
    mycursor = mydb.cursor()

    sql = "INSERT INTO ambientes (descricao) VALUES (%s)"
    val = ('ambiente1')
    mycursor.execute(sql, val)
    mydb.commit()


def getSoundSample():
    # initialise pyaudio
    p = pyaudio.PyAudio()

    buffer_size = 4096
    pyaudio_format = pyaudio.paInt16
    n_channels = 1
    samplerate = 48000
    record_sec = 5
    now_ts = datetime.datetime.now()
    now_ts_str = now_ts.strftime("%Y-%m-%d_%H-%M-%S")
    print('Current Timestamp : ', now_ts_str)
    WAVE_OUTPUT_FILENAME = now_ts_str + ".wav"

    stream = p.open(format=pyaudio_format, channels=n_channels, rate=samplerate, input=True,
                    frames_per_buffer=buffer_size)
    frames = []
    print("recording...")

    for i in range(0, int(samplerate / buffer_size * record_sec)):
        data = stream.read(buffer_size)
        frames.append(data)
    print("finished recording")

    # stop Recording\n",
    stream.stop_stream()
    stream.close()
    p.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(n_channels)
    waveFile.setsampwidth(p.get_sample_size(pyaudio_format))
    waveFile.setframerate(samplerate)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

def readAudioFile(filename):
    fs, audio1 = read(filename)
    f, t, S1 = signal.spectrogram(audio1, fs, window='flattop', nperseg=fs // 10, noverlap=fs // 20, scaling='spectrum',
                                  mode='magnitude')
    print('filename: ', filename)
    print('Data length (s): ', t[-1])
    print('Sampling frequency (samples/s): ', fs)

    plt.pcolormesh(t, f[:300], S1[:300][:])
    plt.xlabel('time(s)')
    plt.ylabel('frequency(Hz)')
    plt.show()



if __name__ == '__main__':
    readAudioFile('audioFiles/aircraft_interior_16bits.wav')

