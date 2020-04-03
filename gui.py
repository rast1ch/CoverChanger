import tkinter as tk
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
import tkinter.ttk as ttk
from tkinter import filedialog
import image_scraper as i_s


root = tk.Tk()
root.resizable(0,0)
root.geometry('300x150')
root.title('music-changer')
url= tk.Entry(root,  width=300)
def spotify_get():
    b = url.get()
    i_s.scrap_to_file(i_s.connect(b))
image_download= tk.Button( command=spotify_get,text="image download")
url.pack()
image_download.pack()

def image():
    global x
    x = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = [("jpeg files","*.jpg")])
    if x:
        global label1
        label1 = ttk.Label(text="Image file loaded successfully").grid(row=1, column=1, padx=4, pady=4, sticky='ew')


def audio():
    global y
    y = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = [("mp3 files","*.mp3")])
    if y:
        global label2
        label2 = ttk.Label(text="Audio file loaded successfully").grid(row=2, column=1, padx=4, pady=4, sticky='ew')


def job():
    audio = MP3(y, ID3=ID3)
    try:
        audio.add_tags()
    except error:
        pass
    audio.tags.add(APIC(mime='image/jpeg',type=3,desc=u'Cover',data=open(x,'rb').read()))
    audio.save()
    global label3
    label3 = ttk.Label(text="Cover art changed successfully").grid(row=3, column=1, padx=4, pady=4, sticky='ew')

button1 = ttk.Button(root, text="Select Image", command=image)
button2 = ttk.Button(root, text="Select Audio", command=audio)
button3 = ttk.Button(root, text="Change", command=job)
button1.pack()
button2.pack()
button3.pack()
#button4 = ttk.Button(root, text="Clear", command=clear)


if __name__ == '__main__':
    root.mainloop()
