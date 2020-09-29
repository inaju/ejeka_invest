import requests
import webbrowser

url = "https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110"
myInput = {'email': 'mymail@gmail.com', 'pass': 'mypaass'}
x = requests.post(url, data=myInput)
y = x.text
f = open("home.html", "a")
f.write(y)
f.close()
webbrowser.open(url)
