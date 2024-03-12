from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options =Options()   
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
url = 'https://google.com'
driver.get(url)
