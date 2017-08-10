#pip install playsound

import time

import winsound

from playsound import playsound
# playsound() #must be .wav


def opening():
    playsound('C:\Python36\wav\Prologue.wav') #Prologue
def start():
    playsound('C:\Python36\wav\Start.wav')

def makeChoice():

    choice = ""
    while choice != "f" and choice != "j":

        print("press f to choose option 1.")

        print("press j to choose option 2.")

        print("")

        choice = input(" > ")

        print("")

    return choice

def scene1A(): #start --> sorcerer
    playsound('C:\Python36\wav\Scene_1A.wav')

def scene1B(): #start --> apothecary
    playsound('C:\Python36\wav\Scene_1B.wav')

def scene2A(): #sorcerer --> help
    playsound('C:\Python36\wav\Scene_2A.wav')
    
def scene2B(): #sorcerer --> ignore
    playsound('C:\Python36\wav\Scene_2B.wav')

def sGoodEnd4(): #sorcerer --> ignore --> chase dog // end
    playsound('C:\Python36\wav\sGoodEnd4.wav')

def scene6A(): #sorcerer --> ignore --> don't chase dog & explore --> hunter
    playsound('C:\Python36\wav\Scene6A.wav')
    
def sBadEnd4(): #sorcerer --> ignore --> don't chase dog & explore --> hunter --> steal the horse // end
    playsound('C:\Python36\wav\sBadEnd4.wav')
    
def sGoodEnd5(): #sorcerer --> ignore --> don't chase dog & explore -_> hunter --> ask for directions // end
    playsound('C:\Python36\wav\sGoodEnd5.wav')
    
def sGoodEnd(): #sorcerer --> help --> agree // end
    playsound('C:\Python36\wav\sGoodEnd.wav')
    
def scene3B(): #sorcerer --> help --> decline
    playsound('C:\Python36\wav\scene3B.wav')
    
def scene4A(): #sorcerer --> help --> decline --> waterfall
    playsound('C:\Python36\wav\scene4A.wav')
    
def sGoodEnd1(): #sorcerer --> help --> decline --> waterfall --> swim // end
    playsound('C:\Python36\wav\sGoodEnd1.wav')
    
def sGoodEnd3(): #sorcerer --> help --> decline --> waterfall --> explore // end
    playsound('C:\Python36\wav\sGoodEnd3.wav')
    
def sGoodEnd2(): #sorcerer --> help --> decline --> town // end
    playsound('C:\Python36\wav\sGoodEnd2.wav')
    
def scene2C(): #apothecary --> experiment
    playsound('C:\Python36\wav\Scene2C.wav')

def scene2D(): #apothecary --> explore
    playsound('C:\Python36\wav\Scene2D.wav')
    
def aBadEnd(): #apothecary --> experiment --> run
    playsound('C:\Python36\wav\aBadEnd.wav')
    
def aGoodEnd(): #apothecary --> experiment --> stay and explain
    playsound('C:\Python36\wav\aGoodEnd.wav')
    
def aGoodEnd2(): #apothecary --> explore --> call for help
    playsound('C:\Python36\wav\aGoodEnd2.wav')
    
def aBadEnd2(): #apothecary --> explore --> don't call for help
    playsound('C:\Python36\wav\aBadEnd2.wav')


###############################################################################
opening()



playAgain = "yes"

while playAgain == "yes" or playAgain == "y":

    start()

    firstChoice = makeChoice() #start: left (sorcerer) or right (apothecary)

    if firstChoice == "f":

        scene1A() #start --> sorcerer ---------------------------------------------------------------------------------------------

        sChoice = makeChoice() #sorcerer: help or ignore

        if sChoice == "f":

            scene2A() #sorcerer --> help

            sChoice1 = makeChoice() #sorcerer: agree to help or decline to help

            if sChoice1 == "f":

                sGoodEnd() #sorcerer --> help --> agree to help // end

            else:

                scene3B() #sorcerer --> help --> decline to help

                sChoice2 = makeChoice() #sorcerer --> help --> decline: waterfall or town

                if sChoice2 == "f":

                    scene4A() #sorcerer --> help --> decline --> waterfall

                    sChoice3 = makeChoice() #sorcerer --> help --> decline --> waterfall: swim or explore

                    if sChoice3 == "f":

                        sGoodEnd1() #sorcerer --> help --> decline --> waterfall --> swim // end

                    else:

                        sGoodEnd3() #sorcerer --> help --> decline --> waterfall --> explore // end

                else:

                    sGoodEnd2() #sorcerer --> help --> decline --> town // end

        else:

            scene2B() #sorcerer --> ignore

            sChoice4 = makeChoice() #sorcerer --> ignore: chase dog or don't chase dog

            if sChoice4 == "f":

                sGoodEnd4() #sorcerer --> ignore --> chase dog // end

            else:

                scene6A() #sorcerer --> ignore --> don't chase dog 

                sChoice5 = makeChoice() #sorcerer --> ignore --> don't chase dog --> hunter: horse or directions

                if sChoice5 == "f":

                    sBadEnd3() #sorcerer --> ignore --> don't chase dog --> hunter --> horse // end

                else:

                    sGoodEnd5() #sorcerer --> ignore --> don't chase dog --> hunter --> directions // end

            

    else:

        scene1B() #start --> apothecary -------------------------------------------------------------------------------------------

        aChoice = makeChoice() #apothecary: experiment or explore

        if aChoice == "f":

            scene2C() #apothecary --> experiment

            aChoice1 = makeChoice() #apothecary --> experiment: run or stay and explain

            if aChoice1 == "f":

                aBadEnd() #apothecary --> experiment --> run // end

                #print("")

                #print("Do you want to play again? (yes or no)")

                #playAgain = input(" > ")

            else:

                aGoodEnd() #apothecary --> experiment --> stay and explain // end

                #print("")

                #print("Do you want to play again? (yes or no)")

                #playAgain = input(" > ")

        else:

            scene2D() #apothecary --> explore

            aChoice2 = makeChoice() #apothecary --> explore: call for help or don't call for help

            if aChoice2 == "f":

                aGoodEnd2() #apothecary --> explore --> call for help // end

                #print("")

                #print("Do you want to play again? (yes or no)")

                #playAgain = input(" > ")

            else:

                aBadEnd2() #apothecary --> explore --> don't call for help // end

                #print("")

                #print("Do you want to play again? (yes or no)")

                #playAgain = input(" > ")

        



    # # # # # # # # # # # # # # # # # # # # # # # 

        

   

    print("")

    print("Do you want to play again? (yes or no)")

    playAgain = input(" > ")

exit()
    
