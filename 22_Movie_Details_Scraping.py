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
link = input(' Please add the new record`s IMDb link: ')
cellnumber = input(' Please add the row number of the new record: ')



PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get(link)

# MOVIE TITLE
cell = 'C' + str(cellnumber)
movietitle = ws[cell].value

# YEAR OF RELEASE
cellRYear = 'E' + str(cellnumber)
releaseYear = ws[cellRYear].value

# DIRECTOR(S)
cellRDirector_1 = 'F' + str(cellnumber)
director_1 = ws[cellRDirector_1].value

cellRDirector_2 = 'F' + str(int(cellnumber) + 1)
director_2 = ws[cellRDirector_2].value

cellRDirector_3 = 'F' + str(int(cellnumber) + 2)
director_3 = ws[cellRDirector_3].value

# STAR(S)
cellRStar_1 = 'G' + str(cellnumber)
star_1 = ws[cellRStar_1].value

cellRStar_2 = 'G' + str(int(cellnumber) + 1)
star_2 = ws[cellRStar_2].value

cellRStar_3 = 'G' + str(int(cellnumber) + 2)
star_3 = ws[cellRStar_3].value

# GENRE(S)
cellRGenre_1 = 'H' + str(cellnumber)
genre_1 = ws[cellRGenre_1].value

cellRGenre_2 = 'I' + str(cellnumber)
genre_2 = ws[cellRGenre_2].value

cellRGenre_3 = 'J' + str(cellnumber)
genre_3 = ws[cellRGenre_3].value

# MOVIE LENGTH
cellLengthHour = 'Q' + str(cellnumber)
movieLengthHour = ws[cellLengthHour].value

cellLengthMin = 'R' + str(cellnumber)
movieLengthMin = ws[cellLengthMin].value
     

# TAKING THE VALUES FROM THE 
# MOVIE TITLE
try:
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
                By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/h1'))
        )
          
        titleRead = driver.find_element(
        By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/h1').text
             
except:
        print()
        print('*** ERROR - MOVIE TITLE ***')
        print()
        driver.quit()


# # YEAR OF RELEASE
#         try:
#             movieYear = driver.find_element(
#                 By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[1]/span').text
            
#         except:
#             print('Year of release')
#             driver.quit()

# # DIRECTOR(S)
#         try:
#             element = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located(
#                     (By.XPATH, '//*[@id="react-autowhatever-1--item-0"]/a'))
#             )
#             search = driver.find_element(
#                 By.XPATH, '//*[@id="react-autowhatever-1--item-0"]/a')
#             search.click()
#         except:
#             driver.quit()

# # STAR(S)
#         try:
#             element = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located(
#                     (By.XPATH, '//*[@id="react-autowhatever-1--item-0"]/a'))
#             )
#             search = driver.find_element(
#                 By.XPATH, '//*[@id="react-autowhatever-1--item-0"]/a')
#             search.click()
#         except:
#             driver.quit()

# # GENRE(S)
#         try:
#             element = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located(
#                     (By.XPATH, '//*[@id="react-autowhatever-1--item-0"]/a'))
#             )
#             search = driver.find_element(
#                 By.XPATH, '//*[@id="react-autowhatever-1--item-0"]/a')
#             search.click()
#         except:
#             driver.quit()



# # TAKING THE LENGTH VALUE
#         try:
#             element = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located(
#                     (By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[2]'))
#             )

#             # taking the 2nd item(length) from "2022 1h 33m"
#             movieLengthSum = driver.find_element(
#                 By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[2]').text
            
#             # if the movie has classification(pg-13): "2022 pg-13 1h 33m" taking the 3rd item
#             if 'h' not in list(movieLengthSum) or 'm' not in list(movieLengthSum):
#                 movieLengthSum = driver.find_element(
#                     By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[3]').text
#         except:
#             print('Movie length')
#             driver.quit()



# # VALUATE AND TRANSFORM THE LENGTH VALUE(S)
#         lengthHour = None
#         lengthMinute = None
#     # JUST ONE ITEM LENGTH VALUE, LIKE 45m OR 2h
#         if len(str(movieLengthSum).split()) == 1:
#             if 'h' in list(str(movieLengthSum)):
#                 lengthHour = str(movieLengthSum).strip('hm')    # removing the "h" or "m" values, i know, in this case, just 'h' should be there
#             if 'm' in list(str(movieLengthSum)):
#                 lengthMinute = str(movieLengthSum).strip('hm')

#     # TWO ITEMS LENGTH VALUES, LIKE 2h 32m
#         if len(str(movieLengthSum).split()) == 2:
#             lengthList = str(movieLengthSum).split()
#             lengthHour = lengthList[0].strip('hm')
#             lengthMinute = lengthList[1].strip('hm')



# # ADDING THE VALUES TO EXCEL
# # MOVIE TITLE

# # YEAR OF RELEASE 
    
# # DIRECTOR(S)

# # STAR(S)

# # GENRE(S)

# # MOVIE LENGTH
#         if lengthHour != None:
#             ws[cellLengthHour].value = str(lengthHour)
#         if lengthMinute != None:
#             ws[cellLengthMin].value = str(lengthMinute)
                
#         wb.save('MoviePY.xlsx')
        

#         print()                                
#         k = len(str(' NEW RECORD ADDED ')) + 10
#         print('*'*k)
#         print(' NEW RECORD ADDED ')
#         print('*'*k)

#         driver.quit()
#         sys.exit()



#     except:                                     
#         print()                                
#         k = len(str(' DANGER WILL ROBINSON, DANGER ')) + 10
#         print('*'*k)
#         print(' DANGER WILL ROBINSON, DANGER '.center(k, '*'))
#         print('*'*k)
#         print()
#         # wb.save('MoviePY.xlsx')
#         driver.quit()
#         sys.exit()