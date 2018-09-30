from flask import Flask, render_template, jsonify, request

app = Flask(__name__, )

@app.route('/')
def mainMap():
    return render_template('mapPage.html')

@app.route('/SpeedBumps')
def speed_bumps():
    speedbumps = eval(open('res/speedbumps.json', 'r').read())
    speedbumps = {id : {
        'coordinates' : d['geoData']['coordinates'],
        'street' : d['Location'],
        'id' : d['ID']
    } for id, d in speedbumps.items()}
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
    weights = [t['weight'] for t in c]
    from Scripts.classified_cars import Weight_Sort
    ws = Weight_Sort(weights)

    return jsonify(
        {
            'sumCars' : len(weights),
            'classes' : {
                'light-weighted' : ws[0],
                'average-weighted' : ws[1],
                'heavy-weighted' : ws[2]
            }
        }
    )

@app.route('/TimeSorted')
def time_sorted():
    speedbumps = eval(open('res/speedbumps.json', 'r').read())
    carinfo = eval(open('res/carinfo-29-09.json', 'r').read())
    times = []
    for c in carinfo:
        for e in c['events']:
            times.append({
                'time' : e['time'],
                'weight' : e['weight'],
                'coordinates' : speedbumps[c['ID']]['geoData']['coordinates'],
                'ID' : c['ID']
            })
    return jsonify(sorted(times, key=lambda x : x['time']))

@app.route('/statistics')
def statistics():
    return render_template('statistics.html')

@app.route('/CarPaths')
def car_paths():
    from Scripts.make_route import make_route
    res = [d for d in make_route(request.args.get('id')) if len(d['touches']) > 1]
    return jsonify(res)

if __name__ == '__main__':
    from Scripts.make_route import make_route
    print(make_route(13))
