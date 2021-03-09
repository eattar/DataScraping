from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
import csv
import sys

path = os.path.realpath('chromedriver')
links = open(os.path.realpath('links.txt'), 'r')
driver = webdriver.Chrome(path)

counter = 0

for link in links.readlines():

    driver.get(link)
    # Name
    name = driver.find_element_by_xpath('//*[@id="main_content"]/table[1]/tbody/tr[1]/td/b').text
    # Address
    address_line = driver.find_element_by_css_selector(
        '#main_content > table:nth-child(5) > tbody > tr:nth-child(1) > td').text
    ad_start = address_line.find('\n')
    address = address_line[ad_start + 1:]
    # City
    city_line = driver.find_element_by_css_selector(
        '#main_content > table:nth-child(5) > tbody > tr:nth-child(2) > td').text
    ci_end = city_line.find(',')
    city = city_line[:ci_end]
    # State
    state = city_line[ci_end + 2:ci_end + 4]
    # Zip Code
    zip_code = city_line[ci_end + 5:]
    # Phone
    phone = driver.find_element_by_css_selector(
        '#main_content > table:nth-child(5) > tbody > tr:nth-child(3) > td').text
    # Facility
    facility_type = driver.find_element_by_css_selector(
        '#main_content > table.cc_search > tbody > tr:nth-child(1) > td:nth-child(2) > span > span > font > u').text
    # License
    license_type = driver.find_element_by_css_selector(
        '#main_content > table.cc_search > tbody > tr:nth-child(2) > td:nth-child(2) > span > span > font > u').text
    # Capacity
    capacity = driver.find_element_by_css_selector(
        '#main_content > table.cc_search > tbody > tr:nth-child(6) > td:nth-child(2)').text
    # Ages
    ages = driver.find_element_by_css_selector(
        '#main_content > table.cc_search > tbody > tr:nth-child(7) > td:nth-child(2)').text
    # Current
    for i in [9, 8, 10]:
        try:
            current_line = driver.find_element_by_css_selector(f'#main_content > table.cc_search > tbody > tr:nth-child({i})').text
            current = current_line[25:]
            if current == "Yes" or current == "No":
                break
        except NoSuchElementException:
            continue
    #Write to CSV
    with open(os.path.realpath('data.csv'), 'a') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        filewriter.writerow([name, address, city, state, zip_code, phone, facility_type, license_type, capacity, ages, current])
    counter += 1
    print(counter)

driver.close()
print('done')
sys.exit(0)