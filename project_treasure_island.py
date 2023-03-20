print('''
*******************************************************************************
                                 # #  ( )
                                  ___#_#___|__
                              _  |____________|  _
                       _=====| | |            | | |==== _
                 =====| |.---------------------------. | |====
   <--------------------'   .  .  .  .  .  .  .  .   '--------------/
     \                                                             /
      \_______________________________________________WWS_________/
  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
   wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
*******************************************************************************
''')


print("Welcome to BattleShip Journey.")
print("Your mission is to find the Treasure Island.")
quiz = input("You are going to the Tresure Island. Select destination left or right\n").lower()
if quiz == "left":
  quiz2 = input("You met monster! choose your action swim or fight\n").lower()
  if quiz2 == "fight":
    quiz3 = input('Choose your destination river,ocean and valley.\n').lower()
    if quiz3 == "river":
      print("You Died! Game Over.")
    elif quiz3 == "ocean":
      print("Finally, you find Tresure Island!!")
    elif quiz3 == "vally":
      print("You Died! Game Over.")
    else:
      print("You Died! Game Over.")
  else:
    print("You Died! Game Over.")
  
else:
  print("You Died! Game Over.")
