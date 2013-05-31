#! /usr/bin/env python

import sys
import sqlite3 as lite
from tkinter import Tk


def toclip(text):
    r =Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(text)
    print("Copied to clipboard: " + text)
    


def cleanup(strung):
    s2 = strung.replace("('","")
    s3 = s2.replace("',)","")
    s4 = s3.strip('[]')
    s5 = s4.replace(" ,", ",")
    return s5 


def grabelist(sector):
    con = None
    try:
        con = lite.connect("C:\\Users\\eblincow\\Dropbox\\joblich\\eq.db")
        cur = con.cursor()
    #    cur.execute("select Email from eq where Sector like " + sector + "%")
        cur.execute("select Email from eq where Sector like '" + sector + "%';")
        ae = cur.fetchall()
        ato = str(ae)
        ate = cleanup(ato)
        toclip(ate)
    
    except lite.Error:
        eo = cur.fetchone()
        print(eo)
        print('Cant connect - Error')
        sys.exit(1)

    finally:
        con.commit()
        if con:
            con.close()


# enter interactive console menu for grabbing emails.
def kickstart():
    alfa = "\n--Please enter the first letter (except Foundations/Faith Communities) of the sector for which you want an email list.\n The email list will be copied to the clipboard and ready to be put into Microsoft Outlook.\n"
    breto = "*A*rts and Humanities\n*B*usiness\n*E*ducation\n*Fa*ith Communities\n*Fo*undations\n*G*overnment\n*H*ealthcare\n*J*udicial System\n*N*on-Profit\n \n Please Enter your selection now: \n"
    aeol = input(alfa + breto)
    grabelist(aeol)
