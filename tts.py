from gtts import gTTS
from deep_translator import GoogleTranslator

def generate_hindi_tts(text, filename="output.mp3"):
    gTTS(text=GoogleTranslator(source="auto", target="hi").translate(text), lang="hi").save(filename)
    return filename