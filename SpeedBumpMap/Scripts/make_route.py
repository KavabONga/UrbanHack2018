import json
import math


def make_route(bump_id):
    def check(event, this_bump_id):
        for i in range(len(check_events)):
            if event['axles'] == check_events[i][0]['axles'] and \
               event['weight'] == check_events[i][0]['weight'] and\
               math.fabs(event['time'] - check_events[i][0]['time']) <= 1800:
                event['id'] = id_dict[str(this_bump_id)]
                check_events[i].append(event)
    inp_dict = open("../res/IDs.json", "r").read()
    inp_json = open("../res/carinfo-29-09.json", "r").read()
    carinfo = eval(inp_json)
    id_dict = eval(inp_dict)
    check_bump_id = bump_id
    check_bump_num = id_dict[str(check_bump_id)]
    check_events = list()
    for i in carinfo[check_bump_num]['events']:
        i['id'] = check_bump_id
        check_events.append([i])

    for i in range(check_bump_num):
        for j in carinfo[i]['events']:
            check(j, carinfo[i]['ID'])

    for i in range(check_bump_num + 1, len(carinfo)):
        for j in carinfo[i]['events']:
            check(j, carinfo[i]['ID'])
    for car in check_events:
        car.sort(key=lambda this_car: this_car['time'])
    ans = list()
    for car in check_events:
        tmp_dict = dict()
        tmp_dict['axles'] = car[0]['axles']
        tmp_dict['weight'] = car[0]['weight']
        tmp_dict['touches'] = list()
        for i in car:
            one_more_tmp_dict = dict()
            one_more_tmp_dict['time'] = i['time']
            one_more_tmp_dict['id'] = i['id']
            tmp_dict['touches'].append(one_more_tmp_dict)
        ans.append(tmp_dict)
    return json.dumps(ans)

make_route(24)