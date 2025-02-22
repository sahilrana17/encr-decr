from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')

def htop():
    name="Sahil Rana"
    username=os.getenv("USER","codespace")
    server_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    top_output=subprocess.getoutput("top -b -n 1")

    return f"""

    <pre>
    Name : {name}
    User : {username}
    Server Time : {server_time}

    Top Output:
    {top_output}
    </pre>

    """

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)