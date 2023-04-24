from log_processor import LogProcessor
from data_structurer import DataStructurer
from playtime_calculator import PlaytimeCalculator


#===============================
FILENAME = 'BIA_WW2_2023_04_23'
MONTH = 'april'
MISSION_DURATION = 120; 
#===============================


log_processor = LogProcessor(file_name=FILENAME, month=MONTH)
log_data = log_processor.process_log()

data_structurer = DataStructurer(processed_log=log_data, file_name=FILENAME, month=MONTH)
structured_data = data_structurer.organize_by_player()

playtime_calculator = PlaytimeCalculator(structured_data=structured_data, filename=FILENAME, month=MONTH, mission_duration=MISSION_DURATION)
playtime_calculator.final_attendance()

