from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
