# pip install flask

from flask import Flask, render_template,request

app = Flask(__name__)

# define the endpoint

@app.route('/', methods=['GET'])
def home():
    return render_template('form.html')

@app.route('/upload',methods=['POST'])
def get_data():
    file=request.files['file']
    print("File Function contains: ",request.files)
    print("Files are: ",file)

    if file.filename.endswith(".csv"):
        path =  "userfile/" + file.filename
        file.save(path)
        return "We have received your file! Thank You"
    else:
        return "Upload a csv file only/-"
    # return "We have received the file. Thank You"

if __name__=='__main__':
    app.run(debug=True)