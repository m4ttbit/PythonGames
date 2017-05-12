import time
import random

def menu(): # menu of game options
  print()
  print('What would you like to do, ' + myName + '?')
  print()
  print('1 - Guess the Number\n2 - Tell Me a Joke')

  select = str(input('>> '))

  if select == "1":
    guessgame()

  elif select == "2":
    joke()

  else:
    print()
    print("You didn't pick a number from the list. Try again.")
    menu()

def guessgame(): # This is a simple guess the number game.
  guessesTaken = 0

  number = random.randint(1, 20)
  print()
  print('Well, ' + myName + ", I'm thinking of a number between 1 and 20.\nI'll give you 5 guesses.")

  for guessesTaken in range(5):
    print('Take a guess.')
    guess = input('>> ')
    guess = int(guess)
      
    if guess < number:
      print()
      print('Your guess is too low.')
        
    if guess > number:
      print()
      print('Your guess is too high.')
          
    if guess == number:
      break
  
  if guess == number:
    guessesTotal = str(guessesTaken + 1)
    print()
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTotal + ' guesses!')
  
  if guess != number:
    stateNumber = str(number)
    print()
    print('Nope. The number I was thinking of was ' + stateNumber + '.')
  
  print("Do you want to play again?\n'Y' or 'N'")
  again = str(input('>> '))
  again = again.upper()
  
  if again == "Y":
    guessgame()
  
  else:
    menu()
  
def joke():
  funny = random.randint(1, 10)

  if funny == 1:
    print()
    print("What do you call an old snowman?")
    input("Press 'Enter' to find out.")
    print()
    print('Water!')
    print()
    print("Want another joke? 'Y' or 'N'")
    anotherJoke = str(input('>> '))
    anotherJoke = anotherJoke.upper()
    
    if anotherJoke == "Y":
      joke()
    
    else:
      menu()
      
  if funny == 2:
    print()
    print("Where do pencils go for vacation?")
    input("Press 'Enter' to find out.")
    print()
    print('Pencil-vania!')
    print()
    print("Want another joke? 'Y' or 'N'")
    anotherJoke = str(input('>> '))
    anotherJoke = anotherJoke.upper()
    
    if anotherJoke == "Y":
      joke()
    
    else:
      menu()

  if funny == 3:
    print()
    print("How do you make a tissue dance?")
    input("Press 'Enter' to find out.")
    print()
    print('You put a little boogie in it!')
    print()
    print("Want another joke? 'Y' or 'N'")
    anotherJoke = str(input('>> '))
    anotherJoke = anotherJoke.upper()
    
    if anotherJoke == "Y":
      joke()
    
    else:
      menu()

  if funny == 4:
    print()
    print("Which dinosaur knew the most words?")
    input("Press 'Enter' to find out.")
    print()
    print('The thesaurus!')
    print()
    print("Want another joke? 'Y' or 'N'")
    anotherJoke = str(input('>> '))
    anotherJoke = anotherJoke.upper()
    
    if anotherJoke == "Y":
      joke()
    
    else:
      menu()

  if funny == 5:
    print()
    print("How do you know when the moon has had enough to eat?")
    input("Press 'Enter' to find out.")
    print()
    print("When it's full!")
    print()
    print("Want another joke? 'Y' or 'N'")
    anotherJoke = str(input('>> '))
    anotherJoke = anotherJoke.upper()
    
    if anotherJoke == "Y":
      joke()
    
    else:
      menu()

  if funny == 6:
    print()
    print("Why did the cow become an astronaut?")
    input("Press 'Enter' to find out.")
    print()
    print("To visit the Milky Way!")
    print()
    print("Want another joke? 'Y' or 'N'")
    anotherJoke = str(input('>> '))
    anotherJoke = anotherJoke.upper()
    
    if anotherJoke == "Y":
      joke()
    
    else:
      menu()

  if funny == 7:
    print()
    print("Who comes to a picnic but is never invited?")
    input("Press 'Enter' to find out.")
    print()
    print("Ants.")
    print()
    print("Want another joke? 'Y' or 'N'")
    anotherJoke = str(input('>> '))
    anotherJoke = anotherJoke.upper()
    
    if anotherJoke == "Y":
      joke()
    
    else:
      menu()

  if funny == 8:
    print()
    print("Why did the banana go to the doctor?")
    input("Press 'Enter' to find out.")
    print()
    print("Because it wasn't peeling well!")
    print()
    print("Want another joke? 'Y' or 'N'")
    anotherJoke = str(input('>> '))
    anotherJoke = anotherJoke.upper()
    
    if anotherJoke == "Y":
      joke()
    
    else:
      menu()

  if funny == 9:
    print()
    print("Why was Cinderella not very good at basketball?")
    input("Press 'Enter' to find out.")
    print()
    print("She always ran away from the ball!")
    print()
    print("Want another joke? 'Y' or 'N'")
    anotherJoke = str(input('>> '))
    anotherJoke = anotherJoke.upper()
    
    if anotherJoke == "Y":
      joke()
    
    else:
      menu()
      
  if funny == 10:
    print()
    print("Why was the math book sad?")
    input("Press 'Enter' to find out.")
    print()
    print("It had too many problems!")
    print()
    print("Want another joke? 'Y' or 'N'")
    anotherJoke = str(input('>> '))
    anotherJoke = anotherJoke.upper()
    
    if anotherJoke == "Y":
      joke()
    
    else:
      menu()

print("Hi! What's your name?")
myName = str(input('>> '))
print('Great to meet you, ' + myName +". My name's m4tt.")
time.sleep(1.5)
print()
print('Let's play a game!')
menu()