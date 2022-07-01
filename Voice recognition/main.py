import pyaudio
import wave
import speech_recognition as sr
import subprocess
from command import commander

running = True


def play_audio(filename):
    chunk = 1024  # Framrate of audio
    wf = wave.open(filename, 'rb')  # r=read, b=binary
    pa = pyaudio.PyAudio()  # using libraby

    Stream = pa.open(  # formats audio
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    data_stream = wf.readframes(chunk)  # file variable

    while data_stream:  # working time
        Stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    Stream.close()
    pa.terminate()


def say(text):            # talk back by terminal
    subprocess.call('say' + text, shell=True)


r = sr.Recognizer()
cmd = commander()

def initSpeech():
    print("Listening.......")

    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source,timeout=3, phrase_time_limit=3)

    commend = " "

    try:
        commend = r.recognize_google(audio)   # recognising using internet
        print("Your Command.....: " + commend)

    except :
        print("I couldn't understand.")
        print(commend)
        if commend == ["quit", "exit", "bye", "goodbye"]:    # exit command
            global running
            running = False
        cmd.discover(commend)    # this for voice reply
        # say('you said' + commend) # this for print the response


while running == True:
    initSpeech()