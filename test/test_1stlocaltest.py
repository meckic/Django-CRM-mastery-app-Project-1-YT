# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test1stlocaltest():
  def setup_method(self, method):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-search-engine-choice-screen")
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_1stlocaltest(self):
    # Test name: 1st local test
    # Step # | name | target | value | comment
    # 1 | open | / |  | 
    self.driver.get("http://127.0.0.1:8000/")
    # 2 | setWindowSize | 1392x1026 |  | 
    self.driver.set_window_size(1392, 1026)
    # 3 | click | linkText=Persons |  | 
    self.driver.find_element(By.LINK_TEXT, "Persons").click()
    # 4 | click | linkText=Create a new person |  | 
    self.driver.find_element(By.LINK_TEXT, "Create a new person").click()
    # 5 | click | id=id_first_name |  | 
    self.driver.find_element(By.ID, "id_first_name").click()
    # 6 | type | id=id_first_name | fn | 
    self.driver.find_element(By.ID, "id_first_name").send_keys("fn")
    # 7 | type | id=id_last_name | ln | 
    self.driver.find_element(By.ID, "id_last_name").send_keys("ln")
    # 8 | type | id=id_email | em@em.com | 
    self.driver.find_element(By.ID, "id_email").send_keys("em@em.com")
    # 9 | type | id=id_phone | 112233 | 
    self.driver.find_element(By.ID, "id_phone").send_keys("112233")
    # 10 | type | id=id_address | addrr | 
    self.driver.find_element(By.ID, "id_address").send_keys("addrr")
    # 11 | type | id=id_city | citty | 
    self.driver.find_element(By.ID, "id_city").send_keys("citty")
    # 12 | type | id=id_province | provv | 
    self.driver.find_element(By.ID, "id_province").send_keys("provv")
    # 13 | type | id=id_country | countr | 
    self.driver.find_element(By.ID, "id_country").send_keys("countr")
    # 14 | click | css=.btn-primary |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    # 15 | click | css=tr:nth-child(4) .fa |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) .fa").click()
    # 16 | click | linkText=Update person |  | 
    self.driver.find_element(By.LINK_TEXT, "Update person").click()
    # 17 | click | id=id_city |  | 
    self.driver.find_element(By.ID, "id_city").click()
    # 18 | type | id=id_city | city | 
    self.driver.find_element(By.ID, "id_city").send_keys("city")
    # 19 | click | css=.btn-info |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-info").click()
    # 20 | click | linkText=Venues |  | 
    self.driver.find_element(By.LINK_TEXT, "Venues").click()
    # 21 | click | linkText=Create a new venue |  | 
    self.driver.find_element(By.LINK_TEXT, "Create a new venue").click()
    # 22 | click | id=id_name |  | 
    self.driver.find_element(By.ID, "id_name").click()
    # 23 | type | id=id_name | tvenue | 
    self.driver.find_element(By.ID, "id_name").send_keys("tvenue")
    # 24 | type | id=id_email | tem@em.ocm | 
    self.driver.find_element(By.ID, "id_email").send_keys("tem@em.ocm")
    # 25 | type | id=id_phone | 33333 | 
    self.driver.find_element(By.ID, "id_phone").send_keys("33333")
    # 26 | click | id=id_address |  | 
    self.driver.find_element(By.ID, "id_address").click()
    # 27 | type | id=id_address | addree | 
    self.driver.find_element(By.ID, "id_address").send_keys("addree")
    # 28 | click | id=id_city |  | 
    self.driver.find_element(By.ID, "id_city").click()
    # 29 | type | id=id_city | citty | 
    self.driver.find_element(By.ID, "id_city").send_keys("citty")
    # 30 | click | id=id_province |  | 
    self.driver.find_element(By.ID, "id_province").click()
    # 31 | type | id=id_province | prov | 
    self.driver.find_element(By.ID, "id_province").send_keys("prov")
    # 32 | click | id=id_country |  | 
    self.driver.find_element(By.ID, "id_country").click()
    # 33 | type | id=id_country | contr | 
    self.driver.find_element(By.ID, "id_country").send_keys("contr")
    # 36 | click | css=.btn-primary |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    # 37 | click | css=tr:nth-child(3) .fa |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) .fa").click()
    # 38 | click | linkText=Update venue |  | 
    self.driver.find_element(By.LINK_TEXT, "Update venue").click()
    # 39 | click | id=id_city |  | 
    self.driver.find_element(By.ID, "id_city").click()
    # 40 | click | id=id_city |  | 
    self.driver.find_element(By.ID, "id_city").click()
    # 41 | click | id=id_city |  | 
    self.driver.find_element(By.ID, "id_city").click()
    # 42 | type | id=id_city | city | 
    self.driver.find_element(By.ID, "id_city").send_keys("city")
    # 43 | click | css=.btn-info |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-info").click()
    # 44 | click | linkText=Events |  | 
    self.driver.find_element(By.LINK_TEXT, "Events").click()
    # 45 | click | linkText=Create a new event |  | 
    self.driver.find_element(By.LINK_TEXT, "Create a new event").click()
    # 46 | click | id=id_name |  | 
    self.driver.find_element(By.ID, "id_name").click()
    # 47 | type | id=id_name | tevent | 
    self.driver.find_element(By.ID, "id_name").send_keys("tevent")
    # 48 | type | id=id_date | 2024-10-10 | 
    self.driver.find_element(By.ID, "id_date").send_keys("2024-10-10")
    # 49 | type | id=id_description | desr | 
    self.driver.find_element(By.ID, "id_description").send_keys("desr")
    # 50 | type | id=id_webpage | https://aa.bb | 
    self.driver.find_element(By.ID, "id_webpage").send_keys("https://aa.bb")
    # 51 | click | id=id_venue |  | 
    self.driver.find_element(By.ID, "id_venue").click()
    # 52 | select | id=id_venue | label=tvenue | 
    dropdown = self.driver.find_element(By.ID, "id_venue")
    dropdown.find_element(By.XPATH, "//option[. = 'tvenue']").click()
    # 53 | addSelection | id=id_persons | label=fn ln | 
    dropdown = self.driver.find_element(By.ID, "id_persons")
    dropdown.find_element(By.XPATH, "//option[. = 'fn ln']").click()
    # 54 | click | css=.btn-primary |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    # 55 | click | css=tr:nth-child(2) .fa |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) .fa").click()
    # 56 | click | linkText=Update event |  | 
    self.driver.find_element(By.LINK_TEXT, "Update event").click()
    # 57 | click | id=id_description |  | 
    self.driver.find_element(By.ID, "id_description").click()
    # 58 | type | id=id_description | tdesvription | 
    self.driver.find_element(By.ID, "id_description").send_keys("tdesvription")
    # 59 | click | css=.btn-info |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-info").click()
    # 60 | click | linkText=Search |  | 
    self.driver.find_element(By.LINK_TEXT, "Search").click()
    # 61 | click | name=search |  | 
    self.driver.find_element(By.NAME, "search").click()
    # 62 | type | name=search | r | 
    self.driver.find_element(By.NAME, "search").send_keys("r")
  
