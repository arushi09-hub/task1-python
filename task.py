import os
import pyttsx3
print('===================================================================================')
print('                                    Chat Bot                                       ')
print('===================================================================================')
pyttsx3.speak('Hello User,Please enter your name')
name=input('Enter your name here : ')

pyttsx3.speak('Hey '+name+' , What can I do for you')
command=input('What do you want to do : ')

if("chrome" in command):
    pyttsx3.speak('Enter URL for chrome')
    chrome=input('Enter URL for chrome : ')
    os.system('start chrome '+chrome)

elif("notepad" in command):
    pyttsx3.speak('Enter file name')
    notepad=input('Enter the filename (with extension) which you want to open with Notepad : ')
    os.system('notepad '+notepad)

elif("date" in command):
    pyttsx3.speak('You requested for date')
    os.system('date /t')

elif("time" in command):
    pyttsx3.speak('You requested for time')
    os.system('time /t')

elif("cls" in command or "clear screen" in command):
    pyttsx3.speak('Clearing the Screen')
    os.system('cls')

elif(command=='Clear Screen And Run Bot'):
    pyttsx3.speak('You entered Clear Screen And Run Bot ')
    os.system('cls')
    os.system('python task1.py')

elif("my ip" in command):
    pyttsx3.speak('I P will be displayed shortly')
    os.system('ipconfig')

elif(command=='Sleep System'):
    pyttsx3.speak('Enter Amount of time')
    amt=input('Enter amount of time : ')
    os.system('timeout '+amt)
else:
   print('Wrong Choice')
   pyttsx3.speak('You had entered wrong choice');