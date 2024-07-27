import pandas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = r"chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

mission_link = 'http://biaarma.com/event/OpBruteForce1'

op_name = mission_link.split('/')
op_name = op_name[4]
print(op_name)

# ==================================================================================================================== #
driver.get(mission_link)
# ==================================================================================================================== #
slots = driver.find_elements(By.CLASS_NAME, value='pn-event-slot')
date = driver.find_element(By.CLASS_NAME, value='event-label')

slot_name = []
slot_attendant = []

for item in slots:
    info = item.text.splitlines()
    try:
        slot_attendant.append(info[1])
        slot_name.append(info[0])
    except IndexError:
        pass

data = slot_attendant

date = date.text.split()[1]
date = date.replace('/', '-')
date = pandas.to_datetime(date)
date = f'{date.month}-{date.day}'
file_name = f'{op_name}-{date}.csv'
print(file_name)


dataframe = pandas.DataFrame(data=data)
dataframe.to_csv(f'website_slots/2024/july/{file_name}')

# ==================================================================================================================== #
driver.quit()
# ==================================================================================================================== #
