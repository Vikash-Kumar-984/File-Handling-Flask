# pip install flask

from flask import Flask, render_template

app = Flask(__name__)

# define the endpoint

@app.route('/', methods=['GET'])
def home():
    return render_template('form.html')

@app.route('/upload',methods=['POST'])
def get_data():
    return "We have received the file. Thank You"

if __name__=='__main__':
    app.run(debug=True)