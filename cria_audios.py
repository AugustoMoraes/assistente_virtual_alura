from gtts import gTTS
from subprocess import call # MAC / LINUX
#from playsound import playsound # WINDOWS
def cria_audio(audio):
    tts = gTTS(audio, lang='pt-br')
    tts.save('feedback.mp3')

    #call(['afplay', 'audios/hello.mp3']) # OSX
    call(['aplay', 'audios/feedback.mp3']) # LINUX
    #playsound('audios/hello.mp3') # WINDOWS

cria_audio('Espera aí')