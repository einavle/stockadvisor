
from flask import *  
from advisor import Advisor
import os 


app = Flask(__name__)   
advisor=Advisor()
  
@app.route('/advise', methods = ['GET','POST'])  
def advise():
    return advisor.advise()

@app.route('/', methods = ['GET','POST'])  
def mainRoute():
    return "Hello from stock advisor"



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)
