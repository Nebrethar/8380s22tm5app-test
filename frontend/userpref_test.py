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


class TestUserPreferences(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        print("step 0:driver is loaded")

    def test_userpref(self):
        username = "instructor"
        password = "gounomavs1a"

        # User preferences
        driver = self.driver
        driver.maximize_window()
        driver.get("https://stately-granita-d9d023.netlify.app/")
        time.sleep(4)
        elem = driver.find_element(By.XPATH, "/html/body/div[1]/html/div/body/header/div[1]/nav/div[2]/a").click()
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "/html/body/div[1]/html/div/body/header/div[2]/div/div/div/div/div[2]/div/div/input[1]")
        elem.send_keys(username)
        elem = driver.find_element(By.XPATH, "/html/body/div[1]/html/div/body/header/div[2]/div/div/div/div/div[2]/div/div/input[2]")
        elem.send_keys(password)
        time.sleep(3)
        elem = driver.find_element(By.XPATH,"/html/body/div[1]/html/div/body/header/div[2]/div/div/div/div/div[2]/button").click()
        time.sleep(5)
        print("step 1: user login successful")
        elem = driver.find_element(By.XPATH,"/html/body/div/html/div/body/header/div[1]/nav/div[1]/div/a[3]").click()
        print("step 2: clicked user preferences link")

        try:
            print("step 3: success")
            assert True
        except NoSuchElementException:
            self.fail("user preferences test failed")
            assert False
        time.sleep(3)
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

