import pyaudio
import wave
import speech_recognition as sr


def play_audio(filename):
    chunk = 1024               # Framrate of audio
    wf = wave.open(filename, 'rb')   # r=read, b=binary
    pa = pyaudio.PyAudio()     # using libraby

    Stream = pa.open(                      #formats audio
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    data_stream = wf.readframes(chunk)           #file variable

    while data_stream:                #working time
        Stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    Stream.close()
    pa.terminate()

play_audio("./Game-Show-Buzzer.wav")   #file location

