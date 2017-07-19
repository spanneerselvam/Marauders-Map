print("Messers Moony, Wormtail, Padfoot, and Prongs")
print("Are Proud to Present: The Marauders Map")
print()
print("You are fortunate enough to stuble upon this map. Press 'Enter' to continue.")
input()
name = input("Enter your name: ")
input2 = input("Enter your house (gryffindor, ravenclaw, hufflepuff, slytherin): ")
if input2 == "gryffindor":
  print("Ahh, a fellow gryffindor! The best house in Hogwarts and where the brave at heart dwell! Welcome {}!".format(name))
  print("Enjoy and remember when your done to give it a tap and say 'Mischief Managed' otherwise anyone can read it!")
  print("Cheers, Mates!")
if input2 == "ravenclaw":
  print("Oh look what we have here, a snobby Ravenclaw... Praised for your cleverness and wit... Hahaha.")
  print("Mr. Padfoot wonders if you are all so clever then why was that prat Gilderoy Lockhart a Ravenclaw.")
  print("Mr. Prongs agrees with Padfoot and believes that you should go on and read a book instead.")
if input2 == "hufflepuff":
  print("Congratulations {}!".format(name))
  print("You have come across the mobile version of 'Hogwarts, A History' by Bathilda Bagshot. This is a book concerning Hogwarts School of Witchcraft and Wizardry and its history. Enjoy at your pleasure.")
if input2 == "slytherin":
  print("Mr. Moony presents his compliments to {} and begs {} to keep their abnormally large nose out of other people's business".format(name))
  print("Mr. Prongs agrees with Mr. Moony and would like to add that {} is an ugly git".format(name))
  print("Mr. Padfoot would like to register his astonishment that an idiot like that was even accepted to Hogwarts")
  print("Mr. Wormtail bids {} good day, and advises {}} to wash their hair, the slime-ball".format(name))
