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

23 - Contact Details Collector - Regular Expressions
- ask for a file (location)
- give back the email addresses and phone numbers if there any in the file