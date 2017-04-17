################################################################
# Logit directory creation script in python
# Python 2.7.12
# By Simon Bardsley
# 15 April, 2017
# Description: This script prompts the usesr for information on Change numnber, a short description, a customer
# name and a company name (if it is a data provision request)
# Add... check if Change number exists in other directories
# Add... limited text input() to a number of chars of one type
################################################################
import os, re, time, errno, sys
from os import listdir, path, chmod

#Logit list variable
logitClass = {0: 'DP' , 1: 'SA' , 2: 'DS' , 3: 'PS' , 4: 'IN' , 5: 'MR' , 6: 'LOGIMA'}

#Logit name variables
logitType = input("Choose a logit type number: 0:'DP', 1:'SA', 2:'DS', 3:'PS', 4:'IN', 5:'MR', 6:'LOGIMA' "[0:1]
#print(logitType)
changeNum = input("Provide the logit change number (e.g. C12345): ")[0:6]
shortDesc = input("Write a short description (<15 char): ")[0:15]
customerName = input("Add the customers name? ")[0:15]
os.chdir("C:\\Users\\simonbardsley\\Downloads")
print(os.getcwd())


# Check if the folder exists, if not create it either as a general logit or a data provision request and exit if statement
if logitType == 2:
    companyName = input("What is the company name? ")
    logitName = str(changeNum + " - " + shortDesc + " - " + customerName + " - " + companyName + " - " + logitClass[logitType])
    path = os.path.join("C:\\Users\\simonbardsley\\Downloads\\", logitName)
    if not os.path.exists(path):
        os.mkdir(path)
        print("A logit folder was created as: " + logitName)
        time.sleep(2)
        #os.chmod(path, mode=777)
        os.chdir(path)
        print("###################################")
        print("Creating subfolders")
        time.sleep(2)
        print("Documents...")
        time.sleep(2)
        os.mkdir("1 Documents")
        print("Inputs...")
        time.sleep(2)
        os.mkdir("2 Inputs")
        print("Data...")
        time.sleep(2)
        os.mkdir("3 Data")
        print("Workspaces...")
        time.sleep(2)
        os.mkdir("4 Workspaces")
        print("Outputs...")
        os.mkdir("5 Outputs." )
        time.sleep(2)
        print("###################################")
        print("Listing Logit directory contents")
    else:
        print("Directory already exists!")
        sys.exit
else:
    logitName = str(changeNum + " - " + shortDesc + " - " + customerName + " - " + logitClass[logitType])
    path = os.path.join("C:\\Users\\simonbardsley\\Downloads\\", logitName)
    if not os.path.exists(path):
        os.mkdir(path)
        time.sleep(2)
        #os.chmod(path, mode=777)
        os.chdir(path)
        print("###################################")
        print("Creating subfolders")
        time.sleep(2)
        print("Documents...")
        time.sleep(2)
        os.mkdir("1 Documents")
        print("Inputs...")
        time.sleep(2)
        os.mkdir("2 Inputs")
        print("Data...")
        time.sleep(2)
        os.mkdir("3 Data")
        print("Workspaces...")
        time.sleep(2)
        os.mkdir("4 Workspaces")
        print("Outputs...")
        os.mkdir("5 Outputs." )
        time.sleep(2)
        print("###################################")
        print("Listing Logit directory contents")
        print("A logit folder was created as: " + logitName)
    else:
        print("Directory already exists!")
        sys.exit


list = os.listdir(path)

for items in list:
    print(items)

toClose = input("Do you want to close this program? y\n ")

if toClose == "y":
    exit
else:
   time.sleep(10)
