<<<<<<< HEAD
from gtts import gTTS
from deep_translator import GoogleTranslator

def generate_hindi_tts(text, filename="output.mp3"):
    gTTS(text=GoogleTranslator(source="auto", target="hi").translate(text), lang="hi").save(filename)
=======
from gtts import gTTS
from deep_translator import GoogleTranslator

def generate_hindi_tts(text, filename="output.mp3"):
    gTTS(text=GoogleTranslator(source="auto", target="hi").translate(text), lang="hi").save(filename)
>>>>>>> e1e754f (Initial commit)
    return filename