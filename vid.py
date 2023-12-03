from tkinter import *
from pytube import YouTube

fen = Tk()
def recup():
    return entre.get()

def go():
    url = recup()
    
    try:
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download()
        print("La vidéo a été téléchargée avec succès.")
    except Exception as e:
        print("Une erreur s'est produite lors du téléchargement de la vidéo :", str(e))
    print(url)

fen.title("Video")
fen.geometry("400x400")
fen.resizable(width=False, height=False)
fen.config(bg='black')
frame = Frame(fen, bg="black")
frame.pack(expand=YES)
label = Label(frame, text='Votre lien', font=("courrier", 11),bg='black', fg="white")
label.pack()
entre = Entry(frame)
entre.pack()
bt = Button(fen, text="Télécharger", font=("arial", 20), bg="grey", fg="black", command=go)
bt.pack(pady=50)



fen.mainloop()

