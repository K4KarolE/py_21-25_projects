'''
21 - Movie Length Scraping - Excel + Selenium
- take an already existing title(which does not have movie length yet) + it`s release year from the MoviePY excel sheet 
- look for it on IMDb
- open the first match in the roll down results = open the title`s movie database site
- take the length of the movie
- paste it into the excel sheet
- repeat it for the full sheet -> we are going to have a better estimations about the total time spent on watching movies
'''

from openpyxl import load_workbook
wb = load_workbook('MoviePY.xlsx', data_only=True)
ws = wb.active

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#BANNER
print()
k = 50
print('*'*k)    
print(' Please wait, the program is loading '.center(k,'*'))
print('*'*k)



# VALUE EXTRACTION FROM THE EXCEL

cellnumber = 15


cell = 'C' + str(cellnumber)
movietitle = ws[cell].value

cellRYear = 'E' + str(cellnumber)
releaseYear = ws[cellRYear].value

cellLengthHour = 'Q' + str(cellnumber)
movieLengthHour = ws[cellLengthHour].value

cellLengthMin = 'R' + str(cellnumber)
movieLengthMin = ws[cellLengthMin].value


def isItShow():                           # movie titles including S01, S02.. or it`s release year like "1992-1999" are TV shows
    if len(str(releaseYear)) != 4:
        return True
    else:
        for i in str(movietitle).split():
            if i[0] == 'S' and len(i) == 3 and i[1].isdigit() and i[2].isdigit():
                return True

# movietitle == None: empty cell(1 title in at least 3 merged cells)
# movietitle == '-': excluding movies with no english title
# isItShow: excluding TV shows
# movieLengthHour != 0 and movieLengthMin != 0: look for title which does not have length yet        
while movietitle == None or movietitle == '-' or isItShow() or movieLengthHour != None or movieLengthMin != None:   
    cellnumber += 1                                            
    cell = 'C' + str(cellnumber)
    movietitle = ws[cell].value

    cellRYear = 'E' + str(cellnumber)
    releaseYear = ws[cellRYear].value

    cellLengthHour = 'Q' + str(cellnumber)
    movieLengthHour = ws[cellLengthHour].value

    cellLengthMin = 'R' + str(cellnumber)
    movieLengthMin = ws[cellLengthMin].value






searchForMovie = ' '.join([ str(movietitle), str(releaseYear) ])

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
# driver.minimize_window()
driver.get('https://www.imdb.com')  
                                           
try:
    element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'suggestion-search' ))
            )
except:
        driver.quit()


search = driver.find_element(By.ID,'suggestion-search')
search.send_keys(searchForMovie)


time.sleep(2)

search = driver.find_element(By.XPATH,'//*[@id="react-autowhatever-1--item-0"]/a')
search.click()


time.sleep(3)
movieLengthSum = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[2]').text
# taking the 2nd item from "2022 1h 33m"

if 'h' not in list(movieLengthSum) or 'm' not in list(movieLengthSum): # if movie has classification(PG-13): "2022 PG-13 1h 33m" taking the 3rd item
    movieLengthSum = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[3]').text

       
#         driver.quit()

print('******************************************')
print(movieLengthSum)








    # except:                                     # the search engine - first result - movie database combination is not ideal
    #     print()                                 # if there is an error in this sequence
    #     k = len(str(movietitle)) + 35           # below message is displayed and looking for a new title from the excel/movie database
    #     print('*'*k)    
    #     print((' ERROR! - for ' + str(movietitle) + ' (' + str(releaseYear) + ') ').center(k,'*'))
    #     print(' Looking for the next title '.center(k,'*'))
    #     print('*'*k)
    #     print()
    #     break