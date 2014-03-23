#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import fileinput
import time
import math

def ORP(n):
    percentage = 0.45
    return int(math.ceil(n * 0.45))

def calculate_spaces(word, maxLength):
    maxOrp = ORP(maxLength) # index + 1
    orp = ORP(len(word)) # index + 1
    prefixSpace = maxOrp - orp
    postfixSpace = maxLength - len(word) - prefixSpace
    
    return (orp, prefixSpace, postfixSpace)

def find_max(reading):
    reading = sorted(reading, key=lambda x: len(x), reverse=True)
    return len(reading[0])

def parse_article(article):
    """
    argument: article::string
    returns: [ word::string | sign::string ]

    word :: single word
    sign :: <pause>
    """
    charToRemoved = ",.!\xad"

    for eachChar in charToRemoved:
        article = article.replace(eachChar, "")

    article = article.strip()
    article = article.replace("\n", " <pause> ")

    return article.split()

def print_word(word, orpConfig):
    def insert_color(word, orpIndex):
        colorCode_red = "\033[91m"
        colorCode_restore = "\033[0m"

        return word[0:orpIndex] + colorCode_red + word[orpIndex] + colorCode_restore + word[orpIndex+1:]
        
    orp, prefix, postfix = orpConfig
    stringToPrint = " " * prefix + insert_color(word, orp-1) + " " * postfix

    print ("\r%s" % stringToPrint, end='')
    sys.stdout.flush()

def spritz(wpm, reading):
    """
    function to perform "spritz"
    """
    secondPerWord = 60.0 / wpm
    sleepInterval = secondPerWord 
    maxLength = find_max(reading)

    for word in reading:
        if word == "<pause>":
            time.sleep(sleepInterval * 10)
            continue

        wordSleepInterval = 0.01 * len(word)

        time.sleep(sleepInterval + wordSleepInterval)
        orpConfig = calculate_spaces(word, maxLength)
        print_word(word, orpConfig)

def main(wpm, article):
    """
    Main function
    """
    reading = parse_article(article)
    spritz(wpm, reading)

if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1]:
        try:
            wpm = int(sys.argv[1])
        except:
            print ("<wpm> need to be an integer")
            exit(1)
    else:
        wpm = 250

    article = ""
    
    for line in fileinput.input(sys.argv[2:]):
        article += line
    
    main(wpm, article)
