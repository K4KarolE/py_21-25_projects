'''
22 - Movie Details Scraping - Excel + Selenium
- user already has the the movie database link in clipboard
- user starts the program
- asking which row in the excel sheet will be used
- collecting the movie details(title, director, stars..) from the site and adding to the excel sheet
'''

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver

import sys

from openpyxl import load_workbook
wb = load_workbook('MoviePY.xlsx', data_only=True)
ws = wb.active


print()
k = 40
print('*'*k)
print(' I am Db Bee! '.center(k,'*'))
print('*'*k)
print()
link = 'https://www.imdb.com/title/tt1617661/?ref_=nv_sr_srsg_0' # more directors
# link = 'https://www.imdb.com/title/tt3076658/?ref_=nv_sr_srsg_0' # 1 director
# link = 'https://www.imdb.com/title/tt9271672/?ref_=ls_mv_desc' # 1 star
# link = 'https://www.imdb.com/title/tt10810424/?ref_=nm_flmg_wr_6' # dave 1 star



#link = input(' Please add the new record`s IMDb link: ')
cellnumber = '6957' #input(' Please add the row number of the new record: ')



PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get(link)

  
# very likely there is at least one director and star
director_2_Read = None
director_3_Read = None
star_2_Read = None
star_3_Read = None

# TAKING THE VALUES FROM THE 
# MOVIE TITLE
try:
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
                By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/h1'))
        )                       
          
        titleRead = driver.find_element(
        By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/h1').text
        
        print('***************************')
        print(titleRead)        
except:
        print()
        print('*** ERROR - MOVIE TITLE ***')
        print()
        driver.quit()
        sys.exit()


# YEAR OF RELEASE
try:
        yearRead = driver.find_element(
        By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[1]/a').text # if only one item(year) there is no index in the last li[1] just li
                
        print('***************************')
        print(yearRead)     
except:
        print()
        print('*** ERROR - YEAR OF RELEASE ***')
        print()
        driver.quit()

# DIRECTOR(S)
try:    
        director_1_Read = driver.find_element(
        By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[1]/div/ul/li[1]/a').text

        print('***************************')
        print(director_1_Read)

        director_2_Read = driver.find_element(
        By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[1]/div/ul/li[2]/a').text

        print('***************************')
        print(director_2_Read)

        director_3_Read = driver.find_element(
        By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[1]/div/ul/li[3]/a').text   
except:
        print()
        print('*** ERROR - MULTIPLE DIRECTORS ***')
        print()
        

# STAR(S)
try:    
        star_1_Read = driver.find_element(
        By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[3]/div/ul/li[1]/a').text

        print('***************************')
        print(star_1_Read)

        star_2_Read = driver.find_element(
        By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[3]/div/ul/li[2]/a').text

        print('***************************')
        print(star_2_Read)

        star_3_Read = driver.find_element(
        By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[3]/div/ul/li[3]/a').text

        print('***************************')
        print(star_3_Read)

except:
        print()
        print('*** ERROR - STARS ***')
        print()
        

# GENRE(S)
try:    
        genre_1_Read = driver.find_element(
        By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/a[1]/span').text

        print('***************************')
        print(genre_1_Read)

        genre_2_Read = driver.find_element(
        By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/a[2]/span').text

        print('***************************')
        print(genre_2_Read)

        genre_3_Read = driver.find_element(
        By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/a[3]/span').text

        print('***************************')
        print(genre_3_Read)

except:
        print()
        print('*** ERROR - GENRE ***')
        print()



# TAKING THE LENGTH VALUE
try:
       
        # taking the 2nd item(length) from "2022 1h 33m"
        movieLengthSum = driver.find_element(
        By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[2]').text

        # if the movie has classification(pg-13): "2022 pg-13 1h 33m" taking the 3rd item
        if 'h' not in list(movieLengthSum) or 'm' not in list(movieLengthSum):
                movieLengthSum = driver.find_element(
                By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[3]').text
except:
        print()
        print('*** ERROR - LENGTH ***')
        print()
       



# VALUATE AND TRANSFORM THE LENGTH VALUE(S)
lengthHour = None
lengthMinute = None
# JUST ONE ITEM LENGTH VALUE, LIKE 45m OR 2h
if len(str(movieLengthSum).split()) == 1:
        if 'h' in list(str(movieLengthSum)):
                lengthHour = str(movieLengthSum).strip('hm')    # removing the "h" or "m" values, i know, in this case, just 'h' should be there
        if 'm' in list(str(movieLengthSum)):
                lengthMinute = str(movieLengthSum).strip('hm')

# TWO ITEMS LENGTH VALUES, LIKE 2h 32m
if len(str(movieLengthSum).split()) == 2:
        lengthList = str(movieLengthSum).split()
        lengthHour = lengthList[0].strip('hm')
        lengthMinute = lengthList[1].strip('hm')

# ADDING THE VALUES TO EXCEL
# MOVIE TITLE
cell = 'C' + str(cellnumber)
ws[cell].value = titleRead
# YEAR OF RELEASE 
cellRYear = 'E' + str(cellnumber)
ws[cellRYear].value = yearRead

# DIRECTOR(S)
cellRDirector_1 = 'F' + str(cellnumber)
ws[cellRDirector_1].value = director_1_Read

if director_2_Read != None:
        cellRDirector_2 = 'F' + str(int(cellnumber) + 1)
        ws[cellRDirector_2].value = director_2_Read

if director_3_Read != None:
        cellRDirector_3 = 'F' + str(int(cellnumber) + 1)
        ws[cellRDirector_3].value = director_3_Read

# STAR(S)
cellRStar_1 = 'G' + str(cellnumber)
ws[cellRStar_1].value = star_1_Read

if star_2_Read != None:
        cellRStar_2 = 'G' + str(int(cellnumber) + 1)
        ws[cellRStar_2].value = star_2_Read

if star_3_Read != None:
        cellRStar_3 = 'G' + str(int(cellnumber) + 2)
        ws[cellRStar_3].value = star_3_Read


# GENRE(S)
cellRGenre_1 = 'H' + str(cellnumber)
ws[cellRGenre_1].value = genre_1_Read

if genre_2_Read != None:
        cellRGenre_2 = 'I' + str(cellnumber)
        ws[cellRGenre_2].value = genre_2_Read

if genre_3_Read != None:
        cellRGenre_3 = 'J' + str(cellnumber)
        ws[cellRGenre_3].value = genre_3_Read


# MOVIE LENGTH
if lengthHour != None:
        cellLengthHour = 'Q' + str(cellnumber)
        ws[cellLengthHour].value = str(lengthHour)
if lengthMinute != None:
        cellLengthMin = 'R' + str(cellnumber)
        ws[cellLengthMin].value = str(lengthMinute)

# 1st TIME WATCHING
cellRFirst = 'O' + str(cellnumber)
ws[cellRFirst].value = '1st'        


wb.save('MoviePY.xlsx')
driver.quit()
sys.exit()