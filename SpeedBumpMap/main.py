from flask import Flask, render_template, jsonify

app = Flask(__name__, )

@app.route('/')
def mainMap():
    return render_template('mapPage.html')

@app.route('/SpeedBumps')
def speed_bumps():
    speedbumps = eval(open('res/speedbumps.json', 'r').read())
    speedbumps = [{
        'coordinates' : d['geoData']['coordinates'],
        'street' : d['Location']
    } for id, d in speedbumps.items()]
    return jsonify(speedbumps)

@app.route('/CarCount')
def car_count():
    speedbumps = eval(open('res/speedbumps.json', 'r').read())
    carinfo = eval(open('res/carinfo-29-09.json', 'r').read())
    carinfo = [{'coordinates' : speedbumps[c['ID']]['geoData']['coordinates'], 'count' : len(c['events']), 'summaryWeight' : round(sum([k['weight'] for k in c['events']]), 2)} for c in carinfo]
    return jsonify(carinfo)

@app.route('/StreetDensity')
def street_density():
    speedbumps = eval(open('res/speedbumps.json', 'r').read())
    carinfo = eval(open('res/carinfo-29-09.json', 'r').read())
    carinfo = [{'coordinates' : speedbumps[c['ID']]['geoData']['coordinates'], 'density' : round(sum([k['weight'] for k in c['events']]), 2)} for c in carinfo]
    return jsonify(carinfo)

@app.route('/SummaryData')
def summary_data():
    carinfo = eval(open('res/carinfo-29-09.json', 'r').read())
    axles = {i : 0 for i in range(2, 6)}
    sum_cars = 0
    for c in carinfo:
        for e in c['events']:
            axles[e[axles]] += 1
        sum_cars += len(events)
    return jsonify({'sumCars' : sum_cars, 'axles' : axles})

@app.route('/TimeSorted')
def time_sorted():
    carinfo = eval(open('res/carinfo-29-09.json', 'r').read())
    times = []
    for c in carinfo:
        for e in c['events']:
            times.append({'time' : e['time']})
