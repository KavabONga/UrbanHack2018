from flask import Flask, render_template, jsonify

app = Flask(__name__, )

@app.route('/')
def mainMap():
    return render_template('mapPage.html')

@app.route('/SpeedBumps')
def speed_bumps():
    return jsonify(eval(open('res/speedbumps.json', 'r').read()))
