#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

import sys
import time
import math
import fileinput

def to_unicode(text, encoding='utf-8'):
    """Convert ``text`` to unicode using ``encoding``.

    :param text: string object to convert to ``unicode``
    :type text: ``str`` or ``unicode``
    :returns: string object as unicode object
    :rytpe: ``unicode``
    """
    if isinstance(text, basestring):
        if not isinstance(text, unicode):
            text = unicode(text, encoding)
    return text

##################################################
#   ORP Functions                                #
##################################################

def get_orp(integer):
    """Get Optimal Reading Position (ORP) given ``integer``.
    ORP is slightly left of center.

    :param integer: length of string object to calculate ORP
    :type integer: ``integer``
    :returns: value of ORP
    :rytpe: ``integer``
    """
    percentage = 0.45
    return int(math.ceil(integer * percentage))

def calculate_spaces(word, max_length):
    """Determine buffer spaces for ``word`` given the ``max_length``.

    :param word: string object for calculation
    :type word: ``unicode``
    :param max_length: value of longest word in full text
    :type max_length: ``integer``
    :returns: word's ORP, number of prefix spaces, and number of post spaces
    :rytpe: ``tuple`` of ``integers``
    """
    max_orp = get_orp(max_length)
    orp = get_orp(len(word))
    prefix_space = (max_orp - orp)
    postfix_space = (max_length - len(word) - prefix_space)
    
    return (orp, prefix_space, postfix_space)

def find_max(reading):
    """
    Find longest word in ``reading``.

    :param reading: the full string object to be spritzed
    :type reading: ``unicode``
    :returns: number of characters in the longest word
    :rytpe: ``integer``
    """
    reading = sorted(reading, key=len, reverse=True)
    return len(reading[0])

##################################################
#   Output Functions                             #
##################################################

def insert_color(word, orp):
    """Change color of the ORP letter in ``word`` to red.

    :param word: the word to be color-coded
    :type word: ``unicode``
    :param orp: the index of the ORP letter
    :type orp: ``integer``
    :returns: word with ORP letter in red
    :rytpe: ``unicode``
    """
    color_red = "\033[91m"
    color_restore = "\033[0m"

    chars = list(word)
    chars.insert(orp, color_red)
    chars.insert((orp + 2), color_restore)
    return ''.join(chars)

def print_word(word, orp_config):
    """Pretty print `word` with spritz color formatting

    :param word: the word to be color-coded
    :type word: ``unicode``
    :param orp_config: formatting data for ``word``
    :type orp_config: ``tuple`` of ``integers``
    :returns: Nothing. Prints to console
    :rytpe: ``None``
    """
    (orp, prefix, postfix) = orp_config
    orp = orp - 1           # change for Python list indexing
    print_string = (" " * prefix) + insert_color(word, orp) + (" " * postfix)

    print("\r{}".format(print_string))
    sys.stdout.flush()

##################################################
#   Key Functions                                #
##################################################

def parse_article(article):
    """
    Clean up input ``article`` and insert appropriate pauses.
    
    :param article: the full string object to be spritzed
    :type article: ``unicode``
    :returns: words in ``article``
    :rytpe: ``list``
    """
    remove = (',', '.', '!', '?', '-', ';')

    for char in remove:
        article = article.replace(char, " <pause> ")

    article = article.strip()
    article = article.replace("\n", " <pause> <pause> ")

    return article.split()

def spritz(wpm, reading):
    """"Spritz" the ``reading``.

    :param wpm: words per minute
    :type wpm: ``integer``
    :param reading: the full string object to be spritzed
    :type reading: ``unicode``
    :returns: Nothing. Prints to console
    :rytpe: ``None``
    """
    sleep_interval = (60.0 / wpm)
    max_length = find_max(reading)

    for word in reading:
        if word == "<pause>":
            time.sleep(sleep_interval * 3)
            continue

        word_sleep_interval = 0.01 * len(word)

        time.sleep(sleep_interval + word_sleep_interval)
        orp_config = calculate_spaces(word, max_length)
        #print(word)
        print_word(word, orp_config)

##################################################
#   Main Function                                #
##################################################

def main():
    """Parse command line args and spritz text.
    """
    if len(sys.argv) >= 2 and sys.argv[1]:
        try:
            wpm = int(sys.argv[1])
        except ValueError:
            print ("<wpm> need to be an integer")
            exit(1)
    else:
        wpm = 250

    article = ""
    
    for line in fileinput.input(sys.argv[2:]):
        article += line
    reading = parse_article(article)
    spritz(wpm, reading)

if __name__ == '__main__':
    main()
