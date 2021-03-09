from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os


path = os.path.realpath('chromedriver')
file = open(r'links.txt', 'a')

mainPage = 'https://www.dss.virginia.gov/facility/search/cc2.cgi'
driver = webdriver.Chrome(path)
driver.get(mainPage)
driver.find_element_by_css_selector("#searchdata > tbody > tr:nth-child(5) > td:nth-child(2) > input[type=checkbox]").click()
driver.find_element_by_id("submit").click()

while True:
    try:
        rows = driver.find_elements_by_css_selector("td a")
        for link in rows:
            file.write(link.get_attribute('href'))
        driver.find_element_by_xpath("//*[@id="pagenatedlic_next"]").click()
    except ElementNotVisibleException:
        break

