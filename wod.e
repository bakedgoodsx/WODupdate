
Word of the Day .e
pseudocode blueprint for wod.py

1. Every day: login to drupalgardens.
2. Run wod.py


wod.py:

def loadword
    open file
    get number (first two digits in file)
    extract word+def with that number
    increment number
    save file
    return word+def

def pasteword
    grab webform "http://roundtabletestsite.drupalgardens.com/#overlay=admin/structure/block/manage/block/16/configure%3Fdestination%3Dnode"
    paste loadword() into webform
    click submit

Functions to figure out:
1. loadword already easy
2. pasteword not clear

Work on pasteword



