import speech_recognition as sr

    # Initialize the recognizer class
r = sr.Recognizer()

    # Read from the microphone as the source
with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")


try:
        # Use Google speech recognition
    print("Text:", r.recognize_google(audio_text))
except:
    print("Sorry, I did not get that")
    
