import os
import unittest
from appium import webdriver
from time import sleep
import time
from datetime import datetime

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ChessAndroidTests(unittest.TestCase):
    "Class to run tests against the Chess Free app"
    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH('C:\AutoTeste\selendroid-test-app-0.17.0.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
 
    def tearDown(self):
        "Tear down the test"
        self.driver.quit()
 
    def test_single_player_mode(self):
        teste = "teste"
        element = self.driver.find_element_by_id("inputUsername")
        element.send_keys("oloco bixo")
        time.sleep(3)
        # "Test the Single Player mode launches correctly"
        #element = self.driver.find_element_by_name("PLAY!")
        # element.click()
        # self.driver.find_element_by_name("Single Player").click()
        # textfields = self.driver.find_elements_by_class_name("android.widget.TextView")
        # self.assertEqual('MATCH SETTINGS', textfields[0].text)
 
#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ChessAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)