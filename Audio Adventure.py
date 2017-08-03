
over = False
while over == False:
    print("You wake up in the middle of nowhere, and are unable to recognize your surroundings. You hear birds chirping and the wind blowing through trees. You stand up determined to find out where you are.“Fellow wanderer, you seem lost in the wilderness. Let me guide you through this journey. You must show compassion in order to survive this first trial. Who are you? You ask. No answer.You hear a bird chirping. But birds live in trees. Why is the sound beneath you? You feel the ground around your feet, and your fingers run across something soft.“Bring the bird to the nearby town. Someone can help you there,” the wind seemed to sayI have to help this bird. This is my only chance of getting out of this place.")
    d_one = input("Do you go left or right?: ")
    if d_one == "left":
        print("This is Yticat, a voice says. You hear footsteps walking away from you. You call for help. You say hey there! Please come here and have a look at this injured bird.")
        print("The voice says 'I was lookng for this bird! Thank you so much for bringing my fellow sorcerer back to me' And the sorcerer turns the bird into another sorcerer")
        d_two= input("Would you like to help us in our journey or want help in yours? ")
        if d_two == "left":
          d_three= input("You decide to help them and they require you to run a small errand for them. Do you want to do what they say or poliltely refuse and leave? ")
          if d_three == "left":
              print("You have proven that you are resilitant and the sorcerers were kind enough to let you go back home")
              over = True
          elif d_three == "right":
              d_five= input("You are alone and decide to explore which direction would you go to? ")
              if d_five == "left":
                  print("You reach a waterfall")
                  d_six = input("Do you want to swim or explore more?")
                  if d_six == "left":
                      print("You decided to swim and you ended up reaching a town where they welcomed you as a new resident. After a couple of days your family members bump into you while looking for you")
                      over = True
                  elif d_six == "right":
                      print("While walking away you slipped into the water and were washed into an unknown town. Luckily the friendly residents agreed to welcome you as a part of that town and allowed you to live there for the rest of your life")
                      over = True
              elif d_five == "right":
                  print("You ended up near a town and found your neighbors who happened to visit their relatives in that town. They took the responsibility to take you back home")
                  over = True
          elif d_two == "right":
              print("The sorcerers respect your decision and leave you with water, food and a dog")
              d_nine = input("The dog starts to run really quick. Do you chase the dog or leave her and try to find your way back on your own")
              if d_nine == "left":
                  print("You ran after the dog and eventually reach your home")
                  over = True
              elif d_nine == "right":
                  print("You run into a hunter on a horse back")
                  d_ten = input("You are extremely tired to walk. Do you ask for his horse or ask for directions to home?")
                  if d_ten == "left":
                      print("The hunter was offended but shows mercy on you. He decides to keep you as his sidekick for the rest of your life")
                      over = True
                  elif d_ten == "right":
                      print("You get the directions back home")
                      over = True
    elif d_one == "right":
        print("You reach an abandoned apothecary")
        d_seven = input("Do you wish to experiment to help the injured bird or explore more? ")
        if d_seven == "left":
              print("You accidentally drop a glass jar and the owner of the apothecary comes running towards you")
              d_eight = input("Do you lie to him about what you are doing or ask him to help you heal the bird? ")
              if d_eight == "left":
                  print("The owner catches that you are lying and decides to keep you with him to help him out with work")
                  over = True
              elif d_eight == "right":
                  print("The owner appreciates your honesty and heals the bird. The bird is a socrerer who appreciates ypur persistance and uses magic to find your way back home")
                  over = True
        elif d_seven == "right":
              d_eight = input("While exploring the area you run into thieves. You need to make a quick decision. Will you keep quiet and negotiage with the thieves or run and scream for help? ")
              if d_eight == "left":
                  print("The town sheriff comes along. Even though he knows you arent involved he is suspicious ad locks you up for a term.")
                  over = True
              elif d_eight == "right":
                  print("The sheriff was nearby and heard you scream. After dealing with the robbers he helped you find your home")
                  over = True
        
          
