import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from playsound import playsound
import pygame
from pygame import mixer
import os
import time



PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

setup()

def musicWindow():

    window=Tk()

    window.title('Messenger')
    window.geometry("300x300")
    window.configure(bg='LightSkyBlue')

    global listbox
    global selectLabel 


def resume():
    global song_selected
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()

def pause():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()


def openWindow():

    window=Tk()

    window.title('Messenger')
    window.geometry("500x350")


    selectLabel = Label(window,text="select song",bg='LightSKyBlue',font=('Calibri',0))
    selectLabel.place(x=2,y=1)

    ResumeButton = Button(window,text="Resume",width=10,bd=1,bg='SkyBlue',font=('Calibri',10),command=resume)
    ResumeButton.place(x=30,y=250)

    PauseButton = Button(window,text="Pause",width=10,bd=1,bg='SkyBlue',font=('Calibri',10),command=pause)
    PauseButton.place(x=200,y=250)


    
   
