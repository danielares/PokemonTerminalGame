import requests

import json

def request(url):
    try:
        answer = requests.get(url)
        if answer.status_code == 200:
            return answer.text
        else:
            print("Request error")
    except Exception as error:
        print("Request error")
        print(error)

def parsing(answer_text):
    try:
        return json.loads(answer_text)
    except:
        print("Parsing error")