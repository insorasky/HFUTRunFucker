import os
from flask import Flask, render_template

app = Flask(__name__)
app.config["CONFDIR"] = './certs'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/cert/pem')
def pem():
    return read_cert("pem", "application/x-x509-ca-cert")


@app.route('/cert/p12')
def p12():
    return read_cert("p12", "application/x-pkcs12")


@app.route('/cert/cer')
def cer():
    return read_cert("cer", "application/x-x509-ca-cert")


def read_cert(ext, content_type):
    filename = f"mitmproxy-ca-cert.{ext}"
    p = os.path.join(app.config["CONFDIR"], filename)
    p = os.path.abspath(p)
    with open(p, "rb") as f:
        cert = f.read()

    return cert, {
        "Content-Type": content_type,
        "Content-Disposition": f"inline; filename=HFUTRunFucker-ca-cert.{ext}",
    }
