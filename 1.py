from browser import document, alert

def say_hello(event):
    alert("Hello from Brython!")

button = document["my-button"]
button.bind("click", say_hello)
