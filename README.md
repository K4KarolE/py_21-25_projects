21 - Movie Length Scraping - Excel + Selenium
- take an already existing title(which does not have movie length yet) + it`s release year from the excel sheet 
- look for it on IMDb
- open the first match in the roll down results = open the title`s movie database site
- take the length of the movie
- paste it into the excel sheet
- repeat it for the full sheet -> we are going to have a better estimations about the total time spent on watching movies

22 - Movie Details Scraping - Excel + Selenium / optimized for movies, not ideal for TV series, TV specials /
- ask the new title`s IMDb link
- collect the movie details(title, director, stars..) from the site and add to the excel sheet
- open the poster image in the same tab (the poster image is not 'right click saveable' on IMDb by default)
- in a new browser tab look for the movie`s hungarian title
- end of process confirmation message displayed

23 - TV Show Details Scraping - Excel + Selenium / optimized for TV series /
- same behavior as project 22, just for TV shows

24 - Movie Quotes To Clipboard - V1 - Chapter 6 - Practice
- start the program in command line -> it will copy the value of the keyphrase to clipboard

24 - Movie Quotes To Clipboard - V2 - Chapter 6 - Practice
- ask the user for a keyword or list of the keywords or quite
- the movie quote belongs to the keyword will be displayed and copied to the clipboard

25 - Polymorphic Table - Chapter 6 - Practice
- ask the user for the number of words should be displayed (1-100)
- ask the user for the number of columns should we use
- create a list for every column
- find the longest word/item in every column, it`s length will be the width of that column
