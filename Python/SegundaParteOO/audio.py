import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile(r"C:\udio_longo.wav") as source:
    # r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    try:
        texto = r.recognize_google(audio, language='pt-br')
        print('A transcrição do áudio está a seguir:')
        print(texto)
    except:
        print('Desculpe, tente novamente')
