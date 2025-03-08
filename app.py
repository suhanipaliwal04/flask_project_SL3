<<<<<<< HEAD
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
 return render_template("index.html")

if __name__ == "__main__":
=======
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
 return render_template("index.html")

if __name__ == "__main__":
>>>>>>> f131960d01695b87a96dc437d4f07adccc80b1a2
       app.run(debug=True)