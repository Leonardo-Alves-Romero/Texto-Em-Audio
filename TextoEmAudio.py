from gtts import gTTS
from playsound import playsound

audio = 'audio.mp3'
linguagem = 'pt-br'

sp = gTTS(
    text= 'Seja bem vindo ao meu github aproveite para utilizar este código em seu pc espero que goste e se divirta!!. ',
    lang= linguagem
)

sp.save(audio)
playsound(audio)