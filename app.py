from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"
    
@app.route("/time")
def salvador():
    return current_time
    


now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

if __name__ == "__main__":
    app.run(debug=True)
