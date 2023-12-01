import json

def get_mission_duration(month:str, mission:str):
    f = open(f'mission_duration/{month}.json')
    data = json.load(f)
    return data[mission][0]["Duration"]
