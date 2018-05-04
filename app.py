import psycopg2,psycopg2.extras
import psycopg2,psycopg2.extras
import psycopg2,psycopg2.extras
import psycopg2,psycopg2.extras
import psycopg2,psycopg2.extras
from flask import Flask,render_template,request,make_response,session
#import psycopg2,psycopg2.extras
#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
#from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'wj9jr2jg@249j0J4h20JaV91A03f4j2'

@app.route('/')
def index():
    if 'logged_in' in session and session['logged_in'] == True:
        return 'You are logged in.'
    else:
        session['logged_in'] = True
        return 'You are  not logged in.'