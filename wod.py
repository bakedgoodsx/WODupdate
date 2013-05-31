#!/usr/bin/env python
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import Tk
import grabelist

def openpage():
    a = input("Username: ")
    b = input("Password: ")
    #https://www.drupalgardens.com/user/login

    driver = webdriver.Firefox()
    driver.get("https://www.drupalgardens.com/user/login")
    assert "Log" in driver.title
    namelog = driver.find_element_by_id("edit-name")
    passlog = driver.find_element_by_id("edit-pass")

    namelog.send_keys(a)
    passlog.send_keys(b)
    passlog.send_keys(Keys.RETURN)

    assert "Site" in driver.title
    driver.get("https://www.drupalgardens.com/mysites/1006101/login")
    assert "Equity" in driver.title

    driver.get("http://roundtabletestsite.drupalgardens.com/#overlay=admin/structure/block/manage/block/16/configure%3Fdestination%3Dnode")


def getdef():
    f = open('wodlist.txt', 'r+', encoding='utf-8',errors='ignore')
    a = f.read()
    b = a.split('#')
    f.close()
    f = open('wodlist.txt', 'w', encoding='utf-8',errors='ignore')
    f.truncate()
    if int(b[0])==(len(b)):
        b[0] = '1'
    startpoint = int(b[0])
    b[0] = str(startpoint + 1)  
   
    c = '#'.join(b)
    # c recreates original file structure
    # with the defindex incremented
      
    f.write(c)
    f.close
    # Right now in startpoint we have an index
    # and in b we have an array of strings that will respond
    # to the call of that index. 
    # This is a working loop that iterates thru the list of defs.
    
    # now we need: grabdef and toclip
    defini = b[startpoint]
    grabelist.toclip(defini)



    
getdef()





