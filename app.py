

from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
   def list(): 
return render_template("index.html",show=monthlyexpenses)

if __name__ == "__main__":   
app.run()

