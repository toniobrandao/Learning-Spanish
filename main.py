from tkinter import *
from pandas import *
import random
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- RANDOM WORD MECHANISM ------------------------------- #

words_df = read_csv('data/words.csv', delimiter=";")
words_dict = words_df.to_dict(orient="records")
current_card = random.choice(words_dict)
random_number = 0
print(words_dict)

def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_dict)
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word,text = current_card["Spanish"], fill="black")
    canvas.itemconfig(card_img,image=card_front_img)

    flip_timer = window.after(3000, flip_card)

def is_known():
    words_dict.remove(current_card)
    print(len(words_dict))
    data = DataFrame(words_dict)
    print(data)
    data.to_csv("data/words_to_learn.csv")

# ---------------------------- FLIPPING THE CARD ------------------------------- #

def flip_card():
    global current_card
    print(f"Antonio {card_word}")
    canvas.itemconfig(card_title,text="Portuguese",fill="white")
    canvas.itemconfig(card_word,text = current_card["Portuguese"],fill="white")
    canvas.itemconfig(card_img,image=card_back_img)


# ---------------------------- UI SETUP ------------------------------- #

#Creating a new window and configurations
window = Tk()

window.title("Spanish Course")


window.config(padx=50,pady=50,bg =BACKGROUND_COLOR)

canvas = Canvas(width=800,height=526)
canvas.config(bg =BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

card_img = canvas.create_image(400,263,image = card_front_img)
#https://stackoverflow.com/questions/18137313/python-canvas-object-coords-inverted
card_title = canvas.create_text(400,150, text ="text", font = ("Arial",40,"italic"))
card_word = canvas.create_text(400,263, text ="word", font = ("Arial",40,"bold"))
canvas.grid(row=0,column=0,columnspan=2)



#Buttons
right_img = PhotoImage(file="images/right.png")
correct_btn = Button(image=right_img, highlightthickness=0, command=next_card)
correct_btn.grid(row=1,column=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0 ,command=next_card )
wrong_btn.grid(row=1,column=0)



flip_timer = window.after(3000, flip_card)
next_card()
window.mainloop()