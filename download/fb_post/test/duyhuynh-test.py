import unittest
from selenium import webdriver
class fblogin(unittest.TestCase):
      def setUp(self):
          self.driver=webdriver.Firefox()
          self.driver.get("http://www.facebook.com")
          self.driver.maximize_window()
 
 
      def test_facebookLogin(self):
          driver=self.driver
          driver.find_element_by_id('email').click()
          driver.find_element_by_id('email').clear()
          driver.find_element_by_id('email').send_keys('facebook id')
 
          driver.find_element_by_id('pass').click()
          driver.find_element_by_id('pass').clear()
          driver.find_element_by_id('pass').send_keys('password')
 
 
          driver.find_element_by_xpath("//input[@type='submit']").click()
          driver.implicitly_wait(30)
 
 
          #using the JavaScriptExecutor to scroll down to bottom of window
          driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
 
 
      def tearDown(self):
          self.driver.quit()
if __name__ == "__main__":
unittest.main()
