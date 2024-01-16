import json

class DataStructurer:

    def __init__(self, processed_log:list, file_name:str, month:str, year:str):
        self.data = processed_log
        self.data_by_player = {}
        self.file_name = file_name
        self.month = month
        self.year = year

    def organize_by_player(self):
        for item in self.data:
            name = item[0]
            if name in self.data_by_player:
                continue
            else:
                info_list = []
                for player_statuses in self.data:
                    if player_statuses[0] == name:
                        info_list.append(player_statuses[1:])
                self.data_by_player[name] = info_list
        self.generate_json()
        return self.data_by_player

    def generate_json(self):
        json_data = json.dumps(self.data_by_player)
        with open(f'consult_data/{self.year}/{self.month}/{self.file_name}.json', mode='w', encoding='utf-8') as outfile:
            outfile.write(json_data)

        
