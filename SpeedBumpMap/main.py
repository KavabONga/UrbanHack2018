from flask import Flask, render_template, jsonify

app = Flask(__name__, )

@app.route('/')
def mainMap():
    return render_template('mapPage.html')

@app.route('/SpeedBumps')
def speed_bumps():
    speedbumps = eval(open('res/speedbumps.json', 'r').read())
    speedbumps = [{'coordinates' : d['geoData']['coordinates'], 'street' : d['Location']} for id, d in speedbumps.items()]
    return jsonify(speedbumps)

@app.route('/CarCount')
def car_count():
    speedbumps = eval(open('res/speedbumps.json', 'r').read())
    carinfo = eval(open('res/carinfo-29-09.json', 'r').read())
    carinfo = [{'coordinates' : speedbumps[c['ID']]['geoData']['coordinates'], 'count' : len(c['events']), 'summaryWeight' : sum([k['weight'] for k in c['events']])} for c in carinfo]
    return jsonify(carinfo)
