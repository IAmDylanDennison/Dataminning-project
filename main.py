import csv

from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import matplotlib.pyplot as plt 

with open('diabetes.csv','r') as file:
    reader = csv.DictReader(file)

    count = 0
    ## positive attributes
    pos_preg = []
    pos_age = []
    
     ## negative attributes
    neg_preg = []
    neg_age = []

    # reads each row in csv file
    for row in reader:
        #collects the age and pregnancies of women who tested positive
        if row['Outcome'] == '1':
            pos_preg.append(int(row['Pregnancies']))
            pos_age.append(int(row['Age']))

      #collects the age and pregnancies of women who tested negative
        if row['Outcome'] == '0':
            neg_preg.append(int(row['Pregnancies']))
            neg_age.append(int(row['Age']))
        if count == 80:
            break
        count += 1

print(pos_age)

def plot():

    ## creating the scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(pos_age, pos_preg, c='green')
    plt.scatter(neg_age, neg_preg, c='red')
    
    ## labeling and titling the graph
    plt.title("Diabetics in Pregnant women")
    plt.xlabel("Age")
    plt.ylabel("Pregnancies")
    plt.legend(["Diabetics","No Diabetics"])
    

    ## setting the axis values
    x = [20,30,40,50,60,70,80]
    y= [0,3,6,9,12,15,17]
    
    plt.xticks(x,x)
    plt.yticks(y,y)

    #plt.plot(x, y)
    plt.show()
  
 

# The main tkinter window
window = Tk()
  
# setting the title and 
window.title('Diabetics in Pregnant women')
  
# setting the dimensions of 
# the main window
window.geometry("500x500")
  
# button that displays the plot
plot_button = Button(master = window, command = plot, height = 2,  width = 10, text = "Plot")
# place the button
# into the window
plot_button.pack()
  
# run the gui
window.mainloop()