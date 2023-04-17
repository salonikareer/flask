import requests, json

def get():
 response = requests.get(url="http://127.0.0.1:5000/get value")
 print (response. json())

def post():
  response = requests.post(url="http://127.0.0.1:5000/post-value", json={'Name' : "Himakshi"})
  print (response. json())



get()
post()
get()
