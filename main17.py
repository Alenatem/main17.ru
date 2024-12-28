from selenium import webdriver
#from selenium.webdriver import Keys
#from time import sleep
#import datetime
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains


file = open("log.txt", "w")
#driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option(name='detach', value=True)
#options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get('http://demoqa.com/checkbox')
driver.maximize_window()

main_list = driver.find_element(By.XPATH, '//*[@id="tree-node"]/div/button[1]')
main_list.click()

sublist = driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[3]/span/label')
sublist.click()

correct_text = "veu"
current_text = driver.find_element(By.XPATH, '//*[@id="result"]/span[2]')
assert correct_text == current_text.text, 'text not matches'
file.write('text matches')
