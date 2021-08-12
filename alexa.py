
import pyttsx3
import datetime
import speech_recognition as sr 


engine = pyttsx3.init()
# cambiar la voz
voice = engine.getProperty('voices')
engine.setProperty('voices', voice[0].id)
#cambiar la velocidad
newRate = 170
engine.setProperty('rate', newRate)

def hablar(audio):
    engine.say(audio)
    engine.runAndWait()


def tiempo():
    x = datetime.datetime.now()
    hablar('Hoy es ' + x.strftime("%d") + ' a las ' + x.strftime("%H") + ' HORAS'+ 'Y' +  x.strftime("%M") + 'MINUTOS')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Escuchando')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('reconocido')
        query = r.recognize_google(audio, 'en-US')
        print(query)
    
    except Exception as e:
        print(e)
        hablar('Podes repitir porfavor ', e)
        return 'none'

    return query


takeCommand()

