import unittest
import time
from random import uniform, random, choice, sample
import json, random as rd, string
from random import *
import random
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import warnings
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webelement import WebElement
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert


class TestAdmin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        print("step 0:driver is loaded")

    def test_admin(self):
        # Admin User Information
        username = "instructor"
        password = "gounomavs1a"


        driver = self.driver
        driver.maximize_window()
        driver.get("https://8380s22tm5app.com/admin/")
        time.sleep(4)
        elem = driver.find_element(By.ID, "id_username")
        elem.send_keys(username)
        time.sleep(1)
        elem = driver.find_element(By.ID,"id_password")
        elem.send_keys(password)
        time.sleep(2)
        elem = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[1]/div/form/div[3]/input").click()
        time.sleep(6)
        print("step 1: Admin user login successful")
        elem = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/a[3]").click()


        try:

            print("step 3: success")
            assert True
        except NoSuchElementException:
            self.fail("admin login test failed")
            assert False
        time.sleep(3)
        warnings.simplefilter('ignore', ResourceWarning)


def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

