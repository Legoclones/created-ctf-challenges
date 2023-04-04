# imports
from flask import Flask, render_template, session, request, redirect
import secrets
import sqlite3
import re


# initialize database
conn = sqlite3.connect('local.db')
print("Opened database successfully")

conn.execute('CREATE TABLE if not exists posts (postID TEXT, session TEXT, content TEXT, comments TEXT)')
print("Posts table created successfully")

conn.close()


# initialize flask
app = Flask(__name__)
app.secret_key = open("secret_key.txt", "r").read()
app.config["SESSION_COOKIE_HTTPONLY"] = False


# home page
@app.route('/', methods=['GET'])
def home():

    # if you're a new tester, we'll make you a brand new id!
    if 'id' not in session:
        session['id'] = secrets.token_hex(32)

    # get all posts
    posts = []
    con = sqlite3.connect("local.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute(f"SELECT * FROM posts WHERE session = '{session['id']}'")
    rows = cur.fetchall()

    for row in rows:
        posts.append({
            'id': row['postID'],
            'content': row['content'],
            'comments': row['comments'].split("|")
        })

    # actual HTML for index.html
    index = """
<!DOCTYPE html>

<head>
    <title>Unhackable</title>
</head>

<body>
    <div id="links">
        <a href="/new">Write a new post</a> - <a href="#">Find friends</a>
    </div>

    <div id="title"><h1>Your posts</h1></div>"""

    for post in posts:
        index += """
        <div class="post">"""+post["content"]+"""</div>
        <div class="small">ID - <a href="/getpost?id="""+post["id"]+"""">"""+post["id"]+"""<a></div>
        <div id="comments">"""

        for comment in post["comments"]:
            index += """<div class="comment">"""+comment+"""</div>"""

        index += """
            <div class="comment" id="addComment">
                <form action="/addComment" method="post">
                    <h3>Comment:</h3>
                    <input name="comment" type="text" placeholder="Add a comment here...">
                    <input name="postID" type="hidden" value=\""""+post['id']+"""\">
                    <input type="submit">
                </form>
            </div>
        </div>
        <br><br>"""
    index += """
</body>

<style>
#title, #links {
    text-align:center;
    width:100%;
}
.post {
    width:700px;
    border:1px solid black;
    padding:10px;
    border-radius:5px;
}
.small {
    font-size:0.8em;
    font-style:italic;
    margin:10px 0;
}
#comments {
    margin-left:40px;
}
.comment {
    width:660px;
    border:1px solid black;
    padding:10px;
    border-radius:5px;
}
h3 {
    margin:0;
}
</style>"""
    return index


# form to add a new post
@app.route('/new', methods=['GET'])
def new():
    return render_template("new.html")


@app.route('/getpost', methods=['GET'])
def getpost():
    # get variables
    postid = request.args["id"]
    
    # make sure it's hex
    VALID_CHARS = "0123456789abcdef"
    for letter in postid:
        if letter not in VALID_CHARS:
            return redirect('error')

    # try to get post
    con = sqlite3.connect("local.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute(f"SELECT * FROM posts WHERE postID = '{postid}' LIMIT 1")
    rows = cur.fetchall()

    # make sure post exists
    if len(rows) == 0:
        return redirect('/error')

    for row in rows:
        content = row['content']
        comments = row['comments'].split("|")
    
    content = """
<!DOCTYPE html>

<head>
    <title>Unhackable</title>
</head>

<body>
    <div id="title"><h1>Your post</h1></div>
        <div class="post">"""+content+"""</div>
        <div class="small">ID - """+str(postid)+"""</div>
        <div id="comments">"""

    for comment in comments:
        content += """<div class="comment">"""+comment+"""</div>"""

    content += """
    </div>
    <br><br>
</body>

<style>
#title, #links {
    text-align:center;
    width:100%;
}
.post {
    width:700px;
    border:1px solid black;
    padding:10px;
    border-radius:5px;
}
.small {
    font-size:0.8em;
    font-style:italic;
    margin:10px 0;
}
#comments {
    margin-left:40px;
}
.comment {
    width:660px;
    border:1px solid black;
    padding:10px;
    border-radius:5px;
}
h3 {
    margin:0;
}
</style>"""

    return content


# actually adds a new post
@app.route('/add', methods=['POST'])
def add():
    # get variables
    content = request.form['content']

    # no SQL injection today!!
    if ("'" in content):
        return redirect('error')

    # add new post
    with sqlite3.connect("local.db") as con:
        cur = con.cursor()
        id = secrets.token_hex(24)
        cur.execute(f"INSERT INTO posts (postID, session, content, comments) VALUES ('{id}', '{session['id']}', '{content}', 'Test comment!')")
        con.commit()

    return redirect('/')


# adds a comment to a post
@app.route('/addComment', methods=['POST'])
def addComment():
    # get variables
    comment = request.form['comment']
    id = request.form['postID']

    # no SQL injection today!!
    if ("'" in comment) or ('|' in comment):
        return redirect('error')

    # add comment
    con = sqlite3.connect("local.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute(f"SELECT comments FROM posts WHERE postID = '{id}'")
    rows = cur.fetchall()

    # make sure post exists!
    if len(rows) == 0:
        return redirect('/error')

    finalComment = ""
    for row in rows:
        finalComment = row['comments']+"|"+comment

    cur.execute(f"UPDATE posts SET comments = '{finalComment}' WHERE postID = '{id}'")
    con.commit()

    return redirect('/')


# generic error form
@app.route('/error', methods=['GET'])
def error():
    return render_template("error.html")


# start application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=40005, threaded=True)
