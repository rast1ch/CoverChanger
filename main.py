import image_scraper as i_s
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
from tkinter import *
import webbrowser


root = Tk()
root.resizable(0,0)
root.geometry('300x150')
root.title('music-changer')
el = Entry(root,  width=300)
def spotify_get():
    b = el.get()
    i_s.scrap_to_file(i_s.connect(b))
b = Button(text="Вставить", command=spotify_get, )
el.pack()
b.pack()


if __name__ == '__main__':
    root.mainloop()
