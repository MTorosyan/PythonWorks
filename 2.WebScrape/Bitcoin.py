#Create a script to capture the price of bitcoin
#import the needed packages
import requests
import json
import sys

#function used to handle user input when no arguments are passed in, this allows us to handle input errors better + neater
def userSelection(curData, allKeys):
    #prints all currencies and takes user input
    print("Available currencies: \n" + allKeys)
    selection = str.strip(input("Please type your desired currency: "))
    #check to see if key exists, prints valid results
    if (selection in curData):
        print (selection + " : " + str(curData[selection]['last']))
    else:
        print ("Invalid selection")

#function used when multiple command line arguments are passed in
def handleCmdInput(curData, allKeys, argumentInput):
    #gets the arguments within the list, within the tuple. Side effect of using the optional argument in getCryptoData()
    for argument in argumentInput[0]:
        #valid key check
        if (argument in curData):
            print(argument + " : " + str(curData[argument]['last']))
        else:
            print("You have passed an invalid argument on the commandline. The list of available currencies are: \n" + allKeys)
            exit()

#This function generates a list of all valid keys for currencies
def generateKeyList(curData):
    listKey = ""
    #Generates a list by concatinating every key
    for key in curData:
        listKey = listKey + " " + key
    return listKey

#Posts live data and handles logic (must be split into two functions) the * makes the cmdInput an optional argument
def getCryptoData(*cmdInput):
    #set API URL
    my_url = 'https://blockchain.info/ticker'
    #Posts data to response
    response = requests.post(my_url)
    #Checks HTTP response status
    if(response.ok):
        #Stores the Json response as a nested dictionary
        jData = json.loads(response.content)
        #[TO DO] split into new function from this comment down
        supportedCurrencies = generateKeyList(jData)
        #Initialises the currency availability to pass into other functions
        if (cmdInput):
            handleCmdInput(jData, supportedCurrencies, cmdInput)
        elif(not cmdInput):
            userSelection(jData, supportedCurrencies)
        else:
            print("If you're seeing this message, I am a terrible coder and have not thoroughly thought about this case")
    #handles non 200 HTTP responses
    else:
        response.raise_for_status()

#Checks if command line arguments have been passed in, if not it will go into a prompt mode
if (len(sys.argv) > 1):
    inputList = sys.argv
    inputList.pop(0)
    getCryptoData(inputList)
else:
    getCryptoData()
