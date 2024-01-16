import json

def get_mission_duration(month:str, mission:str, year:str):
    f = open(f'mission_duration/{year}/{month}.json')
    data = json.load(f)
    return data[mission][0]["Duration"]
