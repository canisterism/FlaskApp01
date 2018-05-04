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

@app.route('/')
def index():
    try:
        count = request.cookies.get('count')
        if count != None:
            count = int(count) + 1
        else:
            count = 0
        resp = make_response(render_template('index.html',count=count))
        resp.set_cookie('count',str(count))
        return resp
    except Exception as e:
        return render_template('error.html'),500