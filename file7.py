import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import csv
import tweepy
from tweepy import OAuthHandler
import json

window = Tk()
window.title("Welcome to Likegeeks app")
window.geometry('350x200')
def downloaddata():
    ck = 'tiHCLjJ2rb0ZdZIj5spXUxjm6'
    cs = '3E8ltyOuw2uFOwdcy7G8pmEsibPlFMfhlBsjcgOjHLWuPIohUv'
    at = '1079684161093423104-f9hfR7mue3JtMFEYwINVvk6OxGoMWQ'
    ats = 'LDCHRqmQOFfzsSlBqVq8LTgS7rm9VelKnUugJejyZyY2m'

    auth = tweepy.OAuthHandler(ck, cs)
    auth.set_access_token(at, ats)
    api = tweepy.API(auth)

    public_tweets = api.home_timeline()
    
    tweet_file = open('tweet3.csv', 'w', encoding="utf-8")
    tweet_file.write("Created at,Id")
    for x in public_tweets:
        tweet_file.write(str(x.created_at))
        tweet_file.write("," + str(x.id_str) + "\n")
    tweet_file.close()
    messagebox.showinfo("Data Downloaded")
def createtable():
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="prema")
    mycursor = mydb.cursor()
    sql = "CREATE TABLE tweet1(created_at DATE,id VARCHAR(20))"
    messagebox.showinfo("Table Created")
    mycursor.execute(sql)
    mydb.commit()
def loaddata():
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="prema")
    mycursor = mydb.cursor()
    sql = "load infile 'rC:/Users/roh.mishra/PycharmProjects/TwitterDataAnalysis/tweet3.csv' into table tweet1 fields terminated by ','"
    messagebox.showinfo("Data loaded")
    mycursor.execute(sql)
    mydb.commit()
def sortdata():
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="prema")
    mycursor = mydb.cursor()
    sql = "select date(created_at),count(*) from tweet group by date(created_at) into outfile 'rC:/Users/roh.mishra/PycharmProjects/TwitterDataAnalysis/tweet4.csv' fields terminated by ','"
    messagebox.showinfo("data sorted")
    mycursor.execute(sql)
    mydb.commit()
def Gplot():
    x = []
    y = []
    with open('tweet1.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for i in plots:
            x.append(str(i[0]))
            y.append(str(i[1]))
    plt.plot(y, x, marker='o')
    plt.title('Data from CSV file: People and Date')

    plt.xlabel('Number of tweets')
    plt.ylabel('at created date')
    plt.show()
    messagebox.showinfo("Graph Plotted")
btn = Button(window, text="Download Data", command=downloaddata)
btn.grid(column=2, row=4)
btn1 = Button(window, text="Create Table", command=createtable)
btn1.grid(column=4, row=4)
btn2 = Button(window, text="Load Data", command=loaddata)
btn2.grid(column=6, row=4)
btn3 = Button(window, text="Sort Data", command=sortdata)
btn3.grid(column=8, row=4)
btn4 = Button(window, text="Plot Data", command=Gplot)
btn4.grid(column=10, row=4)
window.mainloop()
