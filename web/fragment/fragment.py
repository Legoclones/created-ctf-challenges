from flask import Flask, request
from urllib.parse import urlparse

FLAG = "byuctf{fr4gm3nt4t10n}"
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    page = """
<html>
<head>
    <title>Fragment</title>
</head>
<body style="text-align:center;">
    <br><br>
    <h1>FRAGMENT</h1>
    <p>There is another web server running on localhost that ONLY <i>I</i> can access!! It contains the flag that you seek!</p>
    <p>To get it, you need me to access the webpage <pre>http://localhost:12345/flag</pre>. If you do, I will give you the flag and you get points.</p>
    <p>I have created a pre-configured URL that will take in <i>YOUR</i> input and send it out. HOWEVER, you have 3 characters that you can use.</p>
    <p>Any more than 3 will not be accepted!</p>
    <p>In addition, if I find the phrase "urmom" ANYWHERE in the URL, I will deny it.</p>
    <p>Good luck!</p>
    <br><br><br>
    <h2>Link</h2>
    <pre>http://localhost:12345/flag&lt;USERINPUT&gt;urmom</pre><br>
    <form action="/link" method="POST">
        <input type="text" name="userinput" placeholder="Userinput here" maxlength=3>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
    """
    return page


@app.route('/link',methods = ['POST'])
def link():
    # get user input
    try:
        userinput = request.form['userinput']
    except:
        return "No user input"
    if len(userinput) > 3:
        return "User input is too long"

    URL = "http://localhost:12345/flag"+userinput+"urmom"

    # parse URL
    parsed = urlparse(URL)

    # ensure scheme and network location are the same
    if (parsed.scheme != "http") and (parsed.netloc != "localhost:12345"):
        return "Invalid URL: "+URL
    # ensure "urmom" is not found
    elif ("urmom" in parsed.path) or ("urmom" in parsed.params) or ("urmom" in parsed.query):
        return "The string 'urmom' was detected in the URL "+URL
    # ensure the path is the same
    elif parsed.path != "/flag":
        return "The page "+str(parsed.path)+" does not exist"

    # if all checks are passed, then 'urmom' is in the fragment!
    return FLAG


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=40004)