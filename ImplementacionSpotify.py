#Diego García, Oskar Villa
#June 2022
import eyed3
import os, pygame
import random
import Functions
import createSongs
#import retoOLED
#import retoUART
#import retoOLED

from PyQt5 import QtGui, QtCore
from Spotify import *

from pygame import mixer

pygame.mixer.init()
if not pygame.font: print ('Warning, fonts disabled')
if not pygame.mixer: print ('Warning, sound disabled')


class Ui_Dialog(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.songs = createSongs.getSongs()
        self.images = createSongs.getImages()
        self.currentSong = 0
        #Flags 
        self.random = False
        self.repeat = False
        self.isPaused = False
        self.timer = QtCore.QTimer(self)
        self.timer.start(100)
        self.setupUi(self)
        
        self.timer.timeout.connect(lambda: self.checkMixerStatus())
        self.button_FF.clicked.connect(lambda : self.nextPressed(False))
        self.button_Play.clicked.connect(lambda :self.playPressed(False))
        self.button_Random.clicked.connect(lambda : self.randomPressed(False))
        self.button_Repeat.clicked.connect(lambda : self.repeatPressed(False))
        self.button_Rewind.clicked.connect(lambda : self.rewindPressed(False))

        self.listWidget.clear()
        for x in range(len(self.songs)):
            pygame.mixer.music.load(self.songs[x])
            audiofile = eyed3.load(self.songs[x])
            item = str(x) + " " + str(audiofile.tag.title) + " - " + str(audiofile.tag.artist)
            self.listWidget.insertItem(x, item)  

    def changeInformation(self, songTitle, songArtist, albumCover):
        self.label.setStyleSheet("border-image: url(:/newPrefix/"+albumCover+");\n")
        self.label_2.setText(songTitle)
        self.label_3.setText(songArtist)


    def checkMixerStatus(self):
        if Functions.checkMusicEnd():
            self.nextPressed()

    def nextPressed(self, gui):
        if self.random == True:
            self.currentSong = random.randint(0,99)
        else: 
            self.currentSong += 1
            if self.currentSong >= len(self.songs):
                self.currentSong = 0
        self.button_Play.setChecked(True)
        #retoOLED.nextOled()
        self.isPaused, songTitle, songArtist,albumCover = Functions.play(self.songs[self.currentSong], self.isPaused, self.images)
        self.changeInformation(songTitle, songArtist, albumCover)

    def playPressed(self, gui):
        if self.button_Play.isChecked() == True:
            #retoOLED.playOled()
            self.isPaused, songTitle, songArtist,albumCover = Functions.play(self.songs[self.currentSong], self.isPaused, self.images)
            self.changeInformation(songTitle, songArtist, albumCover)
        else:
            #retoOLED.pauseOled()
            self.isPaused = Functions.pause(self.isPaused)
        
    def randomPressed(self, gui):
        #retoOLED.randomOled()
        self.random = not self.random
        self.currentSong = random.randint(0,99)

    def repeatPressed(self, gui):
        #retoOLED.repeatOled()
        self.repeat = not self.repeat
        
    def rewindPressed(self, gui):
        if self.random == True:
            self.currentSong = random.randint(0,99)
        else: 
            self.currentSong -= 1
            if self.currentSong <= 0:
                self.currentSong = len(self.songs) - 1
        self.button_Play.setChecked(True)
        #retoOLED.nextOled()
        self.isPaused, songTitle, songArtist,albumCover = Functions.play(self.songs[self.currentSong], self.isPaused, self.images)
        self.changeInformation(songTitle, songArtist, albumCover)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Ui_Dialog()
    window.show()
    app.exec_()
