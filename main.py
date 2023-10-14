import speech_recognition as s_r
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = s_r.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

command=''
def take_command():
    global command
    try:
        print('listening...')
        print(s_r.__version__) # just to print the version not required
        r = s_r.Recognizer()
        my_mic = s_r.Microphone(device_index=1) #my device index is 1, you have to put your device index
        
        with my_mic as source:
            print("Say now!!!!")
            audio = r.listen(source) #take voice input from the microphone
        print(r.recognize_google(audio))
        command=r.recognize_google(audio)
            # voice = listener.listen(source)
            # command = listener.recognize_google(voice)
            # command = command.lower()
            # if 'alexa' in command:
            #     command = command.replace('alexa', '')
            #     print(command)
    except:
        print('no')
    return command

def run_alexa(command):

    #time.sleep(30)
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please tell the command again.')


while True:
     command=take_command()
     run_alexa(command)
