

import json
from urllib import request
import pyttsx3
import datetime
import speech_recognition as sr 
import pyaudio
import requests
import random



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

def getPoke():
    url = 'https://pokeapi.co/api/v2/pokemon'
    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        results = payload.get('results', [])
        pokeArr = []
        if results:
            for pokemon in results:
                name = pokemon['name']
                pokeArr.append(name)
        
    value = random.randint(0,10)
    return pokeArr[value]

def getCoin():
    url = 'https://min-api.cryptocompare.com/data/top/mktcapfull?limit=10&tsym=USD'
    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        results = json.dumps(payload)
        finish = json.loads(results)
        finish = finish["Data"]
        # [0]["CoinInfo"]["FullName"]
        coinArr = []
        if results:
            for coin in finish:
                name = coin
                coinArr.append(name)
        
        return[coinArr]
    

def tiempo():
    x = datetime.datetime.now()
    hablar('Hoy es ' + x.strftime("%d") + ' a las ' + x.strftime("%H") + ' HORAS'+ 'Y' +  x.strftime("%M") + 'MINUTOS')

def coins():
    arrCoins = getCoin()

    for arrcoin1 in arrCoins:    
        for coin in arrcoin1[0:3]:
            hablar('la moneda ' + coin["CoinInfo"]["FullName"] + '. Cotiza ' + coin["DISPLAY"]["USD"]["PRICE"])
        
    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Escuchando')
        r.pause_threshold - 1
        r.adjust_for_ambient_noise(source, duration= 1)
        audio = r.listen(source, 1000)
        print(audio)
    try:
        print('reconocido')
        query = r.recognize_google(audio, language='en-US')
        print(query)
    except Exception as e:
        print(e)
        hablar('Podes repitir porfavor ', e)

        return 'None'

    return query

if __name__ == '__main__':
    hablar('Hola Rey, buenos dias!')
    while True:
        query = takeCommand().lower()
        print(query)
        if 'time' in query:
            tiempo()
        elif 'pokemon' in query:
            hablar(getPoke())
        elif 'money' in query:
            coins()
        elif 'offline' in query:
            quit()


