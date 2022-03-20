from tkinter import *
from random import randint
import pandas

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=20, bg=BACKGROUND_COLOR, width=1000, height=1300)

# -------------------------------------------Convert CSV data to dict------------------------------------------------- #

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
    words_dict = data.to_dict()
    print(words_dict)
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")  # Reading data from CSV if words to learn doesn't exist
    words_dict = data.to_dict()
    print(words_dict)

# -------------------------------------------------Text on Canvas----------------------------------------------------- #
word_index = 0
eng_or_fre = 0


def random_number_gen():
    global word_index
    word_index = randint(0, len(data["French"]))


def french_text_gen():
    global eng_or_fre
    word.config(width=400, height=200, bg="white", highlightthickness=0)
    word.create_text(200, 30, text="French", font=("Avenir", 30, "normal"), fill="grey")
    word.create_text(200, 120, text=words_dict["French"][word_index], font=("Avenir", 40, "bold"), fill="black")
    eng_or_fre = 0
    window.after(5000, func=flip)


def english_text_gen():
    global eng_or_fre
    word.config(width=400, height=200, bg="#83C4AE", highlightthickness=0)
    word.create_text(200, 30, text="English", font=("Avenir", 30, "normal"), fill="yellow")
    word.create_text(200, 120, text=words_dict["English"][word_index], font=("Avenir", 40, "bold"), fill="white")
    eng_or_fre = 1


# -----------------------------------------Word on button click generator--------------------------------------------- #


def right_word_gen():
    words_dict["French"].pop(word_index)  # Removing known words from dict
    words_dict["English"].pop(word_index)
    print(words_dict)
    learnt_data = pandas.DataFrame(words_dict)
    learnt_data.to_csv("./data/words_to_learn.csv", index=False)
    word.delete('all')
    random_number_gen()
    canvas.itemconfig(canvas_image, image=front_card_img)
    french_text_gen()


def wrong_word_gen():
    word.delete('all')
    random_number_gen()
    canvas.itemconfig(canvas_image, image=front_card_img)
    french_text_gen()


# --------------------------------------------------Card Flip--------------------------------------------------------- #

def flip():
    global eng_or_fre
    if eng_or_fre == 0:
        word.delete('all')
        canvas.itemconfig(canvas_image, image=back_card_img)
        english_text_gen()


# -----------------------------------------Application Design/Layout-------------------------------------------------- #

# Canvas Image - Card
canvas = Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="./images/card_front.png")
canvas_image = canvas.create_image(400, 300, image=front_card_img)
back_card_img = PhotoImage(file="./images/card_back.png")

# Canvas Text
word = Canvas(width=400, height=200, bg="white", highlightthickness=0)
french_text_gen()

# Buttons
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")
right_button = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                      command=right_word_gen)
wrong_button = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                      command=wrong_word_gen)

# Grids
canvas.grid(column=0, row=0, columnspan=2)
right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)
word.grid(column=0, row=0, columnspan=2)

window.mainloop()
