# imports go before everything
import random
import time

class Player():
    notepad = {}
    def __init__(self):
        self.notepad = {'Suspects' : '', 'Weapons' : '', 'Rooms' : ''}  

p1 = Player()

class ClueGame(Player):
    suspects = []
    weapons = []
    rooms = []
    answer = {}
    turn = 0
    players = []
    answerList = []

    def __init__(self):
        self.suspects = ['Mrs. White', 'Mrs. Peacock', 'Professor Plum', 'Colonel Mustard', 'Miss Scarlett', 'Reverend Green', 'Mr. Boddy']
        self.weapons = ['Knife', 'Revolver', 'Rope', 'Wrench', 'Candlestick', 'Lead pipe']
        self.rooms = ['Ballroom', 'Billiard Room', 'Conservatory', 'Dining Room', 'Hall', 'Kitchen','Lounge', 'Library', 'Study']
        self.answer = {'Suspect': self.suspects.pop(random.randrange(0,len(self.suspects))), 'Weapon': self.weapons.pop(random.randrange(0,len(self.weapons))), 'Room': self.rooms.pop(random.randrange(0,len(self.rooms)))}
        self.foundRoom = ("")
        self.foundSuspect = ("")
        self.foundWeapon = ("")
        

    def showAnswer(self):
        print(self.answer)
        
    def checkGuess(self):

        print("Guess the Killer! It can be Mrs. White, Mrs. Peacock, Professor Plum, Colonel Mustard, Miss Scarlett, Reverend Green, or Mr. Boddy")

        suspectGuess = input()
        if suspectGuess == self.answer['Suspect']:
            self.answerList.append(True)
        print(self.answerList)
        print("Guess the Weapon! It can be Knife, Revolver, Rope, Wrench, Candlestick, or Lead pipe")
        weaponGuess = input()
        if weaponGuess == self.answer['Weapon']:
            self.answerList.append(True)
        print(self.answerList)
        print("Guess the Room! It can be Ballroom, Billiard Room, Conservatory, Dining Room, Hall, Kitchen, Lounge, Library, or Study")
        suspectGuess = input()
        if suspectGuess == self.answer['Room']:
            self.answerList.append(True)
        print(self.answerList)

        if self.answerList == [True, True, True]:
            print("Congratulations you won!")
            quit
        else:
            print("You lost! You were imprisoned and died. Correct Answers were:")
            print(self.answer)
            quit

        self.answerList.clear

    def initialize(self):
        print("Welcome to the Clue Game!")
        time.sleep(1)

    def findWeapon(self):
        self.foundWeapon = self.weapons.pop(random.randrange(0,len(self.weapons)))
        print("You have found a " + self.foundWeapon)
        p1.notepad.update({'Weapons' : p1.notepad['Weapons'] + self.foundWeapon + ", "})
        time.sleep(1)
        print(self.foundWeapon + " has been added to notepad")
    
    def findSuspect(self):
        self.foundSuspect = self.suspects.pop(random.randrange(0,len(self.suspects)))
        print("You have found " + self.foundSuspect)
        p1.notepad.update({'Suspects' : p1.notepad['Suspects'] + self.foundSuspect + ", " })
        time.sleep(1)
        print(self.foundSuspect + " has been added to notepad")

    def findRoom(self):
        self.foundRoom = self.rooms.pop(random.randrange(0,len(self.rooms)))
        print("You have found yourself inside the " + self.foundRoom)
        p1.notepad.update({'Rooms' : p1.notepad['Rooms'] + self.foundRoom + ", "})
        time.sleep(1)
        print(self.foundRoom + " has been added to notepad")
    
    def timeOut(self):
        if self.answerList != [True, True, True]:
            self.turn+=1
        
        if self.turn == 2000:
            print("Time ran out. You were falsely imprisoned.")
            print("Correct answers were: " + self.answer)
            quit

    def gameMenu(self):
        print('-'*100) 
        print("It was a dark and stormy night.")
        time.sleep(1)
        print('-'*100)
        print("Mr. de Broglie was hosting a gala, but he was not celebrating with the guests.")
        time.sleep(3)
        print('-'*100)
        print("He was rushing around, working on his little imaginary spheres.")
        time.sleep(3)
        print('-'*100)
        print("Suddenly, as midnight struck, a bolt of lightning did as well. The lights instantly went out.")
        time.sleep(4)
        print('-'*100)
        print("Once you lit a candle, Mr. Broglie's body was not 10 feet away from where you stood!")
        time.sleep(5)
        print('-'*100)
        print('His butler came to you. "Did you do this?"')
        time.sleep(3)
        print('-'*100)
        print("You responded no. He did not believe you.")
        time.sleep(2)
        print('-'*100)
        print('"The police will be here in 2 minutes. If you cannot identify the murderer by the time they arrive, you are dead."')
        time.sleep(5)
        print('-'*100)
        print("The killer has already exited the building with the murder weapon.")
        time.sleep(1)
        print('-'*100)
        print("Travel around the mansion to cross off the suspects, weapons, and rooms.")
        print("Correctly guess all 3. Or else. Good luck!                                                                                              Also capitalization and punctuation (if theres a title like Mr.) has to be correct otherwise the guess is wrong")
        time.sleep(2)
        print('-'*100)
        self.findWeapon()
        self.findSuspect()
        self.findRoom()
        print("You are currently in the " + self.foundRoom + " holding a " + self.foundWeapon)
        time.sleep(1)
        print('-'*100)
        while self.answerList != [True, True, True]:
            self.timeOut
            print(self.turn)
            print("Press 1 to check notepad. Press 2 to find a random weapon, suspect, and room. Press 3 to check your guess and avoid being falsely imprisoned!")
            self.playerInput = input()
            if self.playerInput == "1":
                print(p1.notepad)
                continue
            if self.playerInput == "2":
                self.findWeapon()
                self.findSuspect()
                self.findRoom()
                continue
            if self.playerInput == "3":
                self.checkGuess()
                continue
            
        
        time.sleep(2)

game = ClueGame()

game.initialize()
game.gameMenu()

        
        





