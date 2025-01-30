import pandas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import calendar
import os
import time
from main import YEAR, MONTH
from helper import WEBNAMEFIX

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def get_links(month: int):
    links = []

    url = 'https://biaarma.com/previous-events'
    driver.get(url)

    print("hello")
    table = driver.find_element(By.CLASS_NAME, value='table')
    rows = table.find_elements(By.TAG_NAME, 'tr')[1:]
    date_column_index = 4
    link_column_index = 1

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        cell_text = cells[date_column_index].text
        date_time = int(cell_text.split('\n')[0].split('/')[1])
        link = cells[link_column_index].find_element(
            By.TAG_NAME, 'a').get_attribute('href')

        if date_time == month:
            links.append(link)

    return links


def month_string_to_number(month_str: str):
    month_abbr = month_str[:3].capitalize()
    return list(calendar.month_abbr).index(month_abbr)


def fix_name(name):
    name_fix = name
    if "." in name_fix[-1]:
        name_fix = name_fix.replace(".", "")
    if name_fix in WEBNAMEFIX:
        return WEBNAMEFIX[name_fix]
    return name_fix


def get_slots(mission_link: str, year: str, month: str):
    op_name = mission_link.split('/')
    op_name = op_name[4]

    if "Side" in op_name:
        return

    driver.get(mission_link)

    slots = driver.find_elements(By.CLASS_NAME, value='pn-event-slot')
    date = driver.find_element(By.CLASS_NAME, value='event-label')
    game = driver.find_element(
        By.XPATH, value='//*[@id="aspnetForm"]/section/div[1]/div[2]/h5[6]').text.split(" ")[1]

    slot_name = []
    slot_attendant = []

    for item in slots:
        info = item.text.splitlines()
        try:
            slot_attendant.append(fix_name(info[1]))
            slot_name.append(info[0])
        except IndexError:
            pass

    data = slot_attendant

    date = date.text.split()[1]
    date = date.replace('/', '-')
    date = pandas.to_datetime(date)
    date = f'{date.month}-{date.day}'
    file_name = f'{op_name}-{date}.csv'

    dataframe = pandas.DataFrame(data=data)

    if game == "Arma" or game == "ts1.biaarma.com" or game == "ts.ofcra.org":
        directory = f'website_slots/{year}/{month}'
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
        dataframe.to_csv(f'{directory}/{file_name}')
        print(f"created file: {file_name}")
    elif game == "DCS":
        directory = f'DCS/{year}/{month}'
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
        dataframe.to_csv(f'{directory}/{file_name}')
        print(f"created file: {file_name}")


def website_slots(month: str, year: str):
    links = get_links(month=month_string_to_number(month_str=month))
    for link in links:
        time.sleep(1)
        get_slots(mission_link=link, month=month, year=year)
    driver.quit()


website_slots(month=MONTH, year=YEAR)
