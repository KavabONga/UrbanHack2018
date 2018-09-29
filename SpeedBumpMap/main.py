from flask import Flask, render_template, make_response, json, request, Response

app = Flask(__name__, )

@app.route('/')
def mainMap():
    return render_template('mapPage.html')
