
from selenium import webdriver

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
# driver.minimize_window()
driver.get('https://www.imdb.com/title/tt0119822/')
                                           