
from tkinter.font import Font
import pandas 
from sklearn import metrics

from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import tree
from sklearn.preprocessing import MinMaxScaler

import matplotlib.pyplot as plt 

def decTreeAlgo(filename) :
    #use pandas to print CSV file on terminal 
    diabetesInput = pandas.read_csv(filename, delimiter=",")
    #print(diabetesInput)
    diabetesFactors = diabetesInput[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI','DiabetesPedigreeFunction','Age']].values 
    diabetesOutcome = diabetesInput['Outcome']
    #print(diabetesOutcome[0:6])
    #print(diabetesFactors[0:6])

    ## running the test and training data
    diabetesInput_train, diabetesInput_test, diabetesOutcome_train, diabetesOutcome_test = train_test_split(diabetesFactors, diabetesOutcome, test_size=0.3, random_state=4)

    print(diabetesOutcome_train.shape)
    print(diabetesOutcome_test.shape)

    diabetesTree = DecisionTreeClassifier(criterion="entropy", max_depth=4) # entropy makes the decision on a yes or no

    diabetesTree.fit(diabetesInput_train, diabetesOutcome_train)
    prediction = diabetesTree.predict(diabetesInput_test)
    plt.figure(figsize=(15,8))  # set plot size (denoted in inches)
    plt.title("Tree")
    plot_tree(diabetesTree, fontsize=10)
    plt.show()

    ################
    testPregancies = []
    testGlucose = []
    testBloodPressure= []
    testSkinThickness = []
    testInsulin = []
    testBMI = []
    testDPF = []
    testAge = []

    trainPregancies = []
    trainGlucose = []
    trainBloodPressure= []
    trainSkinThickness = []
    trainInsulin = []
    trainBMI = []
    trainDPF = []
    trainAge = []

    global negativePredictTest
    global positivePredictTest
    global negativeTestOutcome
    global positiveTestOutcome

    negativePredictTest = []
    positivePredictTest = []
    
    negativeTestOutcome = []
    positiveTestOutcome = []

    trainOutcome = []
    testOutcome = []
    predictionOutcome = []

    for i in diabetesOutcome_test:
        testOutcome.append(i)
    for i in diabetesOutcome_train:
        trainOutcome.append(i)
    for i in prediction:
        predictionOutcome.append(i)

    for i in predictionOutcome:
        if(i == 1):
            positivePredictTest.append(i)
        else:
            negativePredictTest.append(i)

    for i in testOutcome:
        if(i == 1):
            positiveTestOutcome.append(i)
        else:
            negativeTestOutcome.append(i)


    ## Inputing test data#################
    for i in range(diabetesInput_test.shape[1]):
    # print('Id: %d,' % i, diabetesInput_test[:, i])
        if(i == 0):
            testPregancies.append(diabetesInput_test[:, i])

        if(i == 1):
            testGlucose.append(diabetesInput_test[:, i])
        if(i == 2):
            testBloodPressure.append(diabetesInput_test[:, i])
        if(i == 3):
            testSkinThickness.append(diabetesInput_test[:, i])
        if(i == 4):
            testInsulin.append(diabetesInput_test[:, i]) 
        if(i == 5):
            testBMI.append(diabetesInput_test[:, i])
        if(i == 6):
            testDPF.append(diabetesInput_test[:, i])
        if(i == 7):
            testAge.append(diabetesInput_test[:, i]) 

    for i in range(diabetesInput_train.shape[1]):
            # print('Id: %d,' % i, diabetesInput_test[:, i])
        if(i == 0):
             trainPregancies.append(diabetesInput_train[:, i])

        if(i == 1):
            trainGlucose.append(diabetesInput_train[:, i])
        if(i == 2):
            trainBloodPressure.append(diabetesInput_train[:, i])
        if(i == 3):
            trainSkinThickness.append(diabetesInput_train[:, i])
        if(i == 4):
            trainInsulin.append(diabetesInput_train[:, i]) 
        if(i == 5):
            trainBMI.append(diabetesInput_train[:, i])
        if(i == 6):
            trainDPF.append(diabetesInput_train[:, i])
        if(i == 7):
            trainAge.append(diabetesInput_train[:, i]) 

    ###################writing into train.csv################################
    ##writing into train.csv#########################
    with open ("train.csv", 'wb') as file:
        inputTrainPreg = []
        inputTrainGlucose = []
        inputTrainBloodPressure = []
        inputTrainSkinThickness = []
        inputTrainInsulin = []
        inputTrainBMI = []
        inputTrainDPF = []
        inputTrainAge = []

        for x in trainPregancies:
            for i in x:
                inputTrainPreg.append(i)

        for x in trainGlucose:
            for i in x:
                inputTrainGlucose.append(i)

        for x in trainBloodPressure:
            for i in x:
                inputTrainBloodPressure.append(i)

        for x in trainSkinThickness:
            for i in x:
                inputTrainSkinThickness.append(i)

        for x in trainInsulin:
            for i in x:
                inputTrainInsulin.append(i)

        for x in trainBMI:
            for i in x:
                inputTrainBMI.append(i)

        for x in trainDPF:
            for i in x:
                inputTrainDPF.append(i)

        for x in trainAge:
            for i in x:
                inputTrainAge.append(i)
            

        trainData = {"Preg": inputTrainPreg,
                    "Glucose": inputTrainGlucose,
                    "BloodPressure": inputTrainBloodPressure,
                    "SkinThickness": inputTrainSkinThickness,
                    "Insulin": inputTrainInsulin,
                    "BMI": inputTrainBMI,
                    "DiabetesPedigreeFunction":inputTrainDPF,
                    "Age": inputTrainAge,
                    "Outcome": trainOutcome}
        df = pandas.DataFrame(trainData)

        df.to_csv('train.csv', index=False)
        file.close()


    ##############################################
        #print("L type is "+ str(type(l)))
        ##writes test in to test.csv
        ## Before test table population ################
        
    with open ("testBefore.csv", 'wb') as file:
        inputPreg = []
        inputGlucose = []
        inputBloodPressure = []
        inputSkinThickness = []
        inputInsulin = []
        inputBMI = []
        inputDPF = []
        inputAge = []

        for x in testPregancies:
            for i in x:
                inputPreg.append(i)

        for x in testGlucose:
            for i in x:
                inputGlucose.append(i)

        for x in testBloodPressure:
            for i in x:
                inputBloodPressure.append(i)

        for x in testSkinThickness:
            for i in x:
                inputSkinThickness.append(i)

        for x in testInsulin:
            for i in x:
                inputInsulin.append(i)

        for x in testBMI:
            for i in x:
                inputBMI.append(i)

        for x in testDPF:
            for i in x:
                inputDPF.append(i)

        for x in testAge:
            for i in x:
                inputAge.append(i)
        
        #writer_ = writer(file)
        #for z in range(5):
        #   print(l[z])
        #  writer_.writerow(l[z])
        dictBefore = {"Preg": inputPreg,
                "Glucose": inputGlucose,
                "BloodPressure": inputBloodPressure,
                "SkinThickness": inputSkinThickness,
                "Insulin": inputInsulin,
                "BMI": inputBMI,
                "DiabetesPedigreeFunction":inputDPF,
                "Age": inputAge}
        
        df = pandas.DataFrame(dictBefore)
        df.to_csv('testBefore.csv', index=False)
        file.close()

    ##################


    ## After test Population #########

    with open ("testAfter.csv", 'wb') as file:
        dictAfter = {"Preg": inputPreg,
                    "Glucose": inputGlucose,
                    "BloodPressure": inputBloodPressure,
                    "SkinThickness": inputSkinThickness,
                    "Insulin": inputInsulin,
                    "BMI": inputBMI,
                    "DiabetesPedigreeFunction":inputDPF,
                    "Age": inputAge,
                    "Predicted Outcome" : predictionOutcome,
                    "Outcome": testOutcome}
        df = pandas.DataFrame(dictAfter)
        df.to_csv('testAfter.csv', index=False)

        file.close()

    ##################################
    print("The input Type is" + str(type(diabetesInput_test)))




    #print(diabetesInput_train.shape)
    #print(diabetesInput_test.shape)
   # print(diabetesOutcome_train.shape)
    #print(diabetesOutcome_test.shape)

    #diabetesTree = DecisionTreeClassifier(criterion="entropy", max_depth=4) # entropy makes the decision on a yes or no

    #diabetesTree.fit(diabetesInput_train, diabetesOutcome_train)
    #prediction = diabetesTree.predict(diabetesInput_test)


    #addPrediction = list(prediction)
    #print(addPrediction)
    print(prediction)
    print("\nDecision Trees's Accuracy: ", metrics.accuracy_score(diabetesOutcome_test, prediction))
    return metrics.accuracy_score(diabetesOutcome_test, prediction)

