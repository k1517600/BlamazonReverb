import random
from dfmanager import detect_intent

from voiceinterface import listen, speak

manual_input = False


def await_activation():
    if manual_input:
        words_spoken = input("Speak for me, my child: ")
    else:
        words_spoken = listen()
    if words_spoken.lower().count("alex") > 0:
        speak("Yes?")
        input_words()


def input_words():
    if manual_input:
        input_text = input("Now, what is it that you desire?")
    else:
        input_text = listen()
    result = detect_intent(sessionID, input_text)
    speak(result[0])
    if result[1]:
        input_words()


if __name__ == "__main__":
    while True:
        sessionID = random.randint(0, 100000)
        await_activation()