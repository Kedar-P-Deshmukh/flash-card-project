from  tkinter import *
import pandas
import  random

BACKGROUND_COLOR = "#B1DDC6"
current_card={}
try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data=pandas.read_csv("data/french_words.csv")
data_dict=data.to_dict(orient="records")

def next_card():
    global current_card,counter
    window.after_cancel(counter)
    try:
        current_card=random.choice(data_dict)
    except :
        mycanvas.itemconfig(title, text="French", fill="black")
        mycanvas.itemconfig(word, text="You got it all!!", fill="black")
        reload_button.grid(column=1, row=1)
    else:
        french_word=current_card["French"]
        mycanvas.itemconfig(title, text="French",fill="black")
        mycanvas.itemconfig(word,text=french_word,fill="black")
        mycanvas.itemconfig(card_bg, image=card_front_img)
        counter = window.after(3000, func=filck)


def is_known():
    try:
        data_dict.remove(current_card)
        data=pandas.DataFrame(data_dict)
        data.to_csv("data/words_to_learn.csv",index=False)
    except:
        pass
    else:
        next_card()
        print(len(data_dict))

def filck():
    english_word = current_card["English"]
    mycanvas.itemconfig(title, text="English",fill="white")
    mycanvas.itemconfig(word, text=english_word,fill="white")
    mycanvas.itemconfig(card_bg,image=card_back)

def reload():
    global data_dict,data
    data = pandas.read_csv("data/french_words.csv")
    data_dict = data.to_dict(orient="records")
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
    reload_button.pack_forget()
window=Tk()
window.title("Flash Cards!!!")
window.config(pady=50,padx=50,bg=BACKGROUND_COLOR)

counter=window.after(3000,func=filck)

mycanvas=Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)

card_front_img=PhotoImage(file="images/card_front.png")
card_back=PhotoImage(file="images/card_back.png")
right=PhotoImage(file="images/right.png")
wroung=PhotoImage(file="images/wrong.png")



card_bg=mycanvas.create_image(405,253, image=card_front_img)
mycanvas.grid(column=0 , row=0,columnspan=3)
title=mycanvas.create_text(400,140,text="Title",font=("arial",30,"italic"))
word=mycanvas.create_text(400,253,text="Word",font=("arial",50,"bold"))

unknow_button=Button(image=wroung,command=next_card)
unknow_button.grid(column=0 , row=1)

know_button=Button(image=right,command=is_known)
know_button.grid(column=2 , row=1)

reload_button=Button(text="Restart",command=reload)


next_card()
window.mainloop()
