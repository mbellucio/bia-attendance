class LogProcessor:

    def __init__(self, file_name:str, month:str, year:str):
        """Insert only the file name, without the extension, example: '.txt' """
        
        self.rows = []
        self.splitted_rows = []
        self.filteres_rows = []
        self.final_log = []
        self.unwanted_characters = ["/n", "."]
        self.filter_params = ['connected', 'disconnected']
        self.file_path = f'logs/{year}/{month}/{file_name}.txt'
        self.time_index = 0
        self.name_index = 2
        self.status_index = -1


    def open_file(self):
        with open(
            file= self.file_path,
            mode="r",
            encoding="utf-8"
        ) as log:
            for row in log:
                self.rows.append(row)


    def row_to_list(self):
        for row in self.rows:
            new_row = row.split(" ")
            self.splitted_rows.append(new_row)


    def remove_empty_spaces(self):
        for row in self.splitted_rows:
            while "" in row:
                row.remove("")


    def remove_bad_characters(self):
        for i,row in enumerate(self.splitted_rows):
            self.splitted_rows[i] = [x.replace(".", "").replace("\n","") for x in row]
                

    def remove_bad_lines(self):
        param1 = self.filter_params[0]
        param2 = self.filter_params[1]
        for row in self.splitted_rows:
            if param1 in row or param2 in row:
                self.filteres_rows.append(row)

    def create_final_data(self):
        for item in self.filteres_rows:
            if self.filter_params[0] in item:
                self.status_index = -2
            else:
                self.status_index = -1
            filtered_item = [item[self.name_index], item[self.time_index], item[self.status_index]]
            self.final_log.append(filtered_item)

    def process_log(self):
        self.open_file()
        self.row_to_list()
        self.remove_empty_spaces()
        self.remove_bad_characters()
        self.remove_bad_lines()
        self.create_final_data()
        return self.final_log


