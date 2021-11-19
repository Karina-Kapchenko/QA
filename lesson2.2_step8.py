from selenium import webdriver
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

name_field = browser.find_element_by_css_selector("[name='firstname']")
lastname_field = browser.find_element_by_css_selector("[name='lastname']")
email_field = browser.find_element_by_css_selector("[name='email']")
file_button = browser.find_element_by_css_selector("[type='file']")
send_button = browser.find_element_by_css_selector(".btn-primary")

name_field.send_keys("N")
lastname_field.send_keys("L")
email_field.send_keys("E")

current_dir = os.path.abspath(os.path.dirname(__file__))

file_path = os.path.join(current_dir, "test_file.txt")

file_button.send_keys(file_path)
send_button.click()