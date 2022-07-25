"""Init dre2 file - Select zip file | Read zip | Read images | Center images"""
# pylint: disable=no-member
# Up line to ignore pygame
# pylint: disable=line-too-long
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
        initialdir='/AtualFolder', #um nome qualquer leva para pasta de execução do ficheiro
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
                        with ZipFile(file[0], 'r') as zips:
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


def readfile(filesname):
    """Read first excel"""
    readexcel = pd.read_excel(filesname) #Ficheiro Excel a ser li-do
    data = {
        "readx": list(readexcel['Position_X']),
        "ready": list(readexcel['Position_Y']),
        "readvel": list(readexcel['Speed']),
        "readbrake": list(readexcel['Brake']),
        "readthrottle": list(readexcel['Throttle']),
        "readtick1": list(readexcel['Tick']),
        "readsteer": list(readexcel['Steer']),
        "readgear": list(readexcel['Gear'])
    }
    return data


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

# Verificar se o zip é o correto(no caso de ser outro zip, zip so com um excel, zip sem excel)
def verifyfiles(fileslist):
    """Verify files"""
    again = True
    while again is True:
        try:
            data1input = readfile(fileslist[0])
            data2input = readfile(fileslist[1])
            again = False
            return data1input, data2input
        except IndexError: #so except
            again = True
            root1=tk.Tk()
            showinfo(
                    title='Selected Files',
                    message="Choose correct ZIP file!!"
                )
            root1.destroy()
            fileslist = okfiles()
