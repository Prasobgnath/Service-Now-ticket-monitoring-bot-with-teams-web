# internal imports
import time
# External imports below use pip to install
import pandas as pd                                 #for data analysys
from playsound import playsound                     #for notification sound
from fuzzywuzzy import process                      #for scope maching.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException,ElementClickInterceptedException, JavascriptException, WebDriverException

# Specify the path for below variables
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

# Set Chrome options
opt = Options()
# opt.add_argument("--headless")
# opt.add_argument("--incognito")
# opt.add_experimental_option("debuggerAddress", "localhost:9222")
# Set executable path and open the Chrome browser
opt.add_argument('--user-data-dir=C:'+profile_path)
service = Service(chrome_driver_path)
opt.add_argument('--ignore-certificate-errors')
opt.add_argument('--ignore-ssl-errors')
opt.add_argument('blink-settings=imagesEnabled=false')
driver = webdriver.Chrome(service=service, options=opt)
counter = 0
data = pd.read_excel(inventory_excel)
dns_nodes = data['DNS NODES']
proxy_nodes = data['PROXY NODES']
driver.maximize_window()
playsound(sound)
def main(counter):
    try:
        driver.get(url)

        time.sleep(10)

        # Default frame
        shadowroot = driver.execute_script("return document.querySelector('body>macroponent-f51912f4c700201072b211d4d8c26010').shadowRoot.querySelector('sn-canvas-appshell-root')")

        # Switching to Main iframe contains all the inc details.
        iframe = driver.execute_script("return document.querySelector('body > macroponent-f51912f4c700201072b211d4d8c26010').shadowRoot.querySelector('[id*=main]')")
        driver.switch_to.frame(iframe)

        # Checking if record is empty.
        global no_record
        hold_count = 0
        assign_count = 0
        assign_to_empty = []
        imp_list = []
        try:
            empty_inc = driver.execute_script("return document.querySelector('#incident > div.list2_empty-state-list')")
            no_record = empty_inc.text

        except (NoSuchElementException, AttributeError):
            no_record = "INC YES"
        if no_record == "No records to display":
            print("No Incidents")
        else:
            total_inc_count_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[id*='_total_rows']")))
            element_text = driver.execute_script("return arguments[0].textContent;", total_inc_count_element)

            incoutof = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[id*=_last_row]")))
            outof = driver.execute_script("return arguments[0].textContent;", incoutof)

            print("Total Tickets Open :", element_text, "\n")
            # inc = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[aria-label*='Open record: INC']")))
            # inc_num = driver.execute_script("return arguments[0].textContent;", inc)
            print("{:<11} : {:<15} : {:<15} : {:<20} : {:<20} : {} ".format("Number", "Priority", "State",
                                                                            "Assignment Group", "Assigned_to",
                                                                            "Short Description"))
            inc_data = []

            def readcoulum():
                def append():
                    if "2 - High" in priority:
                        if cd_inc not in imp_list:
                            imp_list.append(at)
                    if "1 - Critical" in priority:
                        if cd_inc not in imp_list:
                            imp_list.append(at)

                    else:
                        if at not in assign_to_empty:
                            if at not in imp_list:
                                assign_to_empty.append(at)

                tbody = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                    (By.XPATH, "//tbody[contains(@class,'list2_body -sticky-group-headers')]")))
                rows = tbody.find_elements(By.TAG_NAME, "tr")
                time.sleep(3)
                for row in rows:
                    cells = row.find_elements(By.TAG_NAME, "td")
                    # row_data = [cell.text.strip() for cell in cells]

                    cd_inc = cells[inc_column_no].text.strip()
                    cd_sd = cells[short_des_column_no].text.strip()
                    aff_user = cells[aff_user_column_no].text.strip()
                    priority = cells[priority_column_no].text.strip()
                    state = cells[state_column_no].text.strip()
                    group = cells[assignment_group_column_no].text.strip()
                    assigned_to = cells[assigned_to_column_no].text.strip()
                    # cd_des = cells[15].text.strip()
                    scope = []
                    dt = "{:<11} : {:<15} : {:<15} : {:<20} : {:<20} : {} ".format(cd_inc, priority, state, group,assigned_to, cd_sd)

                    if dt in inc_data:
                        pass
                    else:
                        inc_data.append(dt)
                        if  "(empty)" in assigned_to:

                            at = "{:<11} : {:<15} : {:<15} : {:<20} : {} ".format(cd_inc, priority, state, group,cd_sd[0:18])
                    

                            def scope_match(search, column, at):
                                scope = []  # Initialize scope inside the function
                                closest_match = process.extractOne(search, column)
                                if column is dns_nodes:
                                    if closest_match[1] >= 90:
                                        scope.append("DNS SCOPE")
                                    else:
                                        scope.append("Unknown SCOPE")
                                elif column is proxy_nodes:
                                    if closest_match[1] >= 90:
                                        scope.append("PROXY SCOPE")
                                    else:
                                        scope.append("Unknown SCOPE")
                                at = "{:<11} : {:<15} : {:<15} : {:<20} : {} ".format(cd_inc, priority, scope[0], group,cd_sd[0:18])
                                
                                return at

                            at = scope_match(cd_sd, dns_nodes, at)
                            if "Unknown SCOPE" in at:
                                at = scope_match(cd_sd, proxy_nodes, at)
                                append()
                            else:
                                append()

                                # print(node)

            # time.sleep(5)
            try:
                firstpg = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, """(//button[contains(@id,"_first")])[2]""")))
                firstpg.click()
            except ElementClickInterceptedException:
                pass
            time.sleep(5)
            nextpag = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, """(//button[contains(@id,"next")])[2]""")))
            lastpg = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, """//button[contains(@class,"list_nav  btn btn-icon h_flip_content tab_")]""")))
            while True:

                try:

                    time.sleep(5)
                    readcoulum()

                    if not nextpag.is_enabled():
                        break
                    nextpag.click()
                    time.sleep(5)
                    readcoulum()
                except StaleElementReferenceException:
                    print("Stale exception")
                    driver.refresh()
                    time.sleep(10)
            try:
                firstpg = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, """(//button[contains(@id,"_first")])[2]""")))
                firstpg.click()
                time.sleep(5)
            except ElementClickInterceptedException:
                pass
            for rows in inc_data:
                print(rows)
                if "On Hold" in rows:
                    hold_count += 1
                if "Assigned" in rows:
                    assign_count += 1
            print("Total INC Captured = ", len(inc_data), " On Hold = ", hold_count, "Assigned = ", assign_count,
                  "Not Assigned = ", len(assign_to_empty))
            print(" ")

            for i in assign_to_empty:
                print(i)

        def message():
            #  switch to teams tab
            driver.get("https://teams.microsoft.com/v2/")
            time.sleep(15)
            try:
                gre1 = "Hi Team, We Have Unassigned Tickets in Queue"
                gre2 = "This is an automated message no reply expected,Thanks"
                send_id = WebDriverWait(driver, 30).until(EC.presence_of_element_located(
                    (By.XPATH, """// span[contains( @ title,"""+ sent_id +""" )]"""))).click()
                Type_msg = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, """//div[contains(@placeholder,"Type a message")]""")))
                Type_msg.send_keys(gre1)
                time.sleep(1)
                Type_msg.send_keys(Keys.ENTER)
                time.sleep(2)

                if imp_list != []:

                    imp = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                        (By.XPATH, """(//div[contains(@class,"ui-toolbar__itemicon")])[4]"""))).click()
                    bold = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                        (By.XPATH, """(//div[contains(@class,"ui-toolbar__itemicon")])[1]"""))).click()
                    # Important = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, """//div[contains(text(),"Important")]"""))).click()
                    time.sleep(1)
                    for inc in imp_list:
                        Type_msg.send_keys(inc)
                        Type_msg.send_keys(Keys.ALT, Keys.ENTER)
                        time.sleep(1)
                    Type_msg.send_keys(Keys.ENTER)
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                        (By.XPATH, """(//div[contains(@class,"ui-toolbar__itemicon")])[32]"""))).click()
                if assign_to_empty != []:
                    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, """(//div[contains(@class,"ui-toolbar__itemicon")])[4]"""))).click()
                    time.sleep(1)
                    for inc1 in assign_to_empty:
                        Type_msg.send_keys(inc1)
                        Type_msg.send_keys(Keys.ALT, Keys.ENTER)
                        time.sleep(1)
                    Type_msg.send_keys(Keys.ENTER)
                    time.sleep(1)
                    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, """(//div[contains(@class,"ui-toolbar__itemicon")])[32]"""))).click()
                time.sleep(2)
                Type_msg.send_keys(gre2)
                time.sleep(1)
                Type_msg.send_keys(Keys.ENTER)
                time.sleep(2)
            except ElementClickInterceptedException:
                driver.refresh()
            # Switch back to the original tab

        if assign_to_empty != [] or imp_list != []:
            playsound(sound)
            message()
        else:
            driver.get("https://teams.microsoft.com/v2/")


    except (JavascriptException, TimeoutException, NameError, WebDriverException) as er:
        print(er)
        driver.refresh()
        counter = 0
        time.sleep(3)


while True:

    main(counter)
    counter += 1
    print("Waiting for sleep time")
    time.sleep(sleep_time)
