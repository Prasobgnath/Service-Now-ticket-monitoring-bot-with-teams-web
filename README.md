ServiceNow incident monitoring bot using selenium and python
------------------------------------------------------------
Internal libraries used 

  >time

External libraries used

  >selenium, pandas, playsound , fuzzywuzzy

Short Summary for libraries
>1. Selenium: This is a powerful tool for automating web browsers. It’s commonly used for web scraping, testing web applications, and automating repetitive web tasks. 	You can control browsers like Chrome, Firefox, and Safari using Selenium.
>2. Pandas: This library is essential for data manipulation and analysis. It provides data structures like DataFrames, which make it easy to handle and analyze large 	datasets. You can perform operations like merging, reshaping, and aggregating data with ease.
>3. Playsound: This is a simple library for playing sound files. It’s lightweight and easy to use, making it perfect for adding audio notifications or sound effects to 	your Python projects.
>4. FuzzyWuzzy: This library is used for fuzzy string matching. It uses the Levenshtein Distance to calculate the differences between sequences, which is useful for 	tasks like deduplication, record linkage, and matching strings that are similar but not exactly the same


Quick install libraries 

	pip install selenium pandas playsound fuzzywuzzy

Dependencies
  
> 1. Stable internet connection
> 2. Compactable chromedriver.exe
> 3. Inventory excel for quick ticket scope identification
> 4. Chrome browser
> 5. Python and the libraries
> 6. Notification sound.wav 

Pre assignments to be made in code

	#Specify the path for below variables
	sound = 'path to your sound .wav file'
	profile_path = 'your chrome profile path type -  chrome://version/'
	chrome_driver_path = "path to your chromedriver.exe file"
	inventory_excel = "path to your inventory list excel for scope identification"

	sleep_time = 180 #interval for the scrip to run 180 - runs in every 3 min.
	url ="https:// link to your snow instance inc queue page"

	# Choose the- teams sender/group name
	sent_id ="'>>Your teams group / individual id<< '"

	# provide the column numbers as per your SNOW instance.
	inc_column_no = 2
	short_des_column_no = 4
	aff_user_column_no =5
	priority_column_no = 7
	state_column_no = 8
	assignment_group_column_no = 11
	assigned_to_column_no = 12

Workflow of code.

> 1. Start
> 2. Opening chrome browser with the specified profile (keep your snow and teams profile logged in)
> 3. Navigating to the ServiceNow incident queue link
> 4. Maximizing the browser window plays a sound that you provided.(only on start)
> 5. Checking for unassigned tickets.
> 6. If tickets found categorizing them based on priorities
> 7. Opening teams web checking for the specified group/ id 
> 8. Sending greeting 1 followed by ticket information followed by greeting 2.
> 9. Priority 1 & 2 tickets will be shared on bold text in teams others in normal text.
> 10. Waiting for sleep time 
> 11. After sleep time repeat from step 1
> 12. End!

Note : quick ticket view and sent ticket view will be printed separately on the terminal for headless users.
