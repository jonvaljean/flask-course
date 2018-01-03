from flask import Flask

app = Flask(__name__)
print("__name__ is ",__name__)

@app.route('/')  # application home page
def home():
    return "Hellooo, world !"

app.run(port=5000)
