import speech_recognition as sr
import pyttsx3
import pyautogui
import time
import sys
import os

# Function to convert text to
# speech
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()



def modes(text, mode):

    # Verify modes commands
    if text == "print mode on":
        mode[0] = 1
        SpeakText("The program is printing, thanks for use!")

    if text == "print mode off":
        mode[0] = 0
        SpeakText("The program is not printing enymore, have a good day!")

    if text == "verbose mode on":
        mode[1] = 1
        SpeakText("Verbose mode Turned On!")

    if text == "verbose mode off":
        mode[1] = 0
        SpeakText("Verbose mode Turned Off!")

    if text == "open calculator":
        SpeakText("Opening calculator...")
        time.sleep(0.5)
        os.system("calc.exe")

    if text == "open draw":
        SpeakText("Opening mspaint...")
        time.sleep(0.5)
        SpeakText("Close mspaint to continue the program")
        os.system("mspaint.exe")

    if text == "open powershell":
        SpeakText("Opening powershell...")
        time.sleep(0.5)
        SpeakText("Close powershell to continue the program")
        os.system("start powershell.exe")

    return mode



def status(text, mode):

    if text == "print status":
        SpeakText("Print Status...")
        time.sleep(1)
        if mode[0] == 1:
            SpeakText("Printing is on.")
            SpeakText("Say: print mode off.")
            SpeakText("To stop the printing")

        elif mode[0] == 0:
            SpeakText("Printing is off.")
            SpeakText("Say print mode on.")
            SpeakText("To start the printing")

    if text == "verbose status":
        SpeakText("Verbose Status...")
        time.sleep(1)
        if mode[1]== 1:
            SpeakText("Verbose Mode On")
            SpeakText("Say Verbose Mode Off, to turn off the verbose mode")
        elif mode[1] == 0:
            SpeakText("Verbose Mode Off")
            SpeakText("Say Verbose Mode on, to turn on the verbose mode")



def run_speech(text, mode):
    if mode[0] == 1:
        pyautogui.write(text)

    if mode[1] == 1:
        SpeakText(text)


def voice_recon():
    MyText = "Sorry I cannot hear you"

    try:
        # use the microphone as source for input.
        with sr.Microphone() as source2:
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.5)

            # listens for the user's input
            audio2 = r.listen(source2)

            # Using google to recognize audio
            # And Writing the result as a text
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
        return MyText

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        # if verbose == 1:
        # SpeakText("Could not request results")
        return (MyText)

    except sr.UnknownValueError:
        print("unknown error occurred")
        # if verbose == 1:
        # SpeakText("error, please say again")
        return MyText



def Welcome(mode ):
    ## Welcome message
    SpeakText("WELCOME!")
    SpeakText("Starting the speech program, please wait a second.")

    time.sleep(1)

    status("print status", mode)
    status("verbose status", mode)

    time.sleep(1)
    SpeakText("Program started, thanks for using.")



def speech(mode):
    try:

        # Loop infinitely for user to
        # speak
        # Verifier
        # if the value is 1, the pharase will write as a keyboard
        # if the value is 0, The pharase dont will write

        if mode[0] == 1 or mode[0] == 0 and mode[1] == 1 or mode[1] == 0:

            ## Main Loop
            while(1):

                # Exception handling to handle
                # exceptions at the runtime
                try:

                    # Voice Reconnaissance
                    MyText = voice_recon()


                    ## Main Functions
                    modes(MyText, mode)
                    status(MyText, mode)
                    run_speech(MyText, mode)

                except Exception as e:
                    print(e)


        else:
            text = "Error, please verify the mode arguments"
            SpeakText(text + "," + mode)
            print(text, mode)

    except Exception as e:
        print(e)





if __name__ == "__main__":
    # Initialize the recognizer
    r = sr.Recognizer()
    mode = [0, 1]

    if len(sys.argv) <= 3:
        speech(mode)
    else:
        # Verify verbose arg
        if sys.argv[1] == "--verbose-on" or sys.argv[2] == "--verbose-on" or sys.argv[3] == "--verbose-on":
            mode[1] = 1
        elif sys.argv[1] == "--verbose-off" or sys.argv[2] == "--verbose-off" or sys.argv[2] == "--verbose-off":
            mode[1] = 0

        # Verify print arg
        if sys.argv[1] == "--print-on" or sys.argv[2] == "--print-on" or sys.argv[3] == "--print-on":
            mode[0] = 1
        elif sys.argv[1] == "--print-off" or sys.argv[2] == "--print-off" or sys.argv[3] == "--print-off":
            mode[0] = 0

        if sys.argv[1] == "--welcome-on" or sys.argv[2] == "--welcome-on" or sys.argv[3] == "--welcome-on":
            Welcome(mode)
            speech(mode)

