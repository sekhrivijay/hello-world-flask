from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
        httpsEnabled = os.environ.get("HTTPS", False)
        port = os.environ.get("PORT", 8080)
        return "Hello world!!!\n https : " + httpsEnabled + "\n port : " + port + "\n" 

if __name__ == "__main__":
        port = int(os.environ.get("PORT", 8080))
        httpsEnabled = os.environ.get("HTTPS", False)
        if httpsEnabled:
            app.run(debug=True,host='0.0.0.0',port=port, ssl_context='adhoc')
        app.run(debug=True,host='0.0.0.0',port=port)
	
