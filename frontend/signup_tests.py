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


class TestSignUp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        print("step 0:driver is loaded")

    def test_signup(self):
        # New User Information
        letters = string.ascii_lowercase
        username_1 = (''.join(random.choice(letters) for _ in range(10)))
        username = "team" + username_1
        password = "musicapp"
        passwordconfirmation = "musicapp"
        Firstname = "team"
        Lastname = "user"
        Email = "teamuser@gmail.com"

        # Sign Up
        driver = self.driver
        driver.maximize_window()
        driver.get("https://stately-granita-d9d023.netlify.app/")
        time.sleep(4)
        elem = driver.find_element(By.XPATH, "/html/body/div[1]/html/div/body/header/div[1]/nav/div[2]/a").click()
        time.sleep(3)
        elem = driver.find_element(By.XPATH,"/html/body/div[1]/html/div/body/header/div[2]/div/div/div/div/div[2]/a").click()
        time.sleep(3)
        elem = driver.find_element(By.ID, "firstName")
        elem.send_keys(Firstname)
        elem = driver.find_element(By.ID, "lastName")
        elem.send_keys(Lastname)
        elem = driver.find_element(By.ID, "email")
        elem.send_keys(Email)
        elem = driver.find_element(By.ID, "username")
        elem.send_keys(username)
        elem = driver.find_element(By.ID, "password")
        elem.send_keys(password)
        elem = driver.find_element(By.ID, "passwordConfirm")
        elem.send_keys(passwordconfirmation)
        time.sleep(3)
        elem = driver.find_element(By.XPATH,"/html/body/div[1]/html/div/body/header/div[2]/div/div/div/div/div[2]/form/button").click()
        time.sleep(5)
        print("step 1: user signup successful")
        elem = driver.find_element(By.XPATH, "/html/body/div/html/div/body/header/div[1]/nav/div[2]/a").click()
        time.sleep(5)
        print("step 2:  trying to login")
        try:

            elem = driver.find_element(By.XPATH,"/html/body/div/html/div/body/header/div[1]/nav/div[2]/a").click()
            print("step 4: clicked login button")
            elem = driver.find_element(By.XPATH,"/html/body/div[1]/html/div/body/header/div[2]/div/div/div/div/div[2]/div/div/input[1]")
            elem.send_keys(username)
            print("step 5: entered username")
            elem = driver.find_element(By.XPATH,"/html/body/div[1]/html/div/body/header/div[2]/div/div/div/div/div[2]/div/div/input[2]")
            elem.send_keys(password)
            print("step 5: entered password")
            time.sleep(5)
            elem = driver.find_element(By.XPATH, "/html/body/div[1]/html/div/body/header/div[2]/div/div/div/div/div[2]/button").click()
            time.sleep(5)
            driver.get("https://stately-granita-d9d023.netlify.app/")
            print("step 6: logged in once again")
            assert True
        except NoSuchElementException:
            self.fail("signup test failed")
            assert False
        time.sleep(3)
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

