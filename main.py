from random import choice
import tkinter

# core functionality
# core functions
# getting hold on the topics from the debate_topics.txt
def get_debate_topic():
    with open("debate_topics.txt") as dt_file:
        content = dt_file.readlines()
        canvas.itemconfig(topic_text,text=choice(content)) 

# adding new topic to the debate_topics.txt
def add_debate_topic(topic):
    with open("debate_topics.txt",'a') as dt_file:
        dt_file.write(f"{topic}\n")

# getting hold on the topics from the jam_topics.txt
def get_jam_topic():
    with open("jam_topics.txt") as jam_file:
        content = jam_file.readlines()
        canvas.itemconfig(topic_text,text=choice(content)) 

# adding new topic to the debate_topics.txt
def add_jam_topic(topic):
    with open("jam_topics.txt",'a') as jam_file:
        jam_file.write(f"{topic}\n")

# secondary window for the dabate topic input
def debate_input_win():
    debate_topic_win = tkinter.Toplevel(window)
    debate_topic_win.title("New debate topic")
    debate_topic_win.geometry("200x80") # widthxheight

    label = tkinter.Label(debate_topic_win,text="Write the topic")
    label.pack()

    input_box = tkinter.Entry(debate_topic_win)
    input_box.pack()

    def submit():
        data = input_box.get()
        if data != "":
            add_debate_topic(data)  
            debate_topic_win.destroy()
    
    submit_button = tkinter.Button(debate_topic_win, text="submit", command= submit)
    submit_button.pack()

# secondary window for the jam topic input
def jam_input_win():
    jam_topic_win = tkinter.Toplevel(window)
    jam_topic_win.title("New jam topic")
    jam_topic_win.geometry("200x80") # widthxheight

    label = tkinter.Label(jam_topic_win,text="Write the topic")
    label.pack()

    input_box = tkinter.Entry(jam_topic_win)
    input_box.pack()

    def submit():
        data = input_box.get()
        if data != "":
            add_jam_topic(data)
            jam_topic_win.destroy()
        
    
    submit_button = tkinter.Button(jam_topic_win, text="submit", command= submit)
    submit_button.pack()

# main window
window = tkinter.Tk()
window.title("Topic picker")
window.minsize(width=350,height=350)
window.config(bg="sienna3")



program_name = tkinter.Label(text="Pick and Speak",font=("Times new roman",32,"italic"),bg="sienna3",fg="spring green")
program_name.pack()

# this is the place where we are going to see the output
canvas = tkinter.Canvas(width=300,height=50)
topic_text =canvas.create_text(100,45,text = "",font=("Arial",16,"bold"),fill="spring green")
canvas.pack()

# getting buttons
new_debate_topic_button = tkinter.Button(text="New debate topic",command=get_debate_topic)
new_debate_topic_button.pack()

new_jam_topic_button = tkinter.Button(text="New jam topic",command=get_jam_topic)
new_jam_topic_button.pack()

# adding buttons
add_debate_topic_button = tkinter.Button(text="Add debate topic",command=debate_input_win)
add_debate_topic_button.pack()

add_jam_topic_button = tkinter.Button(text="Add jam topic",command=jam_input_win)
add_jam_topic_button.pack()

# window ends
window.mainloop()