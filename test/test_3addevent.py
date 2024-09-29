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

class TestAddevent():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_addevent(self):
    self.driver.get("https://kikkare.eu.pythonanywhere.com/")
    self.driver.set_window_size(1600, 1200)
    self.driver.find_element(By.LINK_TEXT, "Persons").click()
    self.driver.find_element(By.LINK_TEXT, "Events").click()
    self.driver.find_element(By.LINK_TEXT, "Create a new event").click()
    self.driver.find_element(By.ID, "id_name").click()
    self.driver.find_element(By.ID, "id_name").send_keys("Rocn roll")
    self.driver.find_element(By.ID, "id_date").click()
    self.driver.find_element(By.CSS_SELECTOR, ".flatpickr-day:nth-child(30)").click()
    self.driver.find_element(By.ID, "id_date").send_keys("2024-09-30 12:00")
    self.driver.find_element(By.CSS_SELECTOR, ".flatpickr-hour").send_keys("16")
    self.driver.find_element(By.ID, "id_description").click()
    self.driver.find_element(By.ID, "id_description").send_keys("rokn roll concert")
    self.driver.find_element(By.ID, "id_webpage").send_keys("http://rr.com")
    self.driver.find_element(By.ID, "id_venue").click()
    dropdown = self.driver.find_element(By.ID, "id_venue")
    dropdown.find_element(By.XPATH, "//option[. = 'Espoo Areena']").click()
    dropdown = self.driver.find_element(By.ID, "id_persons")
    dropdown.find_element(By.XPATH, "//option[. = 'Johan Doe']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
  