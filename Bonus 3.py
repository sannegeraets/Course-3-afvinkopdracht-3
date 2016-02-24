# -*- coding: utf-8 -*-
"""
Created on 6-2-2016

@author: Sanne Geraets
"""

import random

def main():
    d = {
    "alanine" : "A",
    "arginine" : "R",
    "asparagine" : "N",
    "asparaginezuur" : "D",
    "cysteine" : "C",
    "fenylalanine" : "F",
    "glutamine" : "Q",
    "glutaminezuur" : "E",
    "glycine" : "G",
    "histidine" : "H",
    "isoleucine" : "I",
    "leucine" : "L",
    "lisine" : "K",
    "methionine" : "M",
    "proline" : "P",
    "serine" : "S",
    "threonine" : "T",
    "tryptofaan" : "W",
    "tyrosine" : "Y",
    "valine" : "V"
    }
    print("Welcome to the aminoacids quizzzzzz!!!")
    print("Here we will show you a aminoacid,")
    print("Your job is to answer the letter that belongs to that aminoacid")
    print("Good luck!!!")
    print()
    print()
    quizz(d)


def quizz(d):
    count = 0
    while count != 5:
        True = question(d)
        if question(d) == True:
            count += 1
        True = question2(d)
        if question2(d) == True:
            count += 1


def question(d):
    x = random.choice(list(d.keys()))
    print(x)
    print(d[x])
    a = False
    while a == False:
        answer = input("What letter has " + x + "? ").upper()
        if answer != d[x]:
            print("Sorry, that's not the right answer.")
        elif answer == d[x]:
            print("That's the correct answer!!")
            print("We'll play again!!")
            print()
            return True


def question2(d):
    x = random.choice(list(d.keys()))
    print(d[x])
    print(x)
    a = False
    while a == False:
        answer = input("What aminoacid has " + d[x] + "? ").lower()
        if answer != x:
            print("Sorry, that's not the right answer.")
        elif answer == x:
            print("That's the correct answer!!")
            print("We'll play again!!")
            print()
            return True


main()
