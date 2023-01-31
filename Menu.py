#Josh Made This Comment In First Commit
from tkinter import *
import Task1 as tk1
import Task2 as tk2
import Task3 as tk3
import Task4 as tk4
import Task5 as tk5

def validate_info(user, password, menu):
    if user == "JoshuaC01" and password == "Password1":
        menu.destroy()
        choice_menu()
    else:
        print("Invalid")

#Password Menu
def password_menu():
    #Create Password Menu
    menu=Tk()

    #Set Title
    title_style=("Comic Sans MS", 20, "bold")
    title=Label(menu, text="Video Games Sales Analysis", font=title_style)
    title.place(relx=.5, rely=.1,anchor= CENTER)
    subtitle_style=("Comic Sans MS", 18, "bold")
    subtitle=Label(menu, text="Login Menu", font=subtitle_style)
    subtitle.place(relx=.5, rely=.18,anchor= CENTER)

    #Create Username
    entry_style=("Comic Sans MS", 12)
    userL=Label(menu, text="Username:", font=entry_style)
    username=StringVar()
    userE=Entry(menu, textvariable=username, font=entry_style, background="#898584")
    userL.place(relx=.26, rely=.3,anchor= CENTER)
    userE.place(relx=.5, rely=.3,anchor= CENTER)

    #Create Password
    passL=Label(menu, text="Password:", font=entry_style)
    password=StringVar()
    passE=Entry(menu, textvariable=password, font=entry_style, background="#898584", show="*")
    passL.place(relx=.26, rely=.4,anchor= CENTER)
    passE.place(relx=.5, rely=.4,anchor= CENTER)

    #Login Button
    login=Button(menu, text="Login", font=entry_style, command= lambda: validate_info(userE.get(), passE.get(), menu))
    login.place(relx=.5, rely=.5, anchor=CENTER)

    #Set dimensions of menu
    menu.geometry("600x600")
    menu.title("Video Games Sales Analysis")
    menu=mainloop()

#Choice Menu
def choice_menu():
    #Create Menu
    menu=Tk()

    #Set Title
    title_style=("Comic Sans MS", 20, "bold")
    title=Label(menu, text="Video Games Sales Analysis", font=title_style)
    title.place(relx=.5, rely=.1,anchor= CENTER)

    #Create buttons
    button_style=("Comic Sans MS", 16)
    bt=Button(menu, text="Average Sales", font=button_style, command=tk1.highest_sales)
    bt.place(relx=.5, rely=.2,anchor= CENTER)

    bt1=Button(menu, text="Top Platforms", font=button_style, command=tk2.top_platforms)
    bt1.place(relx=.5, rely=.3,anchor= CENTER)

    bt2=Button(menu, text="Top 10 Sold Games", font=button_style, command=tk3.top_10)
    bt2.place(relx=.5, rely=.4,anchor= CENTER)

    bt3=Button(menu, text="Top Region Games", font=button_style, command=tk4.top_games_region)
    bt3.place(relx=.5, rely=.5,anchor= CENTER)

    bt4=Button(menu, text="Top Genre Sales", font=button_style, command=tk5.genre_global_sales)
    bt4.place(relx=.5, rely=.6,anchor= CENTER)

    bt5=Button(menu, text="Quit", font=button_style, command=menu.destroy)
    bt5.place(relx=.5, rely=.7,anchor= CENTER)


    #Set dimensions of menu
    menu.geometry("600x600")
    menu.title("Video Games Sales Analysis")
    menu=mainloop()

password_menu()