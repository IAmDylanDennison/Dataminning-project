
import csv
from chartFunction import *
from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt 

filename = "diabetes.csv"
outcomes = []
count = 0
## positive attributes
pos_preg = []
pos_glucose = []
pos_blood_pres = []
pos_skin_thickness = []
pos_insulin = []
pos_BMI = []
pos_pedigree = []
pos_age = []
pos_outcomes = []
pos_cases = 0
            
## negative attributes
neg_preg = []
neg_glucose = []
neg_blood_pres = []
neg_skin_thickness = []
neg_insulin = []
neg_BMI = []
neg_pedigree = []
neg_age = []
neg_outcomes = []
neg_cases = 0

def uploadFileFromUser(event=None):
    userFile = filedialog.askopenfilename()
    print('Selected: ', userFile)
    global filename
    filename = userFile
    getData(filename)



def getData(userfile):
    with open(userfile,'r') as file:
            reader = csv.DictReader(file)

            global outcomes
            global count
            ## positive attributes
            global pos_preg
            global pos_glucose
            global pos_blood_pres
            global pos_skin_thickness
            global pos_insulin
            global pos_BMI
            global pos_pedigree
            global pos_age
            global pos_outcomes
            global pos_cases
            
            ## negative attributes
            global neg_preg
            global neg_glucose
            global neg_blood_pres
            global neg_skin_thickness
            global neg_insulin
            global neg_BMI
            global neg_pedigree
            global neg_age
            global neg_outcomes
            global neg_cases

            # outcomes
            outcomes = [0,1]
            # reads each row in csv file
            for row in reader:
                #collects the attributes of women who tested positive
                if row['Outcome'] == '1':
                    pos_preg.append(int(row['Pregnancies']))
                    pos_glucose.append(int(row['Glucose']))
                    pos_blood_pres.append(int(row['BloodPressure']))
                    pos_skin_thickness.append(int(row['SkinThickness']))
                    pos_insulin.append(int(row['Insulin']))
                    pos_BMI.append(float(row['BMI']))
                    pos_pedigree.append(float(row['DiabetesPedigreeFunction']))
                    pos_age.append(int(row['Age']))
                    pos_outcomes.append(int (row['Outcome']))

                    outcomes.append(int (row['Outcome']))
                    pos_cases += 1
        
                    
                    

            #collects the attributes of women who tested negative
                if row['Outcome'] == '0':
                    neg_preg.append(int(row['Pregnancies']))
                    neg_glucose.append(int(row['Glucose']))
                    neg_blood_pres.append(int(row['BloodPressure']))
                    neg_skin_thickness.append(int(row['SkinThickness']))
                    neg_insulin.append(int(row['Insulin']))
                    neg_BMI.append(float(row['BMI']))
                    neg_pedigree.append(float(row['DiabetesPedigreeFunction']))
                    neg_age.append(int(row['Age']))
                    neg_outcomes.append(int(row['Outcome']))

                    outcomes.append(int (row['Outcome']))
                    neg_cases += 1

                if count == 500:
                    break
                count += 1
     
def overall_plot():
    x =[0,1]
    y =[]
    y.append(neg_cases)
    y.append(pos_cases)
    # creating a hisogram of all cases
    plt.figure(figsize=(10,6))
    plt.bar(x, height = y,  width = 0.1,color =['red', 'green'])
    #plt.hist(outcomes,bins =2,color ='lightblue')

    
    
    

    ## labeling and titling the graph
    plt.title("Diabetics in Pregnant women")
    plt.xlabel("Outcome")
    plt.ylabel("Cases")
    #plt.legend(["Diabetics","No Diabetics"])

    #plt.xticks(outcomes, ['0','1'])
    ## setting the axis values
    xaxis = [0,1]
    #y= [100,200,300,400,500]
    
    plt.xticks(x,xaxis)
    #plt.yticks(y,y)

 
    plt.show()
    
    


def pregnancy_age_plot():

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
    

#creates plot based on pedigree and insulin
def pedigree_insulin_plot():
    
    ## creating the scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(pos_insulin, pos_pedigree, c='green')
    plt.scatter(neg_insulin, neg_pedigree, c='red')
    
    ## labeling and titling the graph
    plt.title("Diabetics in Pregnant women")
    plt.xlabel("insulin")
    plt.ylabel("pedigree function")
    plt.legend(["Diabetics","No Diabetics"])
    

    ## setting the axis values
    x = [0,100,200,300,400,500,600,700,800,900]
    y= [0,0.2,0.4,0.6,0.8,1,1.2,1.4,1.6,1.8,2.0,2.2,2.4]
    
    plt.xticks(x,x)
    plt.yticks(y,y)

    #plt.plot(x, y)
    plt.show()
################################
#pedigree and preganices plot
def pedigree_pregancies_plot():
    
    ## creating the scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(pos_preg, pos_pedigree, c='green')
    plt.scatter(neg_preg, neg_pedigree, c='red')
    
    ## labeling and titling the graph
    plt.title("Diabetics in Pregnant women")
    plt.xlabel("pregancies")
    plt.ylabel("pedigree function")
    plt.legend(["Diabetics","No Diabetics"])
    

    ## setting the axis values
    x= [0,3,6,9,12,15,17]
    y= [0,0.2,0.4,0.6,0.8,1,1.2,1.4,1.6,1.8,2.0,2.2,2.4]
    
    plt.xticks(x,x)
    plt.yticks(y,y)

    #plt.plot(x, y)
    plt.show()
  ########################
def BMI_age_plot():
    
    ## creating the scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(pos_age, pos_BMI, c='green')
    plt.scatter(neg_age, neg_BMI, c='red')
    
    ## labeling and titling the graph
    plt.title("BMI in Pregnant women")
    plt.xlabel("Age")
    plt.ylabel("BMI")
    plt.legend(["Diabetics","No Diabetics"])
    

    ## setting the axis values
    x = [20,30,40,50,60,70,80]
    y= [0,20,25,30,35,40,45,50,60]
    
    plt.xticks(x,x)
    plt.yticks(y,y)

    #plt.plot(x, y)
    plt.show()

def Pedigree_age_plot():
    
    ## creating the scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(pos_age, pos_pedigree, c='green')
    plt.scatter(neg_age, neg_pedigree, c='red')
    
    ## labeling and titling the graph
    plt.title("Pedigree in Pregnant women")
    plt.xlabel("Age")
    plt.ylabel("Pedigree")
    plt.legend(["Diabetics","No Diabetics"])
    

    ## setting the axis values
    x = [20,30,40,50,60,70,80]
    y= [0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00, 1.10, 1.20, 1.30, 1.40, 1.50, 1.60, 1.70, 1.80, 1.90, 2.00]
    
    plt.xticks(x,x)
    plt.yticks(y,y)

    #plt.plot(x, y)
    plt.show()