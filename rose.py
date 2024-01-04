from gtts import gTTS
import speech_recognition as sr
from subprocess import call, run # MAC / LINUX
from requests import get
from bs4 import BeautifulSoup

#from gtts import gTTS
from playsound import playsound

##### CONFIGURAÇÕES #####
hotword = 'rose'

def monitora_audio():
    # obtain audio from the microphone
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Aguardando o Comando!")
            audio = microfone.listen(source)

        ##### TESTE COMANDO GENÉRICO #####
            try:
                trigger = microfone.recognize_google(audio, language='pt-br')
                trigger = trigger.lower()
                if hotword in trigger:
                    print('Comando: ', trigger)
                    responde('feedback')
                    execulta_comandos(trigger)
                    break

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return trigger
def responde(arquivo):
    call(['aplay', 'audios/'+arquivo +'.mp3'])  # LINUX

def cria_audio(menssagem):
    #audio = 'audio.mp3'
    #language = 'pt-br'
    #sp = gTTS(
    #    text='Meu primeiro áudio gerado em Python',
    #    lang=language
    #)
    #sp.save(audio)
    #playsound(audio)

    # tts = gTTS(menssagem, lang='pt-br')
    # tts.save('audios/menssagem.mp3')

    #call(['afplay', 'audios/hello.mp3']) # OSX
    #call(['aplay', 'audios/menssagem.mp3']) # LINUX
    #run(['aplay', 'audios/menssagem.mp3'])  # LINUX
    #playsound('audios/hello.mp3') # WINDOWS

    audio = 'audio.mp3'
    language = 'pt-br'

    sp = gTTS(
        text=menssagem,
        lang=language
    )
    sp.save(audio)
    playsound(audio)
def execulta_comandos(trigger):
    if 'notícias' in trigger:
        ultimas_noticias()

##### FUNÇÕES PRINCIPAIS #####

def ultimas_noticias():
    site = get('https://news.google.com/news/rss?ned=pt_br&gl=BR&hl=pt')
    noticias = BeautifulSoup(site.text, 'html.parser')
    for item in noticias.findAll('item')[:5]:
        menssagem = item.title.text
        print(menssagem)
        cria_audio(menssagem)

def main():
    monitora_audio()
    #cria_audio(monitora_audio())

#main()
ultimas_noticias()