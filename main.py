# Import libraries
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


# Initialize Browser
def make_browser():
    # Set webdriver options
    options = Options()
    #options.add_experimental_option('--incognito', True)
    options.add_argument('--disable-extensions')
    options.add_argument('--profile-directory=Default')
    options.add_experimental_option("detach", True)

    # Create webdriver
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = options)
    driver.get("https://www.github.com/login")

    return driver

# Login user
def login_user(browser):
    user, password, projectPath = getUserData()
    # Login
    email_field = browser.find_element_by_id('login_field')
    email_field.send_keys(user)
    password_field = browser.find_element_by_id('password')
    password_field.send_keys(password)
    login_button = browser.find_element_by_name('commit')
    login_button.click()

    return projectPath

# read user account data from config file
def getUserData():
    if not os.path.exists('config.ini'):
        user = input('Github Email: ')
        password = input('Password: ')
        projectPath = input('Projects Path to create new Repos: ')
        with open('config.ini', 'w') as f:
            f.write(f'{user}\n')
            f.write(f'{password}\n')
            f.write(f'{projectPath}\n')
    else:
        with open('config.ini', 'r') as f:
            user = f.readline().replace('\n', '')
            password = f.readline().replace('\n', '')
            projectPath = f.readline().replace('\n', '')

    return user, password, projectPath

browser = make_browser()
