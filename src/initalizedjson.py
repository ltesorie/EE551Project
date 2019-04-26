import json

data_string = '''
{ 
    "users":[
    {
        "username": "ltesorie",
        "password": "1108",
        "balance": "0",
        "transactions": "0"
    },
    {
        "username": "jmac",
        "password": "1234",
        "balance": "10000",
        "transactions": "0"
    },
    {
        "username": "us01",
        "password": "1111",
        "balance": "100",
        "transactions": "0"
    }
]
}
'''

data = json.loads(data_string)
# print(data)
# print(type(data))
# print(data["users"])
# for user in data["users"]:
#    print(user["username"])

with open('json.txt', 'w') as outfile:
    json.dump(data, outfile)
