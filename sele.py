from selenium import webdriver
import random
import time as times

first = "BCGKLPSTY"
later = "BCEFGHKLMPRSTY"
initials = []
copies = 5 

print("Total loops: " + str(copies))
print("Current:")
for i in range(copies + 1):
    f = first[random.randint(0, len(first) - 1)]
    l = later[random.randint(0, len(later) - 1)] + later[random.randint(0, len(later) - 1)]
    initials.append(f + l)
    
for i in range(copies + 1):
    print(i+1)
    chromedriver = "C:/Users/Woon/Documents/ICT/chromedriver_win32/chromedriver.exe"
    driver = webdriver.Chrome(chromedriver)
    driver.get("https://forms.gle/yyfdcfSJgwJRaq1H6")

    name = driver.find_element_by_xpath('//input[@jsname="YPqjbf"]')
    
    male = driver.find_element_by_xpath('//div[@data-value="Male"]')
    female = driver.find_element_by_xpath('//div[@data-value="Female"]')
    
    b_twelve = driver.find_element_by_xpath('//div[@data-value="Below 12"]')
    twelve = driver.find_element_by_xpath('//div[@data-value="12 - 18"]')
    eighteen = driver.find_element_by_xpath('//div[@data-value="18 - 30"]')
    a_thirty = driver.find_element_by_xpath('//div[@data-value="Above 30"]')
    
    l_once = driver.find_element_by_xpath('//div[@data-value="Less than once a week"]')
    once = driver.find_element_by_xpath('//div[@data-value="Once a week"]')
    twice = driver.find_element_by_xpath('//div[@data-value="Twice a week"]')
    more = driver.find_element_by_xpath('//div[@data-value="More than that"]')
    
    yes1 = driver.find_element_by_xpath('//div[@id="i54"]')
    no1 = driver.find_element_by_xpath('//div[@id="i57"]')
    
    yes2 = driver.find_element_by_xpath('//div[@id="i64"]')
    no2 = driver.find_element_by_xpath('//div[@id="i67"]')

    yes3 = driver.find_element_by_xpath('//div[@id="i74"]')
    no3 = driver.find_element_by_xpath('//div[@id="i77"]')

    yes4 = driver.find_element_by_xpath('//div[@id="i84"]')
    no4 = driver.find_element_by_xpath('//div[@id="i87"]')
    
    submit = driver.find_element_by_xpath('//div[@role="button"]')

    s_1 = random.random()
    if s_1 < 0.6:
        gender = male
    else:
        gender = female

    s_2 = random.random()
    if s_2 < 0.8:
        age = eighteen
    elif s_2 < 0.9:
        age = twelve
    elif s_2 < 0.95:
        age = b_twelve
    else:
        age = a_thirty
    
    s_3 = random.random()
    if s_3 < 0.4:
        time = l_once
    elif s_3 < 0.7:
        time = once
    elif s_3 < 0.9:
        time = twice
    else:
        time = more
        

    s_4 = random.random()
    if s_4 < 0.7:
        sel_1 = yes1 
    else:
        sel_1 = no1

    s_5 = random.random()
    if s_5 < 0.7:
        sel_2 = yes2
    else:
        sel_2 = no2

    s_6 = random.random()
    if s_6 < 0.7:
        sel_3 = yes3
    else:
        sel_3 = no3

    s_7 = random.random()
    if s_7 < 0.7:
        sel_4 = yes4
    else:
        sel_4 = no4

        
    
    name.send_keys(initials[i])
    gender.click()
    age.click()
    time.click()
    sel_1.click()
    sel_2.click()
    sel_3.click()
    sel_4.click()
    submit.click()

    driver.quit()

    t = random.random()
    if t < 0.6:
        interval = 60
    elif t < 0.8:
        interval = 120
    else:
        interval = 180

    times.sleep(interval)
    
