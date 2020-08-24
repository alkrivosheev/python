from flask import Flask, render_template    #импорт класса  Flask из библиотеки flask   #pip install flask
#pip install virtualenv
#python -m venv virtual
#./virtual/bin/pip install flask

app=Flask(__name__)

#@app - это декоратор
@app.route('/')
def home():
    return render_template("home.html")
    # return "Website content"

@app.route('/about/')
def about():
    return render_template("about.html")
    # return "About content"

if __name__=="__main__":
    app.run(debug=True)
