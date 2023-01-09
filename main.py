import random

def affiche_morpion(x):
  i = 0
  print("#"*20,)
  while i < 9:
    print(x[i],"|",x[i+1],"|",x[i+2])
    if i < 6:
      print("-"*10)
    i = i + 3
  print("#"*20,)

'''
si return = 1 alors X a gagné
si return = 2 alors Y a gagné
'''

def verifwinH(x):
  i = 0
  while i < 9:
    if x[i] == x[i+1] == x[i+2]:
      if x[i] == "X":
        return 1
      elif x[i] == "O":
        return 2
    i = i + 3

def verifwinV(x):
  i = 0
  while i < 3:
    if x[i] == x[i+3] == x[i+6]:
      if x[i] == "X":
        return 1
      elif x[i] == "O":
        return 2
    i = i + 1

def verifwinD(x):
  if x[0] == x[4] == x[8]:
    if x[0] == "X":
      return 1
    elif x[0] == "O":
      return 2
  elif x[2] == x[4] == x[6]:
    if x[2] == "X":
      return 1
    elif x[2] == "O":
      return 2
    
def verifwin(x):
  if verifwinH(x) == 1 or verifwinH(x) == 2:
    if verifwinH(x) == 1:
      return 1
    else:
      return 2
  elif verifwinV(x) == 1 or verifwinV(x) == 2:
    if verifwinV(x) == 1:
       return 1
    else:
      return 2
  elif verifwinD(x) == 1 or verifwinD(x) == 2:
    if verifwinD(x) == 1:
      return 1
    else:
      return 2
  return 0

def qui_commence():
  print("1 = le joueur X commence")
  print("2 = le joueur O commence")
  statut = True
  while statut:
    x = int(input(" : "))
    if x == 1: 
      print("le joueur XXXXXX commence\n")
      statut = False

    elif x == 2:
      print("le joueur OOOOOOO commence\n")
      statut = False
  return x

def choix_possible():
  affiche_morpion(morption_exemple)
  print("Choissisez votre case selon les numéros")
  x = int(input(" : "))
  return x
  
#####################################################################

i_round = 0

morpion = ["-"]*9
morption_exemple = [0,1,2,3,4,5,6,7,8]

print(" NOUVELLE PARTIE !!!\n")
affiche_morpion(morpion)

joueurX = True
joueurO = True


start = qui_commence()

while joueurX and joueurO and i_round <9:
  
  while start == 1 :
    print("C LE TOUR DU JOUEUR XXXXXXX")
    choix = choix_possible()
    if choix <9 and choix >=0:
      if morpion[choix] == "X" or morpion[choix] == "O":
        print("cette case est déja prise")
      else : 
        morpion[choix] = "X"
        affiche_morpion(morpion)
        start = 2
        i_round = i_round + 1

  if verifwin(morpion) == 1:
    print("LE JOUEUR X A GAGNEEEE","#"*20)
    joueurO = False
    start = 3
  elif verifwin(morpion) == 2:
    print("LE JOUEUR O A GAGNEEEE","#"*20)
    joueurX = False
    start = 3
  
  while start == 2 :
    print("C LE TOUR DU JOUEUR OOOOOOO")
    choix = choix_possible()
    if choix <9 and choix >=0:
      if morpion[choix] == "X" or morpion[choix] == "O":
        print("cette case est déja prise")
      else : 
        morpion[choix] = "O"
        affiche_morpion(morpion)
        start = 1
        i_round = i_round + 1


  if verifwin(morpion) == 1 and start != 3:
    print("LE JOUEUR X A GAGNEEEE","#"*20)
    joueurO = False
  elif verifwin(morpion) == 2 and start != 3:
    print("LE JOUEUR O A GAGNEEEE","#"*20)
    joueurX = False



if i_round == 9 and verifwin(morpion) == 0:
  print("égalité :(((((((((")

