################################################################
# Logit directory creation script in python
# By Simon Bardsley
# 03 April, 2017
# Description: This script prompts the usesr for information on Change numnber, a short description, a customer
# name, a company name (if it is a data provision request)
# Add... check if Change number exists in other directories
# Add... create sub-folders by changing directory to the new director then use os.mkdir to create and name
# subdirectories
# Add... limited text input() to a number of chars of one type
################################################################
import os, re, time
from os import listdir

print("Python", python_version())

#Logit list
logitClass = {0:'DP', 1:'SA', 2:'DS', 3:'PS', 4:'IN', 5:'MR', 6:'LOGIMA'}
for item in logitClass:
    print(item)

#Variables
logitType = int(input("Choose a logit type number: 0:'DP', 1:'SA', 2:'DS', 3:'PS', 4:'IN', 5:'MR', 6:'LOGIMA' "))
changeNum = input("Provide the logit change number (e.g. C12345): ")
shortDesc = input("Write a short description (<15 char): ")[0:15]
customerName = input("Add the customers name? ")
os.chdir("/home/simon/PyCharm")
print(os.getcwd())

if logitType == 2:
    companyName = input("What is the company name? ")
    logitName = os.mkdir(changeNum + " - " + shortDesc + " - " + customerName + " - " +
                         companyName + " - " + logitClass[logitType], mode=777)
    # logitName = changeNum + " - " + shortDesc + " - " + customerName + " - " + companyName + " - " + logitClass[logitType]
    print("A logit folder was created as: " + str(logitName))
else:
    logitName = os.mkdir(changeNum + " - " + shortDesc + " - " + customerName + " - " +
                         logitClass[logitType], mode=777)
    # logitName = changeNum + " - " + shortDesc + " - " + customerName + " - " + logitClass[logitType]
    print("A logit folder was created as: " + str(logitName))


# print("Changing to D:")
# time.sleep(5)
# os.chdir("/home/simon/PyCharm")
# print(os.getcwd())
# print("Creating new logit folder")
# time.sleep(5)
# os.mkdir(logitName, 777)
time.sleep(5)
os.chmod("/home/simon/PyCharm/" + str(logitName), mode=777)
os.chdir("/home/simon/PyCharm/" + str(logitName)
print("###################################")
print("Creating subfolders")
time.sleep(2)
print("Documents...")
time.sleep(2)
os.mkdir("1 Documents", mode=777)
print("Inputs..."),
time.sleep(2),
os.mkdir("2 Inputs", mode=777)
print("Data...")
time.sleep(2)
os.mkdir("3 Data", mode=777)
print("Workspaces...")
time.sleep(2)
os.mkdir("4 Workspaces", mode=777)
print("Outputs...")
os.mkdir("5 Outputs...", mode=777)
time.sleep(2)
print("###################################")
print("Listing Logit directory contents")
time.sleep(5)

list = os.listdir(str(logitName))

for item in list:
    print(item)

toClose = input("Do you want to close this program? Y/N ")
if toClose == "Y":
    exit
else:
    time.sleep(10)