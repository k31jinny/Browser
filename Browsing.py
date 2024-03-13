
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options =Options()   
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
url = 'https://google.com'
driver.get(url) 


'''
<textarea class="gLFyf" aria-controls="Alh6id" aria-owns="Alh6id" autofocus="" title="Search" value="" 
jsaction="paste:puy29d;" aria-label="Search" aria-autocomplete="both" aria-expanded="true" aria-haspopup="false" 
autocapitalize="off" autocomplete="off" autocorrect="off" id="APjFqb" maxlength="2048" name="q" role="combobox" rows="1" 
spellcheck="false" data-ved="0ahUKEwj3-uuU9O-EAxUsGDQIHR9QBscQ39UDCAY" aria-activedescendant="" style=""></textarea>
'''


#driver.find_element(By.CLASS_NAME,"gLFyf").send_keys("블랙핑크")
#time.sleep(1)
#driver.find_element(By.ID, "APjFqb").send_keys("뉴진스")
#time.sleep(1)
#driver.find_element(By.NAME, "q").send_keys("트와이스")

'''//*[@id="APjFqb"]'''
#driver.find_element(By.XPATH,'//*[@id="APjFqb"]').send_keys("security intern")
#time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"[title ='Search']").send_keys("security intern")
time.sleep(1)


#driver.find_element(By.LINK_TEXT, "Sign in").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "Sign").click()


driver.find_element(By.CSS_SELECTOR,"[title ='Search']").send_keys(Keys.ENTER)
time.sleep(1)

'''<span class="gsmt ernJ4c" aria-level="2" role="heading" 
aria-label="Google interactive job search.">Jobs</span>'''

driver.find_element(By.LINK_TEXT,"Jobs").click()
time.sleep(1)


'''
<textarea class="gLFyf" aria-controls="Alh6id" aria-owns="Alh6id" autofocus="" title="Search" value="" jsaction="paste:puy29d;" aria-label="Search" aria-autocomplete="both" aria-expanded="true" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" id="APjFqb" maxlength="2048" name="q" role="combobox" rows="1" spellcheck="false" data-ved="0ahUKEwj3-uuU9O-EAxUsGDQIHR9QBscQ39UDCAY" aria-activedescendant="" style=""></textarea>
'''

navs = driver.find_elements(By.CSS_SELECTOR, ".BjJfJf")
for nav in navs:
    print(nav.get_attribute("outerHTML"))
    print()
    




