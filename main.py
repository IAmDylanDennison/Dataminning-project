
from chartFunction import pregnancy_age_plot, BMI_age_plot, overall_plot, pedigree_insulin_plot, pedigree_pregancies_plot
from chartFunction import beforeTable, afterTable,trainTable, Pedigree_age_plot, getData
from Algo import decTreeAlgo
from tkinter import *
from tkinter import filedialog

accScore = ''
def uploadFileFromUser(event=None):
    userFile = filedialog.askopenfilename()
    print('Selected: ', userFile)
    global filename
    filename = userFile
    getData(filename)
    global accScore
    accScore = str(decTreeAlgo(filename))

def displayAccScore():
    if(accScore != ''):
        treeScore = Label(master = window, text="Accuracy score is: " + accScore, font=("Helvetica", 18))
        treeScore.pack()

def startGui():
    global window
    # The main tkinter window
    window = Tk()
    # setting the title and 
    window.title('Diabetics in Pregnant women')
    # setting the dimensions of 
    # the main window
    window.geometry("1000x800")

    

    #create background
    backgroundImage = PhotoImage(file = "background.png")
    backgroundImageLabel = Label(master = window, image = backgroundImage)
    backgroundImageLabel.place(x=0, y=0)


    #create titles
    plot_label = Label(master = window, text = "Plots", height = 4, width = 10, font = ("Courier", 8))
    file_upload_label = Label(master = window, text = "File Upload", height = 4, width = 15, font = ("Courier", 8))
    table_label = Label(master = window, text = "Tables", height = 4, width = 10, font = ("Courier", 8))
    
    #place the buttons
    pregnancy_age_plot_button = Button(master = window, command = pregnancy_age_plot, height = 2,  width = 25, font=("Courier", 8), text = "Plot Pregnancy & Age")
    BMI_age_plot_button = Button(master = window, command = BMI_age_plot, height = 2,  width = 25, font=("Courier", 8), text = "Plot BMI & Age")
    outcome_button = Button(master = window, command = overall_plot, height = 2,  width = 25, font=("Courier", 8), text = "Outcome Plot")
    Pedigree_age_button = Button(master = window, command = Pedigree_age_plot, height = 2,  width = 25, font=("Courier", 8), text = "Pedigree & Age Plot")
    insulin_pedigree_plot_button = Button(master = window, command = pedigree_insulin_plot, height = 2,  width = 25, font=("Courier", 8), text = "insulin and pedigree")
    pedigree_pregancies_plot_button = Button(master = window, command = pedigree_pregancies_plot, height = 2,  width = 25, font=("Courier", 8), text = "pedigree and pregancies")
    userInputFileButton = Button(master = window, command=uploadFileFromUser, height = 5,  width = 40, font=("Courier", 8), text = "Upload File for Decision Tree")
    trainTableButton = Button(master = window, command=trainTable, height = 5,  width = 30, font=("Courier", 8), text = "Training Data Table")
    beforeDecTree = Button(master = window, command=beforeTable, height = 5,  width = 30, font=("Courier", 8), text = "Before Tree")
    afterDecTree = Button(master = window, command=afterTable, height = 5,  width = 30, font=("Courier", 8), text = "After Tree")
    treeScoreButton = Button(master = window, command = displayAccScore, height = 8,  width = 60, font=("Courier", 8), text = "Display Accuracy Score")

    #outputting accuracy score
    # into the window
    plot_label.place(x = 100, y = 180)
    file_upload_label.place(x = 440, y = 20)
    table_label.place(x = 750, y = 180)
    userInputFileButton.place(x = 350, y = 100)
    outcome_button.place(x = 50, y = 250)
    pregnancy_age_plot_button.place(x = 50, y = 300)
    BMI_age_plot_button.place(x = 50, y = 350)
    Pedigree_age_button.place(x = 50, y = 400)
    insulin_pedigree_plot_button.place(x = 50, y = 450)
    pedigree_pregancies_plot_button.place(x = 50, y = 500)
    trainTableButton.place(x = 680, y = 275)
    beforeDecTree.place(x= 680, y = 375)
    afterDecTree.place(x = 680, y = 475)
    treeScoreButton.place(x = 275, y = 600)
    # run the gui

    
    window.mainloop()
    



if __name__ == '__main__':

    startGui()
    