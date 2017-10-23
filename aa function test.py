# Adventure game code re-write.
# < < https://coderdojoathenry.org/category/python-beginners/page/2/ > > #

import time

def opening():
    print("Darkness, darkness, nothing but darkness.")
    time.sleep(2)
    print("That's the world you've always known; that's the world you've always been in.")
    time.sleep(2)
    print("Even now.")
    time.sleep(1)
    print("Even today.")
    time.sleep(1)
    print("It even feels like nothing.")
    time.sleep(2)
    print("There's nothing around you.")
    time.sleep(2)
    print("There's no one around you.")
    time.sleep(2)
    print("It's just darkness, and darkness forever more.")
    time.sleep(2)
    print("You wonder about the world.")
    time.sleep(2)
    print("And in turn, the world wonders about you.")
    print("")
    time.sleep(3)
    print("'Who are you? Why are you here?' The silence seems to ask.")
    time.sleep(2)
    print("You realize you have no answer.")
    time.sleep(2)
    print("You know nothing about yourself.")
    time.sleep(2)
    print("The only reminder that you're alive, is the dull throb in the back of your skull.")
    print("")
    print("")
    time.sleep(3)
    print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("")

def start():
    print("You are in the middle of nowhere, and you are unable to recognize your surroundings.")
    print("")
    print("Suddenly, you hear a voice from within the trees:")
    print("")
    print("'Fellow wanderer, you seem lost in the wilderness. Let me guide you through this journey.")
    print("You must show compassion in order to survive this first trial.'")
    print("")
    print("'Who are you?' you ask. No answer. It figures -- trees don't talk.")
    print("")
    print("You hear a bird chirping. But... birds live in trees. Why is the sound beneath you?")
    print("You feel the ground around your feet, and your fingers run across something soft.")
    print("")
    print("'Bring the bird to the nearby town. Someone can help you there,' the voice seemed to say.")
    print("")
    print("*I have to help this bird. This is my only chance of getting out of this place.*")
    print("")
    print("Option 1: go left.")
    print("Option 2: go right.")
    print("")
    

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
    print("A shift in the wind reveals the tantalizing aroma of fresh bread.")
    print("You wonder how long it's been since you've eaten.")
    print("*But I can't worry about that now. I have something I need to do.*")
    print("")
    print("You follow the scent of bread on the wind, cradling the fallen bird in your hands.")
    print("The texture of the ground changes from dirt and leaves, to a paved path.")
    print("*That's good. There must be people nearby.*")
    print("")
    print("A hand falls on your shoulder abruptly, stopping you in your tracks.")
    print("")
    print("'Pardon me, traveler, but can I trouble you with a small task?")
    print("I need someone nimle like you to help me out,' a new voice asks.")
    print("It's not one you recognize, but it sounds friendly enough.")
    print("")
    print("Option 1: help the stranger.")
    print("Option 2: ignore the stranger.")
    print("")
          
def scene1B(): #start --> apothecary
    print("You cup the injured bird in your hands and head towards the sound of a drum beating in the distance.")
    print("The crunch of leaves underfoot gives way to a cobblestone path.")
    print("You hear the chatter of townspeople around you, the creaking of wooden wagon wheels and doors.")
    print("The smell of herbs and medicine lace the air.")
    print("*There has to be an apothecary here.*")
    print("")
    print("With outstretched hands, you find a wooden wall. A door.")
    print("You turn the handle, and you are overwhelmed by the mixed aromas of herbs that fill the space.")
    print("*I can either look for someone, or I can try to figure this out myself.")
    print("But it has to be quick... I don't know how much time I -- we -- have left.*")
    print("")
    print("Option 1: experiment with the strange medicines.")
    print("Option 2: look for someone who knows what to do.")
    print("")

def scene2A(): #sorcerer --> help
    print("*If I want any shot at getting this bird help, I'm going to have to make friends. What do I have to lose, anyway?*")
    print("")
    print("'What can I do for you?'")
    print("'Oh, bless your soul. I just need you to pick some herbs for me. From my garden")
    print("It's easy -- I'll show you the way.")
    print("Please... it's important.'")
    print("")
    print("Option 1: agree.")
    print("Option 2: decline.")
    print("")

def scene2B(): #sorcerer --> ignore
    print("You remind yourself that your objective is to find yourself, not make friends. So you politely refuse to assist the stranger.")
    print("Your conscience isn't at peace, but you focus on the insignificance of the herb in the long run.")
    print("")
    print("You begin to resume your journey...")
    print("When all of a sudden, you hear the stranger's voice once more:")
    print("'Wait, I have a friend that might be able to help you in your journey -- my dog.'")
    print("")
    print("You bend down to pet the dog.")
    print("You feel good about your journey now.")
    print("The dog playfully licks your hand, as if in agreement.")
    print("")
    print("After following the sound of the tiny footsteps for somettime, you notice that the footsteps are growing increasingly quick.")
    print("You try to walk as fast as the dog, but you fear that you'll lose him.")
    print("You have to make a decision.")
    print("")
    print("Option 1: chase the dog.")
    print("Option 2: don't chase the dog.")
    print("")

def sGoodEnd4(): #sorcerer --> ignore --> chase dog // end
    print("You decide to chase after the dog.")
    print("As you run, you feel the texture of the ground change beneath your feet.")
    print("The tender earth solidifies into stone. Your footstesps led you to a paved path.")
    print("A strange sound approaches. It takes you a moment to realize that it's the clop of hooves.")
    print("")
    print("*Horses. People.*")
    print("You call out for help. A familiar one answers.")
    print("It's your brother.")
    print("")
    print("You've found home.")
    print("")

def scene6A(): #sorcerer --> ignore --> don't chase dog & explore --> hunter
    print("You choose to let the dog go.")
    print("As you blindly wander the path before you, you wonder if you made the best decision.")
    print("You are lost, and you are lonely.")
    print("Though your body keeps trudging on, your mind is elsewhere.")
    print("")
    print("You are brought back to reality by the sound of an arrow zipping past your ear.")
    print("'Who goes there?' You try to keep your voice steady.")
    print("'I do. And I was not aiming for you. There's a deer behind you, you know. There was.'")
    print("'Who are you?'")
    print("'I am Me.'")
    print("'Oh,' you say softly, secretly fearing that this stranger is a wiseguy in disguise.")
    print("")
    print("You hear something nicker nearby.")
    print("*A horse? Oh, of course -- he's a hunter. He has to get around somehow.*")
    print("You realize that if you let your morals to go naught, you could ride the horse into town in minutes.")
    print("But in doing so, you're risking any help you can potentially gain by befriending the stranger.")
    print("")
    print("Option 1: steal the horse.")
    print("Option 2: ask for directions.")
    print("")

def sBadEnd4(): #sorcerer --> ignore --> don't chase dog & explore --> hunter --> steal the horse // end
    print("*It's every man for himself in this world. I just have to do it.*")

def sGoodEnd5(): #sorcerer --> ignore --> don't chase dog & explore -_> hunter --> ask for directions // end
    print(" < < debug: find hunter, ask for directions > >")    

def sGoodEnd(): #sorcerer --> help --> agree // end
    print("'Of course. I just...' you stroke the bird in your hands. *It's still breathing.*")
    print("")
    print("'Don't worry. I will help your friend, in exchange for your help. I will be careful.'")
    print("The same hand brushes yours, delicately cupping the small bird and gently lifting it out of your hands.")
    print("")
    print("'Reach in front of you. Feel that fence? Just follow it to the end. There will be a tree there.")
    print("Feel for the cavity in the trunk. There's a small plant growing there. I just need one of its leaves.'")
    print("")
    print("'Consider it done,' you say with a renewed sense of purpose.")
    print("You follow the stranger's instructions exactly. You find the tree; you find the plant; you retrace your steps with the jagged leaf in hand.")
    print("")
    print("'I see you found what you've been looking for,' a new voice says.")
    print("'What... do you mean?'")
    print("Laughter. 'The plant, kid. It's magic. It grants wishes.'")
    print("'I don't understand'")
    print("'I had a feeling. Use it to get yourself home.'")
    print("'But how?'")
    print("'Just believe, kid. Just believe. As I did in you.")
    print("Everything is going to be just fine.'")
    print("'Thank you.'")
    print("You smile and close your eyes.")
    print("")
    
def scene3B(): #sorcerer --> help --> decline
    print(" < < debug: decline to help sorcerer > >")

def scene4A(): #sorcerer --> help --> decline --> waterfall
    print(" < < debug: decline to help sorcerer, find waterfall > > ")

def sGoodEnd1(): #sorcerer --> help --> decline --> waterfall --> swim // end
    print(" < < debug: find waterfall, swim > >")

def sGoodEnd3(): #sorcerer --> help --> decline --> waterfall --> explore // end
    print(" < < debug: find waterfall, explore > >")

def sGoodEnd2(): #sorcerer --> help --> decline --> town // end
    print(" < < debug: decline to help sorcerer, find town > >")


def scene2C(): #apothecary --> experiment
    print("*I can do this myself. I never needed help, anyway.*")
    print("You locate a table. A small glass bottle.")
    print("You gently uncork it.")
    print("")
    print("'Just what do you think you're doing here?' a voice from behind you queries.'")
    print("")
    print("Option 1: run.")
    print("Option 2: stay and explain.")
    print("")

def scene2D(): #apothecary --> explore
    print("*Okay. For safety's sake, I'm going to look for someone who knows what they're doing.*")
    print("")
    print("You hear rustling from the opposite side of the room.")
    print("You approach it tentatively.")
    print("")
    print("'Stay back if you don't want to get hurt!' someone cries.")
    print("")
    print("Option 1: call for help.")
    print("Option 2: don't call for help.")
    print("")

def aBadEnd(): #apothecary --> experiment --> run
    print("You do the easy thing: you run.")
    print("But you don't make it very far before an iron grip clasps your arm and stops you in your tracks.")
    print("")
    print("'Oh, so you're a frisky one, eh?' she sneers.")
    print("")
    print("You're breathing heavily.")
    print("'I... it's--'")
    print("You open your hands to reveal the small bird resting in your palms.")
    print("")
    print("She sights. 'You don't look like you're from around here, kid. You look like you've been roughed up some.")
    print("...tell you what, I'll let you off easy this time. I'll help you and your feathered friend.")
    print("But you're gonna have to stay here and learn how to appreciate the art of medicine.")
    print("Oh, and maybe learning a thing or two about common sense. Like, y'know, knocking before you barge into someone's house.'")
    print("")
    print("You have nothing to say. So you nod your head silently and accept your fate.")
    print("")

def aGoodEnd(): #apothecary --> experiment --> stay and explain
    print("'W-wait, ma'am. I... I can explain this,' you stutter.")
    print("")
    print("She sighs. 'That's what they all say, kiddo. This better be good.")
    print("")
    print("You open your palms to reveal the small bird resting within them.")
    print("'He's hurt.'")
    print("'I can see that.' She's not impressed.")
    print("'Well, I can't. I just... want to help him. Please.")
    print("Maybe you can help him. Ma'am.'")
    print("")
    print("Someone is laughing. You are confused.")
    print("")
    print("'Good show, good show. You can stop pretending now, Avian.")
    print("Come on our and help the pour soul.'")
    print("'Aw, but I was having fun,' says a new voice, seemingly from the creature in your hands.")
    print("You feel the tickle of feathers brushing across your palms. A new presence stands before you.")
    print("")
    print("'Hello, traveler. I am Avian, the enchantress.")
    print("I am impressed your act of compassion and bravery. You were ready to sacrifice yourself to help me,")
    print("when you yourself were suffering. For that, I think you deserve a reward.")
    print("How can I serve you?'")
    print("")
    print("'I just want to go home,' you say.")
    print("")
    print("'Very well. Once you open your eyes, your wish will be granted.")
    print("You will be returned to the world from whence you came.'")
    print("")
    print("'Thank you.'")
    print("'No, thank /you./'")
    print("")
    

def aGoodEnd2(): #apothecary --> explore --> call for help
    print("'Who are you, and what are you doing here?' you yell.")
    print("")
    print("'Who are *you*? You better pipe down if you want to stay out of this.'")
    print("")
    print("'I'm not just going to let you get away with... whatever you're doing. I don't feel good about that.'")
    print("")
    print("'Oh, phooey. You're gonan think twice next time!'")
    print("Something thuds to the floor.")
    print("Heavy footsteps draw closer.")
    print("")
    print("'Someone, stop them!' you yell.")
    print("'You stop!' they yell.")
    print("'Everyone, STOP!' yells a new voice.")
    print("The footsteps stop. You feel sick.")
    print("")
    print("'Now, who's going to explain what's going on in here?'")
    print("'They're--'")
    print("'Yeah, I can see that, smart one. Y'all better come with me. You have the right to remain--'")
    print("'One minute. Please. I'm not even supposed to be here.'")
    print("'That's what they all say, kiddo.'")
    print("'Please, just listen to me. Look -- I just want to go home.'")
    print("'You're there already,' she says slowly.")
    print("'No... I'm not. I don't know who I am. I-- I don't know why I'm here.'")
    print("'Just come with me, kid. We'll get this all sorted out. If what you say is true, I'll get you home myself.")
    print("Trust me. Everything is going to be okay.'")
    print("")

def aBadEnd2(): #apothecary --> explore --> don't call for help
    print("'Oh,' you say softly, and back away.")
    print("But you back into something else --")
    print("No, someone else.")
    print("")
    print("'Where do you think you're going?'")
    print("'I, uh--'")
    print("'That goes for everyone. Everyone FREEZE!'")
    print("'Whoa, whoa, whoa. Okay. I'm not guilty. I swear. I was just passing by.'")
    print("'Then what's that in your hand?'")
    print("")
    print("You stop cold. It's the glass bottle.")
    print("")
    print("'You have the right to remain silent,' the voice says.")
    print("'This can't be happening,' you breathe. 'I just... want to go home.'")
    print("")
    print("'That's what they all say, kid. Don't sweat it. You'll get used to your new home in no time.")
    print("They all do.")
    print("")



    
 
#Program begins here: // sChoice = sorcerer, aChoice = apothecary // s = A, B // a = C, D -----------------------------------------###

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
