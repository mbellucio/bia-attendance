import arrow
import pandas
import os


class PlaytimeCalculator:
    def __init__(self, structured_data: dict, filename: str, month: str, mission_duration: int, year: str):
        self.attended_list = []
        self.lost_attendance = []
        self.structured_data = structured_data
        self.file_name = filename
        self.month = month
        self.minimum_playtime = mission_duration
        self.year = year

    def final_attendance(self):
        for name, status in self.structured_data.items():
            first_connect = status[0][0]
            last_disconnect = status[-1][0]

            enter_time = arrow.get(first_connect, 'HH:mm:ss')
            exit_time = arrow.get(last_disconnect, 'HH:mm:ss')
            time_spent_on_server = exit_time - enter_time
            time_spent_on_server = str(time_spent_on_server)
            splitted_time = time_spent_on_server.split(":")

            try:
                playtime_in_minutes = (int(
                    splitted_time[0]) * 60) + (int(splitted_time[1])) + (int(splitted_time[2]) / 60)
            except ValueError:
                self.attended_list.append(name)

            type_test = self.file_name.split("_")
            if type_test[1] == 'TRN':
                self.minimum_playtime = 55

            if playtime_in_minutes > self.minimum_playtime:
                self.attended_list.append(name)
            else:
                self.lost_attendance.append(name)

        self.generate_file()

    def generate_file(self):
        attendance_directory = f"attendance/{self.year}/{self.month}"
        lost_attendance_directory = f"lost_attendance/{self.year}/{self.month}"

        if not os.path.exists(attendance_directory):
            os.makedirs(attendance_directory, exist_ok=True)

        if not os.path.exists(lost_attendance_directory):
            os.makedirs(lost_attendance_directory, exist_ok=True)

        final_data_attended = pandas.DataFrame(self.attended_list)
        final_data_attended.to_csv(f"{attendance_directory}/{self.file_name}.csv")

        final_data_lost_att = pandas.DataFrame(self.lost_attendance)
        final_data_lost_att.to_csv(f"{lost_attendance_directory}/{self.file_name}.csv")
