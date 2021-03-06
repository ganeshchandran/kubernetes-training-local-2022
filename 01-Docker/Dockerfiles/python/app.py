from flask import Flask
import os 
import socket


app = Flask(__name__)

@app.route("/")
def hello():
    html="<h1>Hello From Flask App.!</h1>"
    return html

@app.route("/hello")
def hello_test():
    html="<h2> Hello from docker based python web server.!!!</h2>"
    return html


@app.route("/info")
def hello_info(): 
    html="<h2> Hey Python Web Server</h2>"\
         "<b> Hostname: </b> {hostname}<br/>" \
         "<b> IP Address: </b> {fqdn}<br/>"
    return html.format(hostname=socket.gethostname(),fqdn=socket.gethostbyname(socket.gethostname()))


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8081)
