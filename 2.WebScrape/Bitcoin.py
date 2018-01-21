#Create a script to capture the price of bitcoin
import requests
import json

def liveBitData(keyCur):
    my_url = 'https://blockchain.info/ticker'
    response = requests.post(my_url)

    if(response.ok):
        jData = json.loads(response.content)

        return str(jData[keyCur]['last'])

    #   print("The response contains {0} properties".format(len(jData)))
    #   print("\n")

    #    for key in jData:
    #        print (key + " : " + str(jData[key]['last']))

    else:
        response.raise_for_status()

userCur = input("Please type the currency")

print (userCur + " : " + liveBitData(userCur))
