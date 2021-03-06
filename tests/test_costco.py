# Generated by Selenium IDE
import pytest
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC

#  /opt/bin/start-selenium-standalone.sh
class TestCostcolysol():
  def setup_method(self, method):
    self.product_url = os.environ['PRODUCT_URL']
    self.postal_code = os.environ['POSTAL_CODE']

    options = Options()
    options.headless = True
    self.driver = webdriver.Firefox(options=options)  

    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()

  def wait_for_price(self):
    counter =0 

    time.sleep(2)
    value = self.driver.find_element(By.CSS_SELECTOR, "#math-table .value")
    
    while "--" in value.text:
        self.driver.get( self.product_url)
        time.sleep(2)
        value = self.driver.find_element(By.CSS_SELECTOR, "#math-table .value")

        counter += 1
        if counter == 10:
            value.text=0
    
    return value.text
  
  def test_costco_lysol(self):
    self.driver.get("https://www.costco.ca/")
    self.driver.set_window_size(1440, 877)
    self.driver.find_element(By.CSS_SELECTOR, ".col-xs-12:nth-child(2) > .show:nth-child(2) > input").click()
    self.driver.find_element(By.ID, "language-region-set").click()
    self.driver.get(self.product_url)

    time.sleep(2)
    
    self.driver.find_element(By.ID, "postal-code-input").click()
    self.driver.find_element(By.ID, "postal-code-input").send_keys(self.postal_code)
    self.driver.find_element(By.ID, "postal-code-submit").click()

    self.wait_for_price()
  
    value = self.driver.find_element(By.ID, "add-to-cart-btn").get_attribute("value")
    #assert value == "Out of Stock"
    assert value == "Add to Cart"

    self.driver.close()
  

