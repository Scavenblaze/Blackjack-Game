import random

suits=["Spades", "Diamonds", "Hearts", "Clubs"]
cards=["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]


def cal_card(card):
    if(card in ['K', 'Q', 'J']):
        return 10
    elif(card=='A'):
        return 1
    else:
        return card
    

#player's first 2 cards
def pinitdraw(player):
    psuit=random.choice(suits)
    pcard=random.choice(cards)
    pinitdraw1=(psuit,pcard)
    
    psuit=random.choice(suits)
    pcard=random.choice(cards)
    pinitdraw2=(psuit,pcard)
    
    print("\nPlayer's cards are:", pinitdraw1, pinitdraw2)
    
    player+=cal_card(pinitdraw1[1])
    player+=cal_card(pinitdraw2[1])
    print("\nPlayer is: ",player)
    
    return player


#dealer's first 2 cards
def dinitdraw(dealer):
    dsuit=random.choice(suits)
    dcard=random.choice(cards)
    dinitdraw=(dsuit,dcard)
   
    print("\ndealer's visible card is:", dinitdraw)
   
    dealer+=cal_card(dinitdraw[1])
    print("\nDealer is: ", dealer)
    return dealer

#logic
def hit(player):
    pdraw1=random.choice(suits)
    pdraw2=random.choice(cards)
    pdraw=(pdraw1,pdraw2)
    
    print(pdraw)
    
    player+=cal_card(pdraw[1])
    print("player is ",player)
    return player

#dealer's turn
def dealerhit(dealer, player):
    while(True):
        if(dealer<player):
            ddraw1=random.choice(suits)
            ddraw2=random.choice(cards)
            ddraw=(ddraw1,ddraw2)
            print(ddraw)
            dealer+=cal_card(ddraw[1])
            print("dealer is ",dealer, '\n')
        
        elif(dealer>21):
            print("You win, dealer loses")
            break
        
        elif(dealer>player):
            print("You lose, dealer wins")
            break
        
        elif(dealer==21):
            print("You lose, Dealer wins")
            break
        
        elif(dealer==player):
            print("Push aka draw")
            break



#output
def main():
    player=0
    dealer=0
    player = pinitdraw(player)
    dealer = dinitdraw(dealer)
    
    while(True):
        ch=input("\nEnter your move: 1) Hit\n 2) Stand \n").lower()
        if(ch == 'hit' or ch == '1'):
            player = hit(player)
            if(player==21):
                print("You win")
                break
            
            elif(player>21):
                print("You lose")
                break
        
        elif(ch == 'stand' or ch == '2'):
            print("\nOkay Standing... Dealer will play now.\n")
            dealerhit(dealer, player)
            break
        
        else: print("I said hit or stand")


main()
        
#only hit and stand for now