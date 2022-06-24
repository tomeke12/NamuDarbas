import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")

    def test_search_in_pyhton_org(self):
        driver = self.driver
        driver.get("https://openlibrary.org/")
        self.assertIn("Library", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("Apple")
        elem.send_keys(Keys.RETURN)
        self.assertIn("Apple Delights Cookbook", driver.page_source)
        

    def tearDown(self):
        self.driver.close()

    def test_search_in_pyhton_org2(self):
        driver = self.driver
        driver.get("https://openlibrary.org/")
        self.assertIn("Library", driver.title)
        elem = driver.find_element(By.XPATH, "/html/body/header[1]/ul[2]/li[1]/a")
        elem.send_keys(Keys.RETURN)
        self.assertIn("Log In", driver.page_source)
        elem2 = driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/form/div[1]/div[2]/input")
        elem2.send_keys("test2@gmail.com")
        elem3 = driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/form/div[2]/div[2]/input")
        elem3.send_keys("lasara")
        elem3.send_keys(Keys.RETURN)
        self.assertIn("No account was found with this email. Please try again", driver.page_source)


if __name__ == "__main__":
    unittest.main()


