from flask import *


app = Flask(__name__)


@app.route('/')
def home():
	return render_template('main.html', page='home')


@app.route('/add', methods=['GET'])
def add():
    return render_template('add.html', page='add'   )


@app.route('/create', methods=['POST'])
def create():
    # TODO: create processing method and call it from here
    pass

