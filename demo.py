import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Calibrating for background noise...")
    r.adjust_for_ambient_noise(source, duration=1)
    print("Listening now — please speak clearly.")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio, language="en-IN")  # Change lang code if needed
    print(f"You said: {text}")
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print(f"API error: {e}")
