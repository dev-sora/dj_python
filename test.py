#coding:utf-8

from bottle import route, run
from bottle import get, post, request, redirect, template
import sqlite3

#build database
conn = sqlite3.connect('url.db')
c = conn.cursor()

c.execute('''drop table url_list''')
c.execute('''CREATE TABLE url_list (id integer primary key autoincrement, url text)''')

conn.commit()
conn.close()

#Submit URL
@get("/post")
def index():
    return template("index")

#Check URL
@get("/show")
def show():
    url_list = get_url_list()
    video_id = get_video_id()
    return template("show",url_list=url_list,video_id=video_id)

# What is done here?
# 1.Get YouTube URL from a form data
# 2.Split it by = to get Video ID
# 3.Somehow hit Google API(Not mach so sure XD)
@post("/add")
def add():
    url = request.forms.getunicode("url_in")
    #Split Video ID
    url = url.split("=")[1]
    save_url(url)
    return redirect("/post")

def get_url_list():
    print("This is get_url_list")
    conn = sqlite3.connect("url.db")
    c = conn.cursor()
    select = "select id, url from url_list"
    c.execute(select)
    url_list = []
    for row in c.fetchall():
        url_list.append({
            "id": row[0],
            "url": row[1]
        })
    conn.close()
    return url_list

def save_url(url):
    conn = sqlite3.connect("url.db")
    c = conn.cursor()
    insert = "insert into url_list(url) values(?)"
    c.execute(insert, (url,))
    conn.commit()
    conn.close()
    
@get('/get_id')
def get_video_id():
    conn = sqlite3.connect("url.db")
    c = conn.cursor()
    c.execute('select min(id), url from url_list')
    video_id = c.fetchone()
    c.execute('delete from url_list where id=(select min(id) from url_list)')
    conn.commit()
    conn.close()
    print("This is get_id")
    video_id = video_id[1]
    return video_id
    

run(host='localhost', port=8080, debug=True)