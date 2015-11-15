# -*- coding: utf-8 -*-



""" 
Kurs: DD1320/25 Tillämpad datalogi med Etik
Författare: Robert Åbert, Sara Ervik, CDATE_2.
Uppgift: Lab6.1
"""

class Syntaxfel(Exception):
    pass


"""
Först behöver vi en funktion check_cap_letter(letter) som undersöker om letter är en stor bokstav. 
Om det inte stämmer returneras false
"""
def check_cap_letter(letter):
    cap_letters = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
    for character in cap_letters:
        if letter == character:
            return "Syntaktiskt korrekt"
    return "Fel!"

"""
Vi behöver även funktionen check_lower_letter(letter) som undersöker om letter är en liten bokstav.
Om det inte stämmer returneras false
"""
def check_lower_letter(letter):
    lower_case_letters = "abcdefghijklmnopqrstuvxyz"
    for character in lower_case_letters:
        if letter == character:
            return "Syntaktiskt korrekt"
    return "Fel!"

"""
Undersöker om indata  nummer > 1 samt ett heltal.
Om det inte stämmer returneras false
"""
def check_num(number):
    try:
        number = int(number)
        if number > 1:
            return "Syntaktiskt korrekt"
        raise Syntaxfel
    except Syntaxfel:
        return "Fel!"
