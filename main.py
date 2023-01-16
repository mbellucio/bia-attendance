from log_processor import LogProcessor
from data_structurer import DataStructurer
from playtime_calculator import PlaytimeCalculator


#===============================
FILENAME = 'BIA_VTN_2023_01_12'
#===============================


log_processor = LogProcessor(file_name=FILENAME)
log_data = log_processor.process_log()

data_structurer = DataStructurer(processed_log=log_data, file_name=FILENAME)
structured_data = data_structurer.organize_by_player()

playtime_calculator = PlaytimeCalculator(structured_data=structured_data, filename=FILENAME)
playtime_calculator.final_attendance()

