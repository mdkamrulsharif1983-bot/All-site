import os
from flask import Flask, render_template_string

app = Flask(__name__)

# উপরের HTML কোডটি এখানে ইনপুট দিন
HTML_CODE = """ আপনার উপরের পুরো HTML কোডটি এখানে কপি করে বসান """

@app.route('/')
def home():
    return render_template_string(HTML_CODE)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
  
