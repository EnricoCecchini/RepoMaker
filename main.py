# Import libraries
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import git

# Initialize Browser
def make_browser():
    # Set webdriver options
    options = Options()
    #options.add_experimental_option('--incognito', True)
    options.add_argument('--disable-extensions')
    options.add_argument('--profile-directory=Default')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--incognito")

    # Create webdriver
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = options)
    driver.get("https://www.github.com/login")

    return driver

# Login user
def login_user(browser, batchDir):
    user, password = getUserData(batchDir)
    # Login
    email_field = browser.find_element("id", 'login_field')
    email_field.send_keys(user)
    password_field = browser.find_element("id", 'password')
    password_field.send_keys(password)
    browser.find_element("name", 'commit').click()

# read user account data from config file
def getUserData(batchDir):
    if not os.path.exists(f'{batchDir}\config.ini'):
        user = input('Github Email: ')
        password = input('Password: ')
        with open(f'{batchDir}\config.ini', 'w') as f:
            f.write(f'{user}\n')
            f.write(f'{password}\n')
    else:
        with open(f'{batchDir}\config.ini', 'r') as f:
            user = f.readline().replace('\n', '')
            password = f.readline().replace('\n', '')

    return user, password

# Create Repo
def makeRepo(browser, projectTitle):
    browser.get("https://github.com/new")
    name_field = browser.find_element("id", "repository_name")
    name_field.send_keys(projectTitle)
    #browser.find_element('xpath', '//*[@id="new_repository"]/div[5]/button').click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Creat')]"))).click()

    projectURL = browser.find_element("id", "empty-setup-clone-url").get_attribute('value')
    print(projectURL)

    return projectURL

projectTitle = sys.argv[1]
batchDir = sys.argv[2]
projectDir = sys.argv[3]
print(projectDir)

browser = make_browser()
projectPath = login_user(browser, batchDir)
projectURL = makeRepo(browser, projectTitle)
browser.quit()

# Clone Repo
git.Git(projectDir).clone(projectURL)