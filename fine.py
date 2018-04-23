
# speech recognition

import speech_recognition as speech

#a lot of variables used for loops and conditions
voice = speech.Recognizer()
# Maintain status of each attempt. You can just use two variables successful_attempts and total_attempts also but status list might help you in maintaining more things like a list of tuples (color, result) etc
status = []
# successful_attempts, total_attempts = 0, 0

while True:
    #with microphone input as the input
    with speech.Microphone() as source:
        print("Say something!")

        #variable = the input from the microphone
        audio = voice.listen(source)
        voiceRecog = voice.recognize_google(audio)
        try:
            #print the word that was heard
            print("\nYou said: " + voiceRecog)
        except speech.UnknownValueError:


            #if couldnt recognise then print this msg
            print("Sorry, we couldn't make that out. Try again!")

        except speech.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


        #list of commands  for comparing   
        words = ["add", "division", "multiply"]

        if "quit" in voiceRecog:
            break
        elif voiceRecog in words:
            status.append(1)
            # successful_attempts += 1
            print("\nCommand Found!\n")
        else:
            status.append(0)
            print("\nCommand not found!\n\n")

        # total_attempts += 1

#once loop exited by saying quit, print attempts and successful attempts
print("\nYou checked for", len(status), "commands and had", sum(status), "successful attempts")
#print("\nYou checked for", total_attempts, "commands and had", successful_attempts, "successful attempts")
