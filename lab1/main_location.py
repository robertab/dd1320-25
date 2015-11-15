#! usrbin/env python3

""" 
Kurs: DD1320/25 Tillämpad datalogi med Etik
Författare: Robert Åbert, Sara Ervik, CDATE_2.
Uppgift: Lab1
"""
from location import Location


def read_file(the_file):
    """
    Skapar objekt genom att itirera över längden av listan
    för att sedan använda listan från read_file() för att
    skapa objekt i det i:te elementet. 
    """
    object_list = [Location(the_list[i], the_list[i+1], the_list[i+2],
                            the_list[i+3], the_list[i+4]) \
                   for i in range(6, len(the_list)-4, 6)]
    return object_list 


def search(object_list):
    """
    Jämför namnet från input med namnet från objektet i listan.
    """
    userinput = input("Vilket plats vill du söka efter?: ")
    for i in range(0, len(object_list)):
        if str(object_list[i].get_name()) == userinput:
            print(object_list[i])


def main():
    """
    Initierar programmet. Skickar den hårdkodade filen
    till read_file.
    """
    the_list = read_file("geodataSW.txt")
    object_list = create_object(the_list)
    search(object_list)


if __name__ == '__main__':
    main()


