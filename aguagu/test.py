import speech_recognition as speech_recog
import random 
import time

levels = {

    "easy": ["dairy", "mouse", "computer"],

    "medium": ["programming", "algorithm", "developer"],

    "hard": ["neural network", "machine learning", "artificial intelligence"]

}





def play_game(level, tryi = 1):
    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()
    points = 0
    right = []
    lis = levels[level]
    with mic as audio_file:
        print("level ", level)
        for i in range(len(levels[level])):
            word = lis[random.randint(1, len(lis)) -1 ]
            print("say ", word )
            lis.remove(word)
            g = 0
            while g != tryi:
                recog.adjust_for_ambient_noise(audio_file)
                audio = recog.listen(audio_file)
                try:
                    name = recog.recognize_google(audio, language="en-EN")
                except:
                    return "None"
                print(name)
                if recog.recognize_google(audio, language="en-EN") == word: 
                    points += 1
                    right.append(i + 1)
                    break
                else:
                    if g + 1 != tryi:
                        print("next try")
                    g += 1
        print("Ваш счет: ", points)
        print("вы угадали: ", right, " слова" )
  

play_game("easy", 2)
         


   
