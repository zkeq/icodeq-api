from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
print(driver.title)
driver.quit()