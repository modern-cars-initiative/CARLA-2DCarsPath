"""Init dre2 file - Select zip file | Read zip | Read images | Center images"""
import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from zipfile import ZipFile
import pygame
import pandas as pd

def select_files():
    """Select zip file"""
    filetypes = (
        ('ZIP file', '*.zip'),
        ('All files', '*.*')
    )
    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/AtualFolder', # um nome qualquer leva para a pasta onde esta a ser executado o ficheiro py
        filetypes=filetypes)
    return filenames


def okfiles():
    """OK FILES"""
    checkfiles = False
    root=tk.Tk()
    while not checkfiles:
        file = select_files()
        checkfilenames = [file[0]]
        checkfileexts = ['.zip']
        if len(file) == 1:
            #check if file is zip
            for name in checkfilenames:
                for ext in checkfileexts:
                    if name.endswith(ext):
                        checkfiles = True
                        zips = ZipFile(file[0], 'r')
                        zipfiles = zips.namelist()
                        zips.extractall(".")
                        root.destroy()
                        return zipfiles
                    else:
                        showinfo(
                            title='Selected Files',
                            message="You only can choose a ZIP file!"
                        )
        else:
            showinfo(
                title='Selected Files',
                message="You need to choose one ZIP file!"
            )


def readfile1():
    """Read first excel"""
    readexcel = pd.read_excel(FILESLIST[0]) #Ficheiro Excel a ser li-do
    data1 = {}
    data1 = {
        "readx": list(readexcel['Position_X']),
        "ready": list(readexcel['Position_Y']),
        "readvel": list(readexcel['Speed']),
        "readbrake": list(readexcel['Brake']),
        "readthrottle": list(readexcel['Throttle']),
        "readtick1": list(readexcel['Tick']),
        "readsteer": list(readexcel['Steer']),
        "readgear": list(readexcel['Gear'])
    }
    #data[readbrake]
    return data1

def readfile2():
    """Read second excel"""
    readexcel2 = pd.read_excel(FILESLIST[1]) #Ficheiro Excel a ser li-do
    data2 = {}
    data2 = {
        "readx2": list(readexcel2['Position_X']),
        "ready2": list(readexcel2['Position_Y']),
        "readvel2": list(readexcel2['Speed']),
        "readbrake2": list(readexcel2['Brake']),
        "readthrottle2": list(readexcel2['Throttle']),
        "readtick2": list(readexcel2['Tick']),
        "readsteer2": list(readexcel2['Steer']),
        "readgear2": list(readexcel2['Gear'])
    }
    return data2

def readimages():
    """Read images"""
    image1read = pygame.image.load('IMG/miniCarro.png') #Carro
    image2read = pygame.image.load('IMG/miniEstrela.png') #Estrela
    return image1read, image2read

def centerimages(screenin):
    """Center path on screen"""
    center_originread = lambda p: (p[0] + (screenin.get_width() / 2) - 250, p[1] + screenin.get_height() / 2) #Começar a desenhar no centro !!??
    center_origin2read = lambda p: (p[0] + (screenin.get_width() / 2) + 320 , p[1] + screenin.get_height() / 2)
    return center_originread, center_origin2read

#Main

FILESLIST = okfiles()

# Verificar se o zip é o correto(no caso de ser outro zip, zip so com um excel, zip sem excel)
AGAIN = True
while AGAIN is True:
    try:
        data1input = readfile1()
        data2input = readfile2()
        AGAIN = False
        pygame.init()
        screen = pygame.display.set_mode([1280, 720], 0, 32)
    except IndexError: #so except
        AGAIN = True
        root1=tk.Tk()
        showinfo(
                title='Selected Files',
                message="Choose correct ZIP file!!"
            )
        root1.destroy()
        FILESLIST = okfiles()

image1, image2 = readimages()
center_origin, center_origin2 = centerimages(screen)
