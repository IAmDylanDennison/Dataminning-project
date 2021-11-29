
from chartFunction import pregnancy_age_plot, BMI_age_plot, overall_plot, pedigree_insulin_plot, pedigree_pregancies_plot
from chartFunction import beforeTable, afterTable,trainTable, Pedigree_age_plot, uploadFileFromUser
from tkinter import *


def startGui():
    global window
    # The main tkinter window
    window = Tk()
    # setting the title and 
    window.title('Diabetics in Pregnant women')
    # setting the dimensions of 
    # the main window
    window.geometry("1000x1000")
    
        #place the buttons
    pregnancy_age_plot_button = Button(master = window, command = pregnancy_age_plot, height = 2,  width = 25, font=("Courier", 8), text = "Plot Pregnancy & Age")
    BMI_age_plot_button = Button(master = window, command = BMI_age_plot, height = 2,  width = 25, font=("Courier", 8), text = "Plot BMI & Age")
    outcome_button = Button(master = window, command = overall_plot, height = 2,  width = 25, font=("Courier", 8), text = "Outcome Plot")
    Pedigree_age_button = Button(master = window, command = Pedigree_age_plot, height = 2,  width = 25, font=("Courier", 8), text = "Predigree & Age Plot")
    insulin_pedigree_plot_button = Button(master = window, command = pedigree_insulin_plot, height = 2,  width = 25, font=("Courier", 8), text = "insulin and pedigree")
    pedigree_pregancies_plot_button = Button(master = window, command = pedigree_pregancies_plot, height = 2,  width = 25, font=("Courier", 8), text = "pedigree and pregancies")
    userInputFileButton = Button(master = window, command=uploadFileFromUser, height = 5,  width = 40, font=("Courier", 8), text = "Upload File for Decision Tree")
    trainTableButton = Button(master = window, command=trainTable, height = 5,  width = 40, font=("Courier", 8), text = "Training Data Table")
    beforeDecTree = Button(master = window, command=beforeTable, height = 5,  width = 40, font=("Courier", 8), text = "Before Tree")
    afterDecTree = Button(master = window, command=afterTable, height = 5,  width = 40, font=("Courier", 8), text = "After Tree")
    
    # into the window
    userInputFileButton.pack()
    outcome_button.pack()
    pregnancy_age_plot_button.pack()
    BMI_age_plot_button.pack()
    Pedigree_age_button.pack()
    insulin_pedigree_plot_button.pack()
    pedigree_pregancies_plot_button.pack()
    trainTableButton.pack()
    beforeDecTree.pack()
    afterDecTree.pack()
    # run the gui
    window.mainloop()
    



if __name__ == '__main__':
    startGui()
    