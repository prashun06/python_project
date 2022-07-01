import speech_recognition as sr


r = sr.Recognizer()


def initSpeech():
    print("Listening.......")

    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source, timeout=3, phrase_time_limit=3)

    commend = " "

    try:
        commend = r.recognize_google(audio)   # recognising using internet
        print("Your Command.....: " + commend)
    except :
        print("I couldn't understand.")


initSpeech()