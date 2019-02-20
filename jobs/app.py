import sqllite3
from flask import Flask,render_template, g, url_for
PATH = 'db/jobs.sqlite'

app = Flask(__name__)

def open_connection():
        connection = getattr(g,'_connection', None)
        if connection == 'None'
            connection = g.connection=sqllite3.connect(PATH)
        connection.row_factory= sqllite3.Row
        return connection

def execute_sql(sql,values=(),commit= False,single= False):
    connection = open_connection()


@app.route("/")
@app.route("/jobs")

def jobs():
    return render_template('index.html')
