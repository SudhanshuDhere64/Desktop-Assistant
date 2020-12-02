import pyttsx3
import datetime
import speech_recognition as sr
import os
import random
import webbrowser
import operator
import winshell
import winsound
from selenium import webdriver

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)

    if 4 < hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 17:
        speak("Good afternoon")
    else:
        speak("good evening")
    speak("How may i help you sir")


def commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.adjust_for_ambient_noise(source)
        r.energy_threshold = 50
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio)
        print("User Said :", query)
        # speak(query)
    except Exception as e:
        speak("Say that again please")
        return "None"
    return query


if __name__ == '__main__':
    wishme()
    while True:
        query = commands().lower()


        def get_operator_fn(op):
            return {
                '+': operator.add,
                '-': operator.sub,
                'x': operator.mul,
                'divided': operator.__truediv__,
                'Mod': operator.mod,
                'mod': operator.mod,
                '^': operator.xor,
            }[op]


        def eval_binary_expr(op1, oper, op2):
            op1, op2 = int(op1), int(op2)
            return get_operator_fn(oper)(op1, op2)


        if "intro" in query:
            speak("Hello!! My self Eva.")
            speak("I am your virtual assistant")
            speak("I can perform various task such as managing your Schedules, Automating various tasks of your's.")
            speak(
                "I can entertain you with songs, jokes, movies and more things. I can notify you about weather, traffics")
            speak("Just say anything you need!, i am here at your service.")

        elif "add" in query:
            speak("say an expression")
            exp = commands()
            try:
                print(eval_binary_expr(*(exp.split())))
            except Exception as e:
                speak("Cant perform the operation please try again")

        elif "sub" in query:
            speak("say an expression")
            exp2 = commands()
            try:
                print(eval_binary_expr(*(exp2.split())))
            except Exception as e:
                speak("Cant perform the operation please try again")

        elif "mul" in query:
            speak("say an expression")
            exp3 = commands()
            try:
                print(eval_binary_expr(*(exp3.split())))
            except Exception as e:
                speak("Cant perform the operation please try again")

        elif "div" in query:
            speak("say an expression")
            exp4 = commands()
            try:
                print(eval_binary_expr(*(exp4.split())))
            except Exception as e:
                speak("Cant perform the operation please try again")

        elif "mod" in query:
            speak("say an expression")
            exp5 = commands()
            try:
                print(eval_binary_expr(*(exp5.split())))
            except Exception as e:
                speak("Cant perform the operation please try again")

        elif "power" in query:
            speak("say an expression")
            exp6 = commands()
            try:
                print(eval_binary_expr(*(exp6.split())))
            except Exception as e:
                speak("Cant perform the operation please try again")

        elif "break" in query:
            speak("ok sir have a good day")
            break

        elif "find" in query:
            speak("Please Enter the file name you want to search")
            fname = input("Enter the File Name : ")
            print("User Searched for ", fname)
            path = []
            s = "C:"
            for root, dirs, files in os.walk(s):
                if fname in files:
                    path.append(os.path.join(root, fname))
            print(path)

        elif "play music" in query:
            speak("Sure I am here to entertain you with some music")
            dir = "C:\\Users\\PRATIK KATE\\Desktop\\music"
            songs = os.listdir(dir)
            os.startfile(os.path.join(dir, songs[random.randint(0, len(songs) - 1)]))

        elif "youtube" in query:
            webbrowser.open("youtube.com")

        elif "google" in query:
            webbrowser.open("google.com")

        # using web Automation
        elif "browser" in query:

            driver = webdriver.Chrome()
            driver.get('https://google.com')

            speak("What do you want to search")
            print("What do you want to search: ")
            searchBox = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
            ip = commands()
            searchBox.send_keys(ip)

            searchButton = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
            searchButton.click()

        elif "time" in query:
            t = datetime.datetime.now().strftime("%H:%M")
            speak(f"Time is {t}")

        elif "clean Recycle bin" in query:
            try:
                winshell.Recycle_bin().empty()
            except Exception as e:
                speak("Recycle Bin is Empty!")

        elif "create a file" in query:
            speak("say file name")
            fname = commands()
            fhand = open(fname, "w")
            speak("File is created!")
            speak("You Want to write something to file?")
            ch = commands()
            if ch == "yes":
                speak("say whatever you want to write in the file")
                data = commands()
                fhand.write(data)
            else:
                speak("try again")

        elif "alarm" in query:
            speak("set hours")
            hrs = int(commands())
            speak("set minutes")
            mint = int(commands())
            speak("Am or Pm")
            mm = commands()

            if mm == 'pm':  # to convert pm to military time
                hrs += 12

            elif hrs == 12 and mm == 'am':  # to convert 12am to military time
                hrs -= 12

            else:
                pass

            while True:  # infinite loop starts to make the program running until time matches alarm time

                # ringing alarm + execution condition for alarm
                if hrs == datetime.datetime.now().hour and mint == datetime.datetime.now().minute:
                    print("\nIt's the time!")
                    winsound.beep(1000, 1000)
                    break

        elif "login to my instagram" in query:
            fhand = open('passwd.txt')  # store your password in txt file
            p = fhand.readlines()

            driver = webdriver.Chrome()
            driver.get('https://instagram.com')

            idbox = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
            idbox.send_keys('username')  # add your username here

            passbox = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
            idbox.send_keys(p[0])

            button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
            button.click()

