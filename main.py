from log_processor import LogProcessor
from data_structurer import DataStructurer
from playtime_calculator import PlaytimeCalculator
from mission_duration.duration import get_mission_duration

# ===============================
FILENAME = 'BIA_WW2_2024_02_18'
MONTH = 'february'
YEAR = '2024'
# ===============================

try:
    mission_duration = get_mission_duration(
        month=MONTH, mission=FILENAME, year=YEAR)
except KeyError:
    mission_duration = None

log_processor = LogProcessor(file_name=FILENAME, month=MONTH, year=YEAR)
log_data = log_processor.process_log()

data_structurer = DataStructurer(
    processed_log=log_data, file_name=FILENAME, month=MONTH, year=YEAR)
structured_data = data_structurer.organize_by_player()

playtime_calculator = PlaytimeCalculator(
    structured_data=structured_data,
    filename=FILENAME, month=MONTH,
    mission_duration=mission_duration, year=YEAR
)
playtime_calculator.final_attendance()
