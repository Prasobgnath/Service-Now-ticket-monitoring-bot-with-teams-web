ServiceNow incident monitoring bot using selenium and python
------------------------------------------------------------
Internal libraries used 

  >time

External libraries used

  >selenium, pandas, playsound , fuzzywuzzy

Quick install libraries 

>pip install selenium pandas playsound fuzzywuzzy


Dependencies
  
	stable internet connection
 	compactable chromedriver.exe
	inventory excel for quick ticket scope identification
	chrome browser
	python and the libraries
	notification sound.wav 

pre assignments to be made in code

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

working.

1. opening chrome browser with the specified profile (keep your snow and teams profile logged in)
2. navigating to the ServiceNow incident queue link
3. maximizing the browser window plays a sound that you provided.(only on start)
4. checking for unassigned tickets.
5. if tickets found categorizing them based on priorities
6. opening teams web checking for the specified group/ id 
7. sending greeting 1 followed by ticket information followed by greeting 2.
8. priority 1 & 2 tickets will be shared on bold text in teams others in normal text.
9. waiting for sleep time 
10. after sleep time repeat from step 1

Note : quick ticket view and sent ticket view will be printed separately on the terminal for headless users.
