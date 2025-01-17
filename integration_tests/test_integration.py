# Generated by Selenium IDE
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestIntegration(unittest.TestCase):
  def setUp(self):
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")
    self.driver = webdriver.Chrome(options)
    self.driver.get('http://localhost:5000')
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_usecase(self):
    self.driver.get("http://localhost:5000/")
    self.driver.set_window_size(1050, 708)
    self.driver.find_element(By.NAME, "item").click()
    self.driver.find_element(By.NAME, "item").send_keys("aze")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    self.driver.find_element(By.NAME, "new_item").click()
    self.driver.find_element(By.NAME, "new_item").send_keys("azeaze")
    self.driver.find_element(By.CSS_SELECTOR, "li button").click()
    self.driver.find_element(By.LINK_TEXT, "Delete").click()
  
if __name__ == '__main__':
    unittest.main()