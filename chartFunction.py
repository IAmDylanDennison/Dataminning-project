
import csv
from chartFunction import *
from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt 
import tkinter.ttk as ttk
from Algo import decTreeAlgo

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
    decTreeAlgo(filename)
    



def getData(filename):
    with open(filename,'r') as file:
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
## before Table Function ############
def beforeTable():

    root = Tk()
    root.title("Python - Import CSV File To Tkinter Table")
    width = 500
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Preg", "Glucose", "BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('Preg', text="Preg", anchor=W)
    tree.heading('Glucose', text="Glucose", anchor=W)
    tree.heading('BloodPressure', text="BloodPressure", anchor=W)
    tree.heading('SkinThickness', text="SkinThickness", anchor=W)
    tree.heading('Insulin', text="Insulin", anchor=W)
    tree.heading('BMI', text="BMI", anchor=W)
    tree.heading('DiabetesPedigreeFunction', text="DiabetesPedigreeFunction", anchor=W)
    tree.heading('Age', text="Age", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=300)
    tree.column('#4', stretch=NO, minwidth=0, width=0)
    tree.column('#5', stretch=NO, minwidth=0, width=200)
    tree.column('#6', stretch=NO, minwidth=0, width=200)
    tree.column('#7', stretch=NO, minwidth=0, width=300)


    tree.pack()


    with open('testBefore.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            r1 = row['Preg']
            r2 = row['Glucose']
            r3 = row['BloodPressure']
            r4 = row['SkinThickness']
            r5 = row['Insulin']
            r6 = row['BMI']
            r7 = row['DiabetesPedigreeFunction']
            r8 = row['Age']
            

            tree.insert("", 0, values=(r1, r2, r3, r4, r5, r6, r7, r8))
###########################################################################

### After Table Function #####################
def afterTable():
    root = Tk()
    root.title("Python - Import CSV File To Tkinter Table")
    width = 500
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Preg", "Glucose", "BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age", "Outcome"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('Preg', text="Preg", anchor=W)
    tree.heading('Glucose', text="Glucose", anchor=W)
    tree.heading('BloodPressure', text="BloodPressure", anchor=W)
    tree.heading('SkinThickness', text="SkinThickness", anchor=W)
    tree.heading('Insulin', text="Insulin", anchor=W)
    tree.heading('BMI', text="BMI", anchor=W)
    tree.heading('DiabetesPedigreeFunction', text="DiabetesPedigreeFunction", anchor=W)
    tree.heading('Age', text="Age", anchor=W)
    tree.heading('Outcome', text="Outcome", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=300)
    tree.column('#4', stretch=NO, minwidth=0, width=0)
    tree.column('#5', stretch=NO, minwidth=0, width=200)
    tree.column('#6', stretch=NO, minwidth=0, width=200)
    tree.column('#7', stretch=NO, minwidth=0, width=300)
    tree.column('#8', stretch=NO, minwidth=0, width=300)


    tree.pack()


    with open('testAfter.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            r1 = row['Preg']
            r2 = row['Glucose']
            r3 = row['BloodPressure']
            r4 = row['SkinThickness']
            r5 = row['Insulin']
            r6 = row['BMI']
            r7 = row['DiabetesPedigreeFunction']
            r8 = row['Age']
            r9 = row['Outcome']
    
            

            tree.insert("", 0, values=(r1, r2, r3, r4, r5, r6, r7, r8, r9))

########################################

##################Traing table function#######################
def trainTable():
    root = Tk()
    root.title("Python - Import CSV File To Tkinter Table")
    width = 500
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Preg", "Glucose", "BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age", "Outcome"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('Preg', text="Preg", anchor=W)
    tree.heading('Glucose', text="Glucose", anchor=W)
    tree.heading('BloodPressure', text="BloodPressure", anchor=W)
    tree.heading('SkinThickness', text="SkinThickness", anchor=W)
    tree.heading('Insulin', text="Insulin", anchor=W)
    tree.heading('BMI', text="BMI", anchor=W)
    tree.heading('DiabetesPedigreeFunction', text="DiabetesPedigreeFunction", anchor=W)
    tree.heading('Age', text="Age", anchor=W)
    tree.heading('Outcome', text="Outcome", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=300)
    tree.column('#4', stretch=NO, minwidth=0, width=0)
    tree.column('#5', stretch=NO, minwidth=0, width=200)
    tree.column('#6', stretch=NO, minwidth=0, width=200)
    tree.column('#7', stretch=NO, minwidth=0, width=300)
    tree.column('#8', stretch=NO, minwidth=0, width=300)


    tree.pack()


    with open('train.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            r1 = row['Preg']
            r2 = row['Glucose']
            r3 = row['BloodPressure']
            r4 = row['SkinThickness']
            r5 = row['Insulin']
            r6 = row['BMI']
            r7 = row['DiabetesPedigreeFunction']
            r8 = row['Age']
            r9 = row['Outcome']
    
            

            tree.insert("", 0, values=(r1, r2, r3, r4, r5, r6, r7, r8, r9))




################################################