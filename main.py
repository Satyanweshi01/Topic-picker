from random import choice
import tkinter

def get_debate_topic():
    with open("debate_topics.txt") as dt_file:
        content = dt_file.readlines()
        canvas.itemconfig(topic_text,text=choice(content)) 

def add_debate_topic(topic):
    with open("debate_topics.txt",'a') as dt_file:
        dt_file.write(f"{topic}\n")


def get_jam_topic():
    with open("jam_topics.txt") as jam_file:
        content = jam_file.readlines()
        canvas.itemconfig(topic_text,text=choice(content)) 

def add_jam_topic(topic):
    with open("jam_topics.txt",'a') as jam_file:
        jam_file.write(f"{topic}\n")

# new_debate_topic = input("Enter new debate topic:")
# add_debate_topic(new_debate_topic)
# print(get_debate_topic())

window = tkinter.Tk()
window.title("Topic picker")
window.minsize(width=350,height=350)
window.config(bg="sienna3")



program_name = tkinter.Label(text="Pick and Speak",font=("Times new roman",32,"italic"),bg="sienna3",fg="spring green")
program_name.pack()

canvas = tkinter.Canvas(width=300,height=50)
topic_text =canvas.create_text(100,45,text = "",font=("Arial",16,"bold"),fill="spring green")
canvas.pack()

new_debate_topic_button = tkinter.Button(text="New debate topic",command=get_debate_topic)
new_debate_topic_button.pack()

new_jam_topic_button = tkinter.Button(text="New jam topic",command=get_jam_topic)
new_jam_topic_button.pack()

add_debate_topic_button = tkinter.Button(text="Add debate topic")
add_debate_topic_button.pack()

add_jam_topic_button = tkinter.Button(text="Add jam topic")
add_jam_topic_button.pack()

window.mainloop()