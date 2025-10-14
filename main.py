from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
#----------------------------------------------------------------------------#
#Acessar os dados e gerar um DataFrame
data = pandas.read_csv("data/1000_palavras_espanhol_portugues.csv")
#Usar DataFrame.to_dict(orient="records")
to_learn = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = "Espanhol", fill="black")
    canvas.itemconfig(card_word, text = current_card["Es"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="Portugues", fill="white")
    canvas.itemconfig(card_word, text = current_card["Pt"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)




# #-----------------------------------UI-----------------------------------------#

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263, image = card_front_img)
card_title = canvas.create_text(400, 150,text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0,row=0, columnspan=2)

x_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=x_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0,command=next_card)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()