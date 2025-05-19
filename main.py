from log_processor import LogProcessor
from data_structurer import DataStructurer
from playtime_calculator import PlaytimeCalculator
from mission_duration.duration import get_mission_duration
import os

# =========================
MONTH = 'may'
YEAR = '2025'
ROOT_DIR = 'logs'
# =========================

target_folder = os.path.join(ROOT_DIR, YEAR, MONTH)
items = os.listdir(target_folder)
filenames_without_extensions = [os.path.splitext(file)[0] for file in items]

for filename in filenames_without_extensions:
    try:
        mission_duration = get_mission_duration(
            month=MONTH, mission=filename, year=YEAR)
    except KeyError:
        mission_duration = None

    log_processor = LogProcessor(file_name=filename, month=MONTH, year=YEAR)
    log_data = log_processor.process_log()

    data_structurer = DataStructurer(
        processed_log=log_data, file_name=filename, month=MONTH, year=YEAR)
    structured_data = data_structurer.organize_by_player()

    playtime_calculator = PlaytimeCalculator(
        structured_data=structured_data,
        filename=filename, month=MONTH,
        mission_duration=mission_duration, year=YEAR
    )
    playtime_calculator.final_attendance()

