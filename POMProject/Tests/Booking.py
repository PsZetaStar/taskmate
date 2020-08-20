from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:/Users/Pallavi/Downloads/drivers/chromedriver.exe')
driver.get("https://www.goibibo.com/flights/air-DEL-BOM-20200827-20200830-1-0-0-E-D/")

driver.maximize_window()

#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.execute_script("window.scrollBy(0,250)","")
time.sleep(2)

# to increase the price of ticket for destination
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[4]/div[1]/div/ul/li[4]/span/i").click()
time.sleep(2)
# to increase the price of ticket for returning
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[4]/div[2]/div/ul/li[4]/span/i").click()
time.sleep(2)

#to click radio button of higher price for destination
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[5]/div[1]/div/div[1]/div/div[2]/div[2]/div/span[2]/label").click()
time.sleep(2)
#o click radio button of higher price for returning
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[5]/div[2]/div/div[1]/div/div[1]/div[2]/div/span[2]/label").click()
time.sleep(2)
# to book ticket
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/span[2]/span/input").click()

