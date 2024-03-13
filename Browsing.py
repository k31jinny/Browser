from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options =Options()   
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
url = 'https://google.com'
driver.get(url) 


'''
<textarea class="gLFyf" aria-controls="Alh6id" aria-owns="Alh6id" autofocus="" title="Search" value="" jsaction="paste:puy29d;" aria-label="Search" aria-autocomplete="both" aria-expanded="true" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" id="APjFqb" maxlength="2048" name="q" role="combobox" rows="1" spellcheck="false" data-ved="0ahUKEwj3-uuU9O-EAxUsGDQIHR9QBscQ39UDCAY" aria-activedescendant="" style=""></textarea>
'''


driver.find_element(By.CLASS_NAME,"gLFyf").send_keys("블랙핑크")
time.sleep(1)
driver.find_element(By.ID, "APjFqb").send_keys("뉴진스")
