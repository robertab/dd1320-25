"""
Kurs: DD1320/25 Tillämpad datalogi med Etik
Författare: Robert Åberg, Sara Ervik
Uppgift: Lab2
Fil: main, för både LinkedQ och ArrayQ
"""


from arrayQfile import ArrayQ
# from linkedQFile import LinkedQ




def user_input():
    """
    Tar emot input från användaren och skapar en lista
    med n element
    """
    answer = input("Vilken ordning ligger korten i?: ")
    return answer.split()


def fill_card_deck(answer, card_deck):
    """
    Loopar igenom svaret och köar korten
    """
    for i in answer:
        i = int(i) # Beroende på program
        card_deck.enqueue(i)


def show_sorted_deck(card_deck):
    """
    En while loop som kollar om kortleken är full
    printar ut alla kort som ligger först i kön
    """
    while card_deck.isEmpty() == False:
        queue_card = card_deck.enqueue(card_deck.dequeue())
        empty_the_deck = card_deck.dequeue()
        print(empty_the_deck, end=" ")
        

def main():
    """
    Huvudprogrammet som initierar allt. 
    """
    q = ArrayQ()
#    q = LinkedQ()
    answer = user_input()
    unsorted_array = fill_card_deck(answer, q)
    show_sorted_deck(q)
        
# 7 1 12 2 8 3 11 4 9 5 13 6 10

if __name__ == '__main__':
    main()
