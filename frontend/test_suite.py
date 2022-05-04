import unittest
from signup_tests import TestSignUp
from fb_test import TestFb
from history_test import TestHistory
from random_test import TestRandom
from twitter_test import TestTwitter
from weatherrecommendation_test import TestWeather
from admin_login import TestAdmin
from userpref_test import TestUserPreferences


adminLogin = unittest.TestLoader().loadTestsFromTestCase(TestAdmin)
testSignup = unittest.TestLoader().loadTestsFromTestCase(TestSignUp)
testFb = unittest.TestLoader().loadTestsFromTestCase(TestFb)
testTwitter = unittest.TestLoader().loadTestsFromTestCase(TestTwitter)
testWeather = unittest.TestLoader().loadTestsFromTestCase(TestWeather)
testHistory = unittest.TestLoader().loadTestsFromTestCase(TestHistory)
testRandom = unittest.TestLoader().loadTestsFromTestCase(TestRandom)
testTestUserPreferences = unittest.TestLoader().loadTestsFromTestCase(TestUserPreferences)


test_suite = unittest.TestSuite([adminLogin, testSignup, testFb, testTwitter, testWeather, testHistory, testRandom])

unittest.TextTestRunner().run(test_suite)

def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    runner = unittest.TextTestRunner()