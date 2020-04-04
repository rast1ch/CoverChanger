import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import bs4 as bs4
import requests
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error

def connect(url):
    global result
    r = requests.get(url)
    if str(r.status_code) == '200':
        soup = bs4.BeautifulSoup(r.content, 'lxml')
        return soup
    else:
        print("Unknown Error")
        return 0


def scrap_to_file(soup):
    soup = soup.findAll('img')
    for url in soup:
        result_img = url['src']
        result_name = url['alt']
    result_name = result_name.replace(" ", "_")
    img = requests.get(result_img)
    img_file = open(result_name + '.jpg', 'wb')
    img_file.write(img.content)
    img_file.close
    return 1

def image():
    global x
    x = filedialog.askopenfilename(initialdir = "/",title = "Select image",filetypes = [("jpeg files","*.jpg")])
    return x


def audio():
    global y
    y = filedialog.askopenfilename(initialdir = "/",title = "Select mp3",filetypes = [("mp3 files","*.mp3")])
    return y

def job(x,y):
    audio = MP3(y, ID3=ID3)
    try:
        audio.add_tags()
    except error:
        pass
    audio.tags.add(APIC(mime='image/jpeg',type=3,desc=u'Cover',data=open(x,'rb').read()))
    audio.save()


root = tk.Tk()
root.resizable(0,0)
root.geometry('300x150')
root.title('music-changer')
url= tk.Entry(root,  width=300)
def spotify_get():
    b = url.get()
    scrap_to_file(connect(b))
image_download= tk.Button( command=spotify_get,text="image download")
url.pack()
image_download.pack()

def change():
    job(image(), audio())

button3 = ttk.Button(root, text="Change", command=change)
button3.pack()
#button4 = ttk.Button(root, text="Clear", command=clear)


if __name__ == '__main__':
    root.mainloop()
