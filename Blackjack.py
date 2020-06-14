import random

DealerHand = []
Hand = []
#PlayerHand2 = []
#Choice = ''

Bank = 100000
Bet = 100
Games = 100000

def Hit(Hand):
    Card = random.randint(2, 14)
    if (Card >= 12): #Jack, Queen, King
        Card = 10
    
    Hand.append(Card)
    CheckAce(Hand)

def Double(Hand):
    global Bank
    global Bet
    global DealerHand
    
    NewBet = Bet * 2
    Hit(Hand)
    
    if (sum(Hand) > 21):
        Bank -= NewBet
        return
    
    while (sum(DealerHand) < 17 or (sum(DealerHand) == 17 and 11 in DealerHand)):
        Hit(DealerHand)
    
    if (sum(DealerHand) > 21): #Dealer Busts, Player Wins
        Bank += Bet
        return
    
    elif (sum(Hand) > sum(DealerHand)): #Player Wins
        Bank += Bet
        return
    
    elif (sum(Hand) < sum(DealerHand)): #Player Loses
        Bank -= Bet
        return
    
    else: #Push
        return
        
def Split(Hand):
    Hand1 = [Hand[0]]
    Hand2 = [Hand[0]]
    
    Hit(Hand1)
    Hit(Hand2)
    
    PlayGame(Hand1)
    PlayGame(Hand2)
    

def CheckAce(Hand):
    for i in range(len(Hand)):
        if (Hand[i] == 11 and sum(Hand) > 21):
            Hand[i] = 1
            
def PlayGame(Hand):
    global Bank
    global Bet
    global DealerHand
    
    CheckAce(Hand)
    while (sum(Hand) < 21 and len(Hand) < 5):
        CheckAce(Hand)
        if (sum(Hand) == 21):
            break
        
        if (11 in Hand): #If Player Hand is Soft
            if (sum(Hand) == 13): #Soft 13
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    Hit(Hand)
                
                elif (DealerHand[1] == 2):
                    Hit(Hand)
                
                elif (DealerHand[1] == 3):
                    Hit(Hand)
                
                elif (DealerHand[1] == 4):
                    Hit(Hand)
                
                elif (DealerHand[1] == 5):
                    Hit(Hand)
                
                elif (DealerHand[1] == 6):
                    Hit(Hand)
                
                elif (DealerHand[1] == 7):
                    Hit(Hand)
                
                elif (DealerHand[1] == 8):
                    Hit(Hand)
                
                elif (DealerHand[1] == 9):
                    Hit(Hand)
                
                elif (DealerHand[1] == 10):
                    Hit(Hand)
            
            elif (sum(Hand) == 14): #Soft 14
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    Hit(Hand)
                
                elif (DealerHand[1] == 2):
                    Hit(Hand)
                
                elif (DealerHand[1] == 3):
                    Hit(Hand)
                
                elif (DealerHand[1] == 4):
                    Hit(Hand)
                
                elif (DealerHand[1] == 5):
                    Hit(Hand)
                
                elif (DealerHand[1] == 6):
                    Hit(Hand)
                
                elif (DealerHand[1] == 7):
                    Hit(Hand)
                
                elif (DealerHand[1] == 8):
                    Hit(Hand)
                
                elif (DealerHand[1] == 9):
                    Hit(Hand)
                
                elif (DealerHand[1] == 10):
                    Hit(Hand)
            
            elif (sum(Hand) == 15): #Soft 15
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    Hit(Hand)
                
                elif (DealerHand[1] == 2):
                    Hit(Hand)
                
                elif (DealerHand[1] == 3):
                    Hit(Hand)
                
                elif (DealerHand[1] == 4):
                    Hit(Hand)
                
                elif (DealerHand[1] == 5):
                    Hit(Hand)
                
                elif (DealerHand[1] == 6):
                    Hit(Hand)
                
                elif (DealerHand[1] == 7):
                    Hit(Hand)
                
                elif (DealerHand[1] == 8):
                    Hit(Hand)
                
                elif (DealerHand[1] == 9):
                    Hit(Hand)
                
                elif (DealerHand[1] == 10):
                    Hit(Hand)
            
            elif (sum(Hand) == 16): #Soft 16
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    Hit(Hand)
                
                elif (DealerHand[1] == 2):
                    Hit(Hand)
                
                elif (DealerHand[1] == 3):
                    Hit(Hand)
                
                elif (DealerHand[1] == 4):
                    Hit(Hand)
                
                elif (DealerHand[1] == 5):
                    Hit(Hand)
                
                elif (DealerHand[1] == 6):
                    Hit(Hand)
                
                elif (DealerHand[1] == 7):
                    Hit(Hand)
                
                elif (DealerHand[1] == 8):
                    Hit(Hand)
                
                elif (DealerHand[1] == 9):
                    Hit(Hand)
                
                elif (DealerHand[1] == 10):
                    Hit(Hand)
            
            elif (sum(Hand) == 17): #Soft 17
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    Hit(Hand)
                
                elif (DealerHand[1] == 2):
                    Hit(Hand)
                
                elif (DealerHand[1] == 3):
                    Hit(Hand)
                
                elif (DealerHand[1] == 4):
                    Hit(Hand)
                
                elif (DealerHand[1] == 5):
                    Hit(Hand)
                
                elif (DealerHand[1] == 6):
                    Hit(Hand)
                
                elif (DealerHand[1] == 7):
                    Hit(Hand)
                
                elif (DealerHand[1] == 8):
                    Hit(Hand)
                
                elif (DealerHand[1] == 9):
                    Hit(Hand)
                
                elif (DealerHand[1] == 10):
                    Hit(Hand)
            
            elif (sum(Hand) == 18): #Soft 18
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    Hit(Hand)
                
                elif (DealerHand[1] == 2):
                    break
                
                elif (DealerHand[1] == 3):
                    break
                
                elif (DealerHand[1] == 4):
                    break
                
                elif (DealerHand[1] == 5):
                    break
                
                elif (DealerHand[1] == 6):
                    break
                
                elif (DealerHand[1] == 7):
                    break
                
                elif (DealerHand[1] == 8):
                    break
                
                elif (DealerHand[1] == 9):
                    Hit(Hand)
                
                elif (DealerHand[1] == 10):
                    Hit(Hand)
            
            elif (sum(Hand) == 19): #Soft 19
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    break
                
                elif (DealerHand[1] == 2):
                    break
                
                elif (DealerHand[1] == 3):
                    break
                
                elif (DealerHand[1] == 4):
                    break
                
                elif (DealerHand[1] == 5):
                    break
                
                elif (DealerHand[1] == 6):
                    break
                
                elif (DealerHand[1] == 7):
                    break
                
                elif (DealerHand[1] == 8):
                    break
                
                elif (DealerHand[1] == 9):
                    break
                
                elif (DealerHand[1] == 10):
                    break
            
            elif (sum(Hand) == 20): #Soft 20
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    break
                
                elif (DealerHand[1] == 2):
                    break
                
                elif (DealerHand[1] == 3):
                    break
                
                elif (DealerHand[1] == 4):
                    break
                
                elif (DealerHand[1] == 5):
                    break
                
                elif (DealerHand[1] == 6):
                    break
                
                elif (DealerHand[1] == 7):
                    break
                
                elif (DealerHand[1] == 8):
                    break
                
                elif (DealerHand[1] == 9):
                    break
                
                elif (DealerHand[1] == 10):
                    break
                
        
        else: #Normal Game
            if (sum(Hand) == 4):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    Hit(Hand)
                
                elif (DealerHand[1] == 2):
                    Hit(Hand)
                
                elif (DealerHand[1] == 3):
                    Hit(Hand)
                
                elif (DealerHand[1] == 4):
                    Hit(Hand)
                
                elif (DealerHand[1] == 5):
                    Hit(Hand)
                
                elif (DealerHand[1] == 6):
                    Hit(Hand)
                
                elif (DealerHand[1] == 7):
                    Hit(Hand)
                
                elif (DealerHand[1] == 8):
                    Hit(Hand)
                
                elif (DealerHand[1] == 9):
                    Hit(Hand)
                
                elif (DealerHand[1] == 10):
                    Hit(Hand)
                    
            elif (sum(Hand) == 5):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    Hit(Hand)
                
                elif (DealerHand[1] == 2):
                    Hit(Hand)
                
                elif (DealerHand[1] == 3):
                    Hit(Hand)
                
                elif (DealerHand[1] == 4):
                    Hit(Hand)
                
                elif (DealerHand[1] == 5):
                    Hit(Hand)
                
                elif (DealerHand[1] == 6):
                    Hit(Hand)
                
                elif (DealerHand[1] == 7):
                    Hit(Hand)
                
                elif (DealerHand[1] == 8):
                    Hit(Hand)
                
                elif (DealerHand[1] == 9):
                    Hit(Hand)
                
                elif (DealerHand[1] == 10):
                    Hit(Hand)
            
            elif (sum(Hand) == 6):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    Hit(Hand)
                
                elif (DealerHand[1] == 2):
                    Hit(Hand)
                
                elif (DealerHand[1] == 3):
                    Hit(Hand)
                
                elif (DealerHand[1] == 4):
                    Hit(Hand)
                
                elif (DealerHand[1] == 5):
                    Hit(Hand)
                
                elif (DealerHand[1] == 6):
                    Hit(Hand)
                
                elif (DealerHand[1] == 7):
                    Hit(Hand)
                
                elif (DealerHand[1] == 8):
                    Hit(Hand)
                
                elif (DealerHand[1] == 9):
                    Hit(Hand)
                
                elif (DealerHand[1] == 10):
                    Hit(Hand)
            
            elif (sum(Hand) == 7):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    Hit(Hand)
                
                elif (DealerHand[1] == 2):
                    Hit(Hand)
                
                elif (DealerHand[1] == 3):
                    Hit(Hand)
                
                elif (DealerHand[1] == 4):
                    Hit(Hand)
                
                elif (DealerHand[1] == 5):
                    Hit(Hand)
                
                elif (DealerHand[1] == 6):
                    Hit(Hand)
                
                elif (DealerHand[1] == 7):
                    Hit(Hand)
                
                elif (DealerHand[1] == 8):
                    Hit(Hand)
                
                elif (DealerHand[1] == 9):
                    Hit(Hand)
                
                elif (DealerHand[1] == 10):
                    Hit(Hand)
            
            elif (sum(Hand) == 8):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    Hit(Hand)
                
                elif (DealerHand[1] == 2):
                    Hit(Hand)
                
                elif (DealerHand[1] == 3):
                    Hit(Hand)
                
                elif (DealerHand[1] == 4):
                    Hit(Hand)
                
                elif (DealerHand[1] == 5):
                    Hit(Hand)
                
                elif (DealerHand[1] == 6):
                    Hit(Hand)
                
                elif (DealerHand[1] == 7):
                    Hit(Hand)
                
                elif (DealerHand[1] == 8):
                    Hit(Hand)
                
                elif (DealerHand[1] == 9):
                    Hit(Hand)
                
                elif (DealerHand[1] == 10):
                    Hit(Hand)
            
            elif (sum(Hand) == 9):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    Hit(Hand)
                
                elif (DealerHand[1] == 2):
                    Hit(Hand)
                
                elif (DealerHand[1] == 3):
                    Hit(Hand)
                
                elif (DealerHand[1] == 4):
                    Hit(Hand)
                
                elif (DealerHand[1] == 5):
                    Hit(Hand)
                
                elif (DealerHand[1] == 6):
                    Hit(Hand)
                
                elif (DealerHand[1] == 7):
                    Hit(Hand)
                
                elif (DealerHand[1] == 8):
                    Hit(Hand)
                
                elif (DealerHand[1] == 9):
                    Hit(Hand)
                
                elif (DealerHand[1] == 10):
                    Hit(Hand)
            
            elif (sum(Hand) == 10):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    Hit(Hand)
                
                elif (DealerHand[1] == 2):
                    Hit(Hand)
                
                elif (DealerHand[1] == 3):
                    Hit(Hand)
                
                elif (DealerHand[1] == 4):
                    Hit(Hand)
                
                elif (DealerHand[1] == 5):
                    Hit(Hand)
                
                elif (DealerHand[1] == 6):
                    Hit(Hand)
                
                elif (DealerHand[1] == 7):
                    Hit(Hand)
                
                elif (DealerHand[1] == 8):
                    Hit(Hand)
                
                elif (DealerHand[1] == 9):
                    Hit(Hand)
                
                elif (DealerHand[1] == 10):
                    Hit(Hand)
            
            elif (sum(Hand) == 11):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    Hit(Hand)
                
                elif (DealerHand[1] == 2):
                    Hit(Hand)
                
                elif (DealerHand[1] == 3):
                    Hit(Hand)
                
                elif (DealerHand[1] == 4):
                    Hit(Hand)
                
                elif (DealerHand[1] == 5):
                    Hit(Hand)
                
                elif (DealerHand[1] == 6):
                    Hit(Hand)
                
                elif (DealerHand[1] == 7):
                    Hit(Hand)
                
                elif (DealerHand[1] == 8):
                    Hit(Hand)
                
                elif (DealerHand[1] == 9):
                    Hit(Hand)
                
                elif (DealerHand[1] == 10):
                    Hit(Hand)
            
            elif (sum(Hand) == 12):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    Hit(Hand)
                
                elif (DealerHand[1] == 2):
                    Hit(Hand)
                
                elif (DealerHand[1] == 3):
                    Hit(Hand)
                
                elif (DealerHand[1] == 4):
                    break
                
                elif (DealerHand[1] == 5):
                    break
                
                elif (DealerHand[1] == 6):
                    break
                
                elif (DealerHand[1] == 7):
                    Hit(Hand)
                
                elif (DealerHand[1] == 8):
                    Hit(Hand)
                
                elif (DealerHand[1] == 9):
                    Hit(Hand)
                
                elif (DealerHand[1] == 10):
                    Hit(Hand)
            
            elif (sum(Hand) == 13):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    Hit(Hand)
                
                elif (DealerHand[1] == 2):
                    break
                
                elif (DealerHand[1] == 3):
                    break
                
                elif (DealerHand[1] == 4):
                    break
                
                elif (DealerHand[1] == 5):
                    break
                
                elif (DealerHand[1] == 6):
                    break
                
                elif (DealerHand[1] == 7):
                    Hit(Hand)
                
                elif (DealerHand[1] == 8):
                    Hit(Hand)
                
                elif (DealerHand[1] == 9):
                    Hit(Hand)
                
                elif (DealerHand[1] == 10):
                    Hit(Hand)
            
            elif (sum(Hand) == 14):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    Hit(Hand)
                
                elif (DealerHand[1] == 2):
                    break
                
                elif (DealerHand[1] == 3):
                    break
                
                elif (DealerHand[1] == 4):
                    break
                
                elif (DealerHand[1] == 5):
                    break
                
                elif (DealerHand[1] == 6):
                    break
                
                elif (DealerHand[1] == 7):
                    Hit(Hand)
                
                elif (DealerHand[1] == 8):
                    Hit(Hand)
                
                elif (DealerHand[1] == 9):
                    Hit(Hand)
                
                elif (DealerHand[1] == 10):
                    Hit(Hand)
            
            elif (sum(Hand) == 15):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    Hit(Hand)
                
                elif (DealerHand[1] == 2):
                    break
                
                elif (DealerHand[1] == 3):
                    break
                
                elif (DealerHand[1] == 4):
                    break
                
                elif (DealerHand[1] == 5):
                    break
                
                elif (DealerHand[1] == 6):
                    break
                
                elif (DealerHand[1] == 7):
                    Hit(Hand)
                
                elif (DealerHand[1] == 8):
                    Hit(Hand)
                
                elif (DealerHand[1] == 9):
                    Hit(Hand)
                
                elif (DealerHand[1] == 10):
                    Hit(Hand)
            
            elif (sum(Hand) == 16):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    Hit(Hand)
                
                elif (DealerHand[1] == 2):
                    break
                
                elif (DealerHand[1] == 3):
                    break
                
                elif (DealerHand[1] == 4):
                    break
                
                elif (DealerHand[1] == 5):
                    break
                
                elif (DealerHand[1] == 6):
                    break
                
                elif (DealerHand[1] == 7):
                    Hit(Hand)
                
                elif (DealerHand[1] == 8):
                    Hit(Hand)
                
                elif (DealerHand[1] == 9):
                    Hit(Hand)
                
                elif (DealerHand[1] == 10):
                    Hit(Hand)
            
            elif (sum(Hand) == 17):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    break
                
                elif (DealerHand[1] == 2):
                    break
                
                elif (DealerHand[1] == 3):
                    break
                
                elif (DealerHand[1] == 4):
                    break
                
                elif (DealerHand[1] == 5):
                    break
                
                elif (DealerHand[1] == 6):
                    break
                
                elif (DealerHand[1] == 7):
                    break
                
                elif (DealerHand[1] == 8):
                    break
                
                elif (DealerHand[1] == 9):
                    break
                
                elif (DealerHand[1] == 10):
                    break
            
            elif (sum(Hand) == 18):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    break
                
                elif (DealerHand[1] == 2):
                    break
                
                elif (DealerHand[1] == 3):
                    break
                
                elif (DealerHand[1] == 4):
                    break
                
                elif (DealerHand[1] == 5):
                    break
                
                elif (DealerHand[1] == 6):
                    break
                
                elif (DealerHand[1] == 7):
                    break
                
                elif (DealerHand[1] == 8):
                    break
                
                elif (DealerHand[1] == 9):
                    break
                
                elif (DealerHand[1] == 10):
                    break
            
            elif (sum(Hand) == 19):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    break
                
                elif (DealerHand[1] == 2):
                    break
                
                elif (DealerHand[1] == 3):
                    break
                
                elif (DealerHand[1] == 4):
                    break
                
                elif (DealerHand[1] == 5):
                    break
                
                elif (DealerHand[1] == 6):
                    break
                
                elif (DealerHand[1] == 7):
                    break
                
                elif (DealerHand[1] == 8):
                    break
                
                elif (DealerHand[1] == 9):
                    break
                
                elif (DealerHand[1] == 10):
                    break
            
            elif (sum(Hand) == 20):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    break
                
                elif (DealerHand[1] == 2):
                    break
                
                elif (DealerHand[1] == 3):
                    break
                
                elif (DealerHand[1] == 4):
                    break
                
                elif (DealerHand[1] == 5):
                    break
                
                elif (DealerHand[1] == 6):
                    break
                
                elif (DealerHand[1] == 7):
                    break
                
                elif (DealerHand[1] == 8):
                    break
                
                elif (DealerHand[1] == 9):
                    break
                
                elif (DealerHand[1] == 10):
                    break
        
        CheckAce(Hand)
        if (len(Hand) >= 5 and sum(Hand) <= 21): #5 Card Rule
            Bank += Bet
            return
            
        elif (sum(Hand) > 21): #Player Busts
            Bank -= Bet
            return
    
    while (sum(DealerHand) < 17 or (sum(DealerHand) == 17 and 11 in DealerHand)):
        Hit(DealerHand)
    
    if (sum(DealerHand) > 21): #Dealer Busts, Player Wins
        Bank += Bet
        return
    
    elif (sum(Hand) > sum(DealerHand)): #Player Wins
        Bank += Bet
        return
    
    elif (sum(Hand) < sum(DealerHand)): #Player Loses
        Bank -= Bet
        return
    
    else: #Push
        return
    

for i in range(Games):
    #Deal Cards
    DealerHand = []
    Hand = []
    #PlayerHand2 = []
    
    Hit(DealerHand)
    Hit(DealerHand)
    Hit(Hand)
    Hit(Hand)
    
    #Choice = ''
    
    if (sum(DealerHand) == 21 and sum(Hand) == 21): #If Both Players get Blackjack
        continue #Push
    
    elif (sum(DealerHand) == 21 and sum(Hand) != 21): #If Dealer gets Blackjack
        Bank -= Bet
    
    elif (sum(DealerHand) != 21 and sum(Hand) == 21): #If Player gets Blackjack
        Bank += int(Bet * 1.5)
        
    else:
        if (Hand[0] == Hand[1]): #If Player has a Pair
            if (Hand[0] == 1): #If Ace Pair
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    Split(Hand)
                
                elif (DealerHand[1] == 2):
                    Split(Hand)
                
                elif (DealerHand[1] == 3):
                    Split(Hand)
                
                elif (DealerHand[1] == 4):
                    Split(Hand)
                
                elif (DealerHand[1] == 5):
                    Split(Hand)
                
                elif (DealerHand[1] == 6):
                    Split(Hand)
                
                elif (DealerHand[1] == 7):
                    Split(Hand)
                
                elif (DealerHand[1] == 8):
                    Split(Hand)
                
                elif (DealerHand[1] == 9):
                    Split(Hand)
                
                elif (DealerHand[1] == 10):
                    Split(Hand)
                
            elif (Hand[0] == 2): #If Two Pair
                
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    Split(Hand)
                
                elif (DealerHand[1] == 3):
                    Split(Hand)
                
                elif (DealerHand[1] == 4):
                    Split(Hand)
                
                elif (DealerHand[1] == 5):
                    Split(Hand)
                
                elif (DealerHand[1] == 6):
                    Split(Hand)
                
                elif (DealerHand[1] == 7):
                    Split(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
                
            elif (Hand[0] == 3): #If Three Pair
                
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    Split(Hand)
                
                elif (DealerHand[1] == 3):
                    Split(Hand)
                
                elif (DealerHand[1] == 4):
                    Split(Hand)
                
                elif (DealerHand[1] == 5):
                    Split(Hand)
                
                elif (DealerHand[1] == 6):
                    Split(Hand)
                
                elif (DealerHand[1] == 7):
                    Split(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
            
            elif (Hand[0] == 4): #If Four Pair
                
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 3):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 4):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 5):
                    Split(Hand)
                
                elif (DealerHand[1] == 6):
                    Split(Hand)
                
                elif (DealerHand[1] == 7):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
            
            elif (Hand[0] == 5): #If Five Pair
                
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    Double(Hand)
                
                elif (DealerHand[1] == 3):
                    Double(Hand)
                
                elif (DealerHand[1] == 4):
                    Double(Hand)
                
                elif (DealerHand[1] == 5):
                    Double(Hand)
                
                elif (DealerHand[1] == 6):
                    Double(Hand)
                
                elif (DealerHand[1] == 7):
                    Double(Hand)
                
                elif (DealerHand[1] == 8):
                    Double(Hand)
                
                elif (DealerHand[1] == 9):
                    Double(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
            
            elif (Hand[0] == 6): #If Six Pair
                
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    Split(Hand)
                
                elif (DealerHand[1] == 3):
                    Split(Hand)
                
                elif (DealerHand[1] == 4):
                    Split(Hand)
                
                elif (DealerHand[1] == 5):
                    Split(Hand)
                
                elif (DealerHand[1] == 6):
                    Split(Hand)
                
                elif (DealerHand[1] == 7):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
            
            elif (Hand[0] == 7): #If Seven Pair
                
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    Split(Hand)
                
                elif (DealerHand[1] == 3):
                    Split(Hand)
                
                elif (DealerHand[1] == 4):
                    Split(Hand)
                
                elif (DealerHand[1] == 5):
                    Split(Hand)
                
                elif (DealerHand[1] == 6):
                    Split(Hand)
                
                elif (DealerHand[1] == 7):
                    Split(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
            
            elif (Hand[0] == 8): #If Eight Pair
                
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    Split(Hand)
                
                elif (DealerHand[1] == 2):
                    Split(Hand)
                
                elif (DealerHand[1] == 3):
                    Split(Hand)
                
                elif (DealerHand[1] == 4):
                    Split(Hand)
                
                elif (DealerHand[1] == 5):
                    Split(Hand)
                
                elif (DealerHand[1] == 6):
                    Split(Hand)
                
                elif (DealerHand[1] == 7):
                    Split(Hand)
                
                elif (DealerHand[1] == 8):
                    Split(Hand)
                
                elif (DealerHand[1] == 9):
                    Split(Hand)
                
                elif (DealerHand[1] == 10):
                    Split(Hand)
            
            elif (Hand[0] == 9): #If Nine Pair
                
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    Split(Hand)
                
                elif (DealerHand[1] == 3):
                    Split(Hand)
                
                elif (DealerHand[1] == 4):
                    Split(Hand)
                
                elif (DealerHand[1] == 5):
                    Split(Hand)
                
                elif (DealerHand[1] == 6):
                    Split(Hand)
                
                elif (DealerHand[1] == 7):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 8):
                    Split(Hand)
                
                elif (DealerHand[1] == 9):
                    Split(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
            
            elif (Hand[0] == 10): #If Ten Pair
                
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 3):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 4):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 5):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 6):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 7):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
        
        elif (11 in Hand): #If Player Hand is Soft
            if (sum(Hand) == 13): #Soft 13
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 3):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 4):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 5):
                    Double(Hand)
                
                elif (DealerHand[1] == 6):
                    Double(Hand)
                
                elif (DealerHand[1] == 7):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
            
            elif (sum(Hand) == 14): #Soft 14
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 3):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 4):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 5):
                    Double(Hand)
                
                elif (DealerHand[1] == 6):
                    Double(Hand)
                
                elif (DealerHand[1] == 7):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
            
            elif (sum(Hand) == 15): #Soft 15
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 3):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 4):
                    Double(Hand)
                
                elif (DealerHand[1] == 5):
                    Double(Hand)
                
                elif (DealerHand[1] == 6):
                    Double(Hand)
                
                elif (DealerHand[1] == 7):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
            
            elif (sum(Hand) == 16): #Soft 16
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 3):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 4):
                    Double(Hand)
                
                elif (DealerHand[1] == 5):
                    Double(Hand)
                
                elif (DealerHand[1] == 6):
                    Double(Hand)
                
                elif (DealerHand[1] == 7):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
            
            elif (sum(Hand) == 17): #Soft 17
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 3):
                    Double(Hand)
                
                elif (DealerHand[1] == 4):
                    Double(Hand)
                
                elif (DealerHand[1] == 5):
                    Double(Hand)
                
                elif (DealerHand[1] == 6):
                    Double(Hand)
                
                elif (DealerHand[1] == 7):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
            
            elif (sum(Hand) == 18): #Soft 18
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    Double(Hand)
                
                elif (DealerHand[1] == 3):
                    Double(Hand)
                
                elif (DealerHand[1] == 4):
                    Double(Hand)
                
                elif (DealerHand[1] == 5):
                    Double(Hand)
                
                elif (DealerHand[1] == 6):
                    Double(Hand)
                
                elif (DealerHand[1] == 7):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
            
            elif (sum(Hand) == 19): #Soft 19
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 3):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 4):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 5):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 6):
                    Double(Hand)
                
                elif (DealerHand[1] == 7):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
            
            elif (sum(Hand) == 20): #Soft 20
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 3):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 4):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 5):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 6):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 7):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
        
        else: #Normal Game
            if (sum(Hand) == 5):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 3):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 4):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 5):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 6):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 7):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
            
            elif (sum(Hand) == 6):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 3):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 4):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 5):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 6):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 7):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
                    
            elif (sum(Hand) == 7):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 3):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 4):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 5):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 6):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 7):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
                    
            elif (sum(Hand) == 8):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 3):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 4):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 5):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 6):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 7):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
                    
            elif (sum(Hand) == 9):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 3):
                    Double(Hand)
                
                elif (DealerHand[1] == 4):
                    Double(Hand)
                
                elif (DealerHand[1] == 5):
                    Double(Hand)
                
                elif (DealerHand[1] == 6):
                    Double(Hand)
                
                elif (DealerHand[1] == 7):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
            
            elif (sum(Hand) == 10):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    Double(Hand)
                
                elif (DealerHand[1] == 3):
                    Double(Hand)
                
                elif (DealerHand[1] == 4):
                    Double(Hand)
                
                elif (DealerHand[1] == 5):
                    Double(Hand)
                
                elif (DealerHand[1] == 6):
                    Double(Hand)
                
                elif (DealerHand[1] == 7):
                    Double(Hand)
                
                elif (DealerHand[1] == 8):
                    Double(Hand)
                
                elif (DealerHand[1] == 9):
                    Double(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
            
            elif (sum(Hand) == 11):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    Double(Hand)
                
                elif (DealerHand[1] == 2):
                    Double(Hand)
                
                elif (DealerHand[1] == 3):
                    Double(Hand)
                
                elif (DealerHand[1] == 4):
                    Double(Hand)
                
                elif (DealerHand[1] == 5):
                    Double(Hand)
                
                elif (DealerHand[1] == 6):
                    Double(Hand)
                
                elif (DealerHand[1] == 7):
                    Double(Hand)
                
                elif (DealerHand[1] == 8):
                    Double(Hand)
                
                elif (DealerHand[1] == 9):
                    Double(Hand)
                
                elif (DealerHand[1] == 10):
                    Double(Hand)
            
            elif (sum(Hand) == 12):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 3):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 4):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 5):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 6):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 7):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
            
            elif (sum(Hand) == 13):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 3):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 4):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 5):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 6):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 7):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
            
            elif (sum(Hand) == 14):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 3):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 4):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 5):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 6):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 7):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
            
            elif (sum(Hand) == 15):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 3):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 4):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 5):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 6):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 7):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
            
            elif (sum(Hand) == 16):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 3):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 4):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 5):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 6):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 7):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
            
            elif (sum(Hand) == 17):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 3):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 4):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 5):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 6):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 7):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
            
            elif (sum(Hand) == 18):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 3):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 4):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 5):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 6):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 7):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
            
            elif (sum(Hand) == 19):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 3):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 4):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 5):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 6):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 7):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
            
            elif (sum(Hand) == 20):
                if (DealerHand[1] == 1 or DealerHand[1] == 11): #If Dealer has Ace
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 2):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 3):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 4):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 5):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 6):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 7):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 8):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 9):
                    PlayGame(Hand)
                
                elif (DealerHand[1] == 10):
                    PlayGame(Hand)
     
    #print(Hand)
    #print(DealerHand)
    #Check State of Board
    #Play First Turn
    #Simulate Rest of Game
print(Bank)