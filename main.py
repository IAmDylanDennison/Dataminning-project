
from chartFunction import pregnancy_age_plot, BMI_age_plot, overall_plot, pedigree_insulin_plot, pedigree_pregancies_plot, Pedigree_age_plot, uploadFileFromUser,getData, filename
from tkinter import *

import pandas 
from sklearn import metrics

from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import MinMaxScaler
import sys

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
    #refreshGuiButton = Button(master = window, command=refreshGUi, height = 5,  width = 40, font=("Courier", 8), text = "Refresh Gui after Uploading of File")

    # into the window
    userInputFileButton.pack()
    outcome_button.pack()
    pregnancy_age_plot_button.pack()
    BMI_age_plot_button.pack()
    Pedigree_age_button.pack()
    insulin_pedigree_plot_button.pack()
    pedigree_pregancies_plot_button.pack()
    #refreshGuiButton.pack()
    # run the gui
    window.mainloop()
    

#use pandas to print CSV file on terminal 
diabetesInput = pandas.read_csv("diabetes.csv", delimiter=",")
#print(diabetesInput)
diabetesFactors = diabetesInput[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI','DiabetesPedigreeFunction','Age']].values 
diabetesOutcome = diabetesInput['Outcome']
#print(diabetesOutcome[0:6])
#print(diabetesFactors[0:6])
diabetesInput_train, diabetesInput_test, diabetesOutcome_train, diabetesOutcome_test = train_test_split(diabetesFactors, diabetesOutcome, test_size=0.3, random_state=4)

print("The input Type is" + str(type(diabetesInput_test)))

#print(diabetesInput_train.shape)
#print(diabetesInput_test.shape)
print(diabetesOutcome_train.shape)
print(diabetesOutcome_test.shape)

diabetesTree = DecisionTreeClassifier(criterion="entropy", max_depth=4) # entropy makes the decision on a yes or no

diabetesTree.fit(diabetesInput_train, diabetesOutcome_train)
prediction = diabetesTree.predict(diabetesInput_test)


#addPrediction = list(prediction)
#print(addPrediction)
print(prediction)
print("\nDecision Trees's Accuracy: ", metrics.accuracy_score(diabetesOutcome_test, prediction))


if __name__ == '__main__':
    startGui()
    