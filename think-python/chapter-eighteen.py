# Alexandra de Carvalho, 28 September 2021


import random


# Exercise 18.1 - Write a __lt__ method for Time objects
class Time(object):
    """Represents the time of day.
    attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour=hour
        self.minute=minute
        self.second=second

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def __lt__(self, other):
        if self.hour < other.hour or (self.hour==other.hour and self.minute < other.minute) or (self.hour==other.hour and self.minute==other.minute and self.second < other.second):
            return True
        return False

    def __str__(self):
        return str(self.hour) + ':' + str(self.minute) + ':' + str(self.second) 


# Exercise 18.2 - Write a Deck method named sort that uses the list method sort to sort the cards in a Deck
class Card(object):
    """Represents a standard playing card."""
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
    
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '{} of {}'.format(Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        # check the suits
        if self.suit < other.suit:
            return True
        # suits are the same... check ranks
        if self.suit == other.suit and self.rank < other.rank:
            return True
        return False

    def __eq__(self,other):
        return self.suit == other.suit and self.rank == other.rank

class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
    
    def pop_card(self,i=-1):
        return self.cards.pop(i)

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def shuffle(self):
        random.shuffle(self.cards)
    
    def sort(self):
        self.cards.sort()


    #   Exercise 18.3 - Write a Deck method that takes two parameters, the number of hands and the number of cards per hand, and that creates new Hand objects, deals the appropriate number of cards per hand, and returns a list of Hand objects
    def deal_hands(self, n_hands, n_cards, poker=0):
        res = []

        for n in range(n_hands):
            if poker:
                h = PokerHand()
            else:
                h = Hand()
            for card in range(n_cards):
                self.shuffle()
                h.add_card(self.cards.pop())

            res += [h]
        
        return res

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

class Hand(Deck):
    """Represents a hand of playing cards."""
    def __init__(self, label=''):
        self.cards = []
        self.label = label


# Exercise 18.5 - Encapsulate the global variables and functions of the Markov exercise as attributes and methods of a new class called Markov
class Markov(object):
    """Represents the Markov analysis."""
    def __init__(self):
        self.suffix_map = dict()
        self.all_words = []

    def markov_analysis(self,prefix_length):
        if self.all_words:
            self.all_words = []
        try:
            f = open('alicewonderland.txt','r',encoding='utf8')
        except IOError:
            print("ERROR: Could not find alicewonderland.txt\n")
        else:
            for line in f:
                self.all_words += line.strip().split(' ')
            f.close()
                
        last_idx = len(self.all_words) - prefix_length - 1
        for idx in range(last_idx):
            prefix = ' '.join(self.all_words[idx:idx+prefix_length])
            suffix = self.all_words[idx+prefix_length]
            if prefix not in self.suffix_map:
                self.suffix_map[prefix] = dict()
            self.suffix_map[prefix][suffix] = self.suffix_map[prefix].get(suffix,0) + 1

        return self.suffix_map

    def random_text(self, prefix_length):
        markov = self.markov_analysis(prefix_length)
        text = random.choice(list(markov.keys()))   # seed

        iterations = 0
        while iterations < 40:
            last_choice = ' '.join(text.split(' ')[-prefix_length:])
            text+=' '+sorted(markov[last_choice].items(), key= lambda t: t[1], reverse=True)[0][0]
            iterations+=1
        
        return text


# Exercise 18.6 - Copy the given PokerHand.py and add methods named has_pair, has_twopair, etc. that return True or False according to whether or not the hand meets the relevant criteria
class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.
        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def rank_hist(self):
        hist = dict()
        for card in self.cards:
            hist[card.rank] = hist.get(card.rank, 0) + 1
        return hist

    def has_pair(self):
        rank_hist = self.rank_hist()
        
        for n in rank_hist.values():
            if n > 1:
                return True

        return False
    
    def has_two_pair(self):
        hist = self.rank_hist()
        number_pairs = 0

        for n in hist.values():
            if n > 1:
                number_pairs += 1

        if number_pairs >= 2:
            return True
        else:
            return False

    def has_three_kind(self):
        hist = self.rank_hist()

        for n in hist.values():
            if n > 2:
                return True

        return False

    def has_four_kind(self):
        hist = self.rank_hist()

        for n in hist.values():
            if n > 3:
                return True

        return False

    def has_straight(self):
        if len(self.cards) < 5:
            return False

        hist = list(self.rank_hist().keys())
        
        for card_rank in hist:
            if card_rank > 10:
                continue

            first_rank = card_rank
            rank_sequence = [first_rank]
            
            for n in range(1,5):
                new_rank = first_rank + n
                if new_rank == 14:
                    new_rank = 1

                rank_sequence += [new_rank]
            
            flag = 0
            for element in rank_sequence:
                if element not in hist:
                    flag = 1
                    break
            
            if not flag:
                return True
        
        return False

    def has_straight_flush(self):
        return self.has_flush() and self.has_straight()

    def has_full_house(self):
        hist = self.rank_hist()

        flag1, flag2 = 0,0
        for n in hist.values():
            if n == 3:
                flag1 = 1
            if n == 2:
                flag2 = 1

            if flag1 and flag2:
                return True

        return False
    
    # Exercise 18.6 - Write a method named classify that figures out the highest-value classification for a hand and sets the label attribute accordingly
    def classify(self):
        if self.has_straight_flush():
            self.label = 'straight flush'
        elif self.has_four_kind():
            self.label = 'four of a kind'
        elif self.has_full_house():
            self.label = 'full house'
        elif self.has_flush():
            self.label = 'flush'
        elif self.has_straight():
            self.label = 'straight'
        elif self.has_three_kind():
            self.label = 'three of a kind'
        elif self.has_two_pair():
            self.label = 'two pair'
        elif self.has_pair():
            self.label = 'pair'

# Exercise 18.6 - Write a function that shuffles a deck of cards, divides it into hands, classifies the hands, and counts the number of times various classifications appear
def hand_label_probabilities():
    d = Deck()
    d.shuffle()
    classifications = []
    hands = d.deal_hands(10,5, 1)

    for hand in hands:
        hand.classify()
        classifications += [hand.label]

    res = dict()
    for type_hand in classifications:
        res[type_hand] = res.get(type_hand, 0) + 1   
    
    return res


##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Exercise 18.1")
    print("2. Exercise 18.2")
    print("3. Exercise 18.3")
    print("5. Exercise 18.5")
    print("6. Exercise 18.6")
    print("0. Exit")
    print(67 * "-")

def main():
    loop = True
    t1 = Time(11,59,30)
    d = Deck()
    while loop:
        print_menu()
        try:
            choice = int(input('Enter your choice [1-3,5-6] or 0 to quit: '))
        except:
            choice = 222    # Invalid option
        
        if choice==1:
            while True:
                try:
                    h = int(input('h: '))
                    m = int(input('m: '))
                    s = int(input('s: '))
                except ValueError:
                    print("We're sorry! The time introduced seem to be invalid! Please try again.")
                else:
                    t2 = Time(h,m,s)
                    print('Is', t1, 'lesser than', t2, '?',t1 < t2)
                    break
        elif choice==2:
            print(d)
            d.shuffle()
            print('--' * 60 + '\n', d)
            d.sort()
            print('--' * 60 + '\n', d)
        elif choice==3:
            while True:
                try:
                    n_hands = int(input('Number of hands: '))
                    n_cards = int(input('Number of cards by hand: '))
                except ValueError:
                    print("We're sorry! The numbers you introduced seem to be invalid! Please try again.")
                else:
                    hands = d.deal_hands(n_hands,n_cards)
                    count = 1
                    for hand in hands:
                        print('HAND',count)
                        print(hand)
                        count+=1
                    break
        elif choice==5:
            m = Markov()
            l = 2
            print(m.markov_analysis(l))
            print(m.random_text(l))
        elif choice==6:
            # Exercise 18.6 - Print a table of the classifications and their probabilities
            hand_type_hist = hand_label_probabilities()
            total_hands = sum(list(hand_type_hist.values())) 
            print("{:<16s} {:<16s}".format('Hand Type', 'Probability'))
            for k,v in hand_type_hist.items():
                if not k:
                    k = 'None'
                print("{:<16s} {:<4.2f}%".format(k, 100*v/total_hands))
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()