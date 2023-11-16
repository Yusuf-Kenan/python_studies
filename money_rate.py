import requests as re
import json

api_key = "2be7bad820e7121a78f89679"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/"



while True:
    print("**********************************".center(100))
    print("MONEY RATE APP".center(100))
    base = input("Please type your currency: ")
    target = input("Please type your target currency: ")
    amount = input("Please type amount you want to change: ")
    
    response=re.get(api_url + base + "/" + target + "/" + amount)
    response=json.loads(response.text)
    print(response)
    print(f"{amount} {response['base_code']} is {response['conversion_result']} {response['target_code']}")
    print("---------------".center(100))
    retry = input("Would you like to try again: y/n ")
    if retry != "y":
        break
