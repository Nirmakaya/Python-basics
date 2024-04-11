import requests

# API Consumption Demo : Example of client side API
# We used Stack overflow api to get all question tile and link which have zero answers

# Use of request library to get API request
response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow', verify=False)
# To print it's output jsons
print(response.json()['items'])


# Consuming an API
for data in response.json()['items']:
    if data['answer_count'] == 0:
        print(data['title'])
        print(data['link'])
    else:
        print("skipped")
    print()
    # Space


# Terminal Cmd
# To make requirement file of all dependency : pip freeze > requirement.txt
# To make new python file : touch application.py