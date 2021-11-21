import time
from selenium import webdriver
import unittest

from selenium.webdriver.common.by import By

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"



class TestRegistrationForm(unittest.TestCase):

    def test_registration1(self):
        browser = webdriver.Chrome()
        browser.get(link1)

        first_name = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'first')]")
        first_name.send_keys("K")

        last_name = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'last')]")
        last_name.send_keys("K")

        email = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'email')]")
        email.send_keys("kari_kap@ukr.net")

        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        time.sleep(1)
        message = browser.find_element(By.TAG_NAME, "h1")
        message_text = message.text

        self.assertEqual("Congratulations! You have successfully registered!", message_text, "You did something wrong")

    def test_registration2(self):
        browser = webdriver.Chrome()
        browser.get(link2)

        first_name = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'first')]")
        first_name.send_keys("K")

        email = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'email')]")
        email.send_keys("kari_kap@ukr.net")

        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        time.sleep(1)
        message = browser.find_element(By.CSS_SELECTOR, "h1")
        message_text = message.text

        self.assertEqual("Congratulations! You have successfully registered!", message_text, "You did something wrong")


if __name__ == "__main__":
    unittest.main()