# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import unittest, time, re, os
import timeit
#####################HEADLESS BROWSER##############################################################S
options = FirefoxOptions()
options.add_argument("--headless")
print ("FirefoxOptions %s" % options)
browser = webdriver.Firefox(options=options)
browser.get("https://www.jffd.com/#") #JFFD WEBSITE
print ("OPEN HEADLESS BROWSER")
#--------------------------------------------------------------------------------------------------
#FILE/APP INIT######################################################################################
#-----------------TIMING----------------------------------------------------------------------------- 
start_time = time.time()
print (start_time)
#----------------------------------------------------------------------------------------------------
path = os.getcwd()
print ("The current working directory is %s" % path)
print(path)
file_name = "SCREENSHOTS"
completeName = os. path. join(path, file_name)
print(completeName)
#------CHECK FOR EXISTING SCREENSHOTS DIR------#
if os.path.isdir('completeName'):
   print ("SCREENSHOTS DIR EXISTS")
else:
   print ("SCREENSHOTS DIR CREATED")
#   os.mkdir(completeName)
#----------------------------------------------#
#try:
#    my_abs_path = completeName.resolve(strict=True)
#except FileNotFoundError:
    # doesn't exist
#    os.mkdir(completeName)
#else:
    # exists
#    print ("SCREENSHOTS DIR EXISTS")
#----------------------------------------------#
f = open('SeleniumJFFDHEADLESS.txt', 'w')
print ("OPEN FILE")
f.write('OPEN FILE \n')
#browser = webdriver.Firefox()  
#browser.get("https://www.jffd.com/#") #JFFD WEBSITE
#time.sleep(15)
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1a.png')
browser.find_element_by_css_selector("button.affirm:nth-child(4)").click() #COOKIES ACCEPTED
print ("COOKIES ACCEPTED")
f.write('COOKIES ACCEPTED \n')
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1b.png')
#time.sleep(15)
#####################################################################################################
#Petco- Shorewood####################################################################################
#CSS SELECTOR  .navbar-header-location > a:nth-child(2)
#XPATH /html/body/div[2]/header/nav/div/div[1]/div/div/div/div/div[1]/a
#
#CSS SELECTOR  button.btn:nth-child(3)
#XPATH  /html/body/div[2]/header/nav/div/div[1]/div/div/div/div/div[1]/button
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1b.png')
#print ("Petco- Shorewood")
#f.write('Petco- Shorewood \n')
#####################################################################################################
#SHIPPING UPDATES#####################################################################################
#CSS SELECTOR  .html-slot-container > div:nth-child(1) > label:nth-child(1) > a:nth-child(1) > span:nth-child(1)
#XPATH  /html/body/div[2]/header/nav/div/div[1]/div/div/div/div/div[2]/div/div/label/a/span
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1c.png')
#print ("SHIPPING UPDATES")
#f.write('SHIPPING UPDATES \n')
#Vet Portal
#CSS SELECTOR  li.dropdown:nth-child(1) > a:nth-child(1)
#XPATH  //*[@id="customer-menu"]
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1d.png')
#print ("Vet Portal")
#f.write('Vet Portal  \n')
######################################################################################################
#Contact Us###########################################################################################
#CSS SELECTOR  li.dropdown:nth-chalogild(2) > a:nth-child(1)
#XPATH  //*[@id="customer-menu"]
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1e.png')
#print ("Contact Us")
#f.write('Contact Us  \n')
######################################################################################################
#MY ACCOUNT DROP DOWN ################################################################################
#CSS SELECTOR  #account-menu
#XPATH  //*[@id="account-menu"]
#—————————————————————Sign In————————————————————----———————————————
browser.find_element_by_id('account-menu').click() #OPENS My Account DROP DOWN
time.sleep(10)
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1f.png')
#Sign In. https://www.jffd.com/
#CSS SELECTOR  a.btn-primary
#XPATH  /html/body/div[2]/header/nav/div/div[1]/div/div/div/div/div[3]/li[3]/div/div/a
#browser.find_element_by_xpath("/html/body/div[2]/header/nav/div/div[1]/div/div/div/div/div[3]/li[3]/div/div/").click()
browser.find_element_by_css_selector("a.btn-primary").click() #Sign In
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1g.png')
print ("My Account DROP DOWN")
f.write('My Account DROP DOWN \n')
browser.back() #BACK TO HOME PAGE
print ("BACK TO HOME PAGE")
f.write('BACK TO HOME PAGE \n')
#NEW CUSTOMER##########################################################################################
#———————————————————————New Customer—————————————————————————————————
browser.find_element_by_id('account-menu').click()
time.sleep(10)
#New Customer Start Here https://www.jffd.com/login/?action=register
#CSS SELECTOR  .dropdown--menu--sign-up > a:nth-child(1)
#XPATH  /html/body/div[2]/header/nav/div/div[1]/div/div/div/div/div[3]/li[3]/div/div/span/a
browser.find_element_by_css_selector("a.btn-primary").click() #New Customer Start Here
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1h.png')
print ("New Customer Start Here")
f.write('New Customer Start Here \n')
browser.back() #BACK TO HOME PAGE
print ("BACK TO HOME PAGE")
f.write('BACK TO HOME PAGE \n')
time.sleep(10)
#ACCOUNT################################################################################################
#————————————————————————Account————————————————————----————————————
browser.find_element_by_id('account-menu').click()
time.sleep(10)
#Account. https://www.jffd.com/account
#CSS SELECTOR  div.content-asset:nth-child(3) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)
#XPATH  /html/body/div[2]/header/nav/div/div[1]/div/div/div/div/div[3]/li[3]/div/div/div/ul/li[1]/a
browser.find_element_by_css_selector("div.content-asset:nth-child(3) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)").click() #Account
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1i.png')
print ("Account")
f.write('Account \n')
browser.back() #BACK TO HOME PAGE
print ("BACK TO HOME PAGE")
f.write('BACK TO HOME PAGE \n')
#ORDERS################################################################################################
#————————————————————————Orders—————————————————————————--------———————
browser.find_element_by_id('account-menu').click()
time.sleep(10)
#Orders  https://www.jffd.com/orders
#CSS SELECTOR  div.content-asset:nth-child(3) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)
#XPATH  /html/body/div[2]/header/nav/div/div[1]/div/div/div/div/div[3]/li[3]/div/div/div/ul/li[2]/a
browser.find_element_by_css_selector("div.content-asset:nth-child(3) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1").click() #Orders
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1j.png')
print ("Orders")
f.write('Orders \n')
browser.back() #BACK TO HOME PAGE
print ("BACK TO HOME PAGE")
f.write('BACK TO HOME PAGE \n')
#MANAGE AUTOSHIP#########################################################################################
#—————————————————————————Manage Autoship———————————————————————————————
browser.find_element_by_id('account-menu').click()
time.sleep(10)
#Manage Autoship. https://www.jffd.com/autoships
#CSS SELECTOR  div.content-asset:nth-child(3) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)
#XPATH  /html/body/div[2]/header/nav/div/div[1]/div/div/div/div/div[3]/li[3]/div/div/div/ul/li[3]/a
browser.find_element_by_css_selector("div.content-asset:nth-child(3) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)").click() #Manage Autoship
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1k.png')
print ("Manage Autoship")
f.write('Manage Autoship \n')
browser.back() #BACK TO HOME PAGE
print ("BACK TO HOME PAGE")
f.write('BACK TO HOME PAGE \n')
#MY PETS##################################################################################################
#——————————————————————————My Pets————————————————————————----------——————
browser.find_element_by_id('account-menu').click()
time.sleep(10)
#My Pets. https://www.jffd.com/mypets
#CSS SELECTOR  div.content-asset:nth-child(3) > ul:nth-child(1) > li:nth-child(4) > a:nth-child(1)
#XPATH  /html/body/div[2]/header/nav/div/div[1]/div/div/div/div/div[3]/li[3]/div/div/div/ul/li[4]/a
browser.find_element_by_css_selector("div.content-asset:nth-child(3) > ul:nth-child(1) > li:nth-child(4) > a:nth-child(1)").click() #My Pets
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1l.png')
print ("My Pets")
f.write('My Pets \n')
browser.back() #BACK TO HOME PAGE
print ("BACK TO HOME PAGE")
f.write('BACK TO HOME PAGE \n')
#FILE/APP CLOSE############################################################################################
#print ("CLOSE FILE")
#f.write('CLOSE FILE \n')
#f.close()
#SHOP######################################################################################################
#FRESH FROZEN DAILY DIETS##################################################################################
#//*[@id="daily-diets"] https://www.jffd.com/daily-meals/
#DROP DOWN DISPLAYS
elementDD = browser.find_element_by_id("shop")
action = ActionChains(browser) #create action chain object
action.click_and_hold(on_element = elementDD) #click and hold the item 
action.perform() #SHOP DROP DOWN ELEMENT
browser.find_element_by_id('daily-diets').click() #https://www.jffd.com/daily-meals/
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1m.png')
browser.back() #https://www.jffd.com/
##PANTRY FRESH##############################################################################################
elementDD = browser.find_element_by_id("shop")
action = ActionChains(browser) #create action chain object
action.click_and_hold(on_element = elementDD) #click and hold the item 
action.perform() #SHOP DROP DOWN ELEMENT
browser.find_element_by_id('pantry-fresh').click()  #PANTRY FRESH
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1n.png')
browser.back()
#VET DIETS##################################################################################################
elementDD = browser.find_element_by_id("shop")
action = ActionChains(browser) #create action chain object
action.click_and_hold(on_element = elementDD) #click and hold the item 
action.perform() #SHOP DROP DOWN ELEMENT
time.sleep(15)
browser.find_element_by_id('vet-diets').click()
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1o.png')
browser.back()
#DIY KITS###################################################################################################
elementDD = browser.find_element_by_id("shop")
action = ActionChains(browser) #create action chain object
action.click_and_hold(on_element = elementDD) #click and hold the item 
action.perform() #SHOP DROP DOWN ELEMENT
time.sleep(15)
browser.find_element_by_id('diy-kits').click()
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1p.png')
browser.back()
#CUSTOM DIETS###############################################################################################
elementDD = browser.find_element_by_id("shop")
action = ActionChains(browser) #create action chain object
action.click_and_hold(on_element = elementDD) #click and hold the item 
action.perform() #SHOP DROP DOWN ELEMENT
time.sleep(10)
browser.find_element_by_id('custom-diets').click()
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1q.png')
browser.back()
#DAILY DIETS################################################################################################
elementDD = browser.find_element_by_id("shop")
action = ActionChains(browser) #create action chain object
action.click_and_hold(on_element = elementDD) #click and hold the item 
action.perform() #SHOP DROP DOWN ELEMENT
time.sleep(10)
browser.find_element_by_id('daily-diets-cats').click()
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1r.png')
browser.back()
#TREATS#####################################################################################################
elementDD = browser.find_element_by_id("shop")
action = ActionChains(browser) #create action chain object
action.click_and_hold(on_element = elementDD) #click and hold the item 
action.perform() #SHOP DROP DOWN ELEMENT
time.sleep(10)
browser.find_element_by_id('treats').click()
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1s.png')
browser.back()
#SUPPLEMENTS################################################################################################
elementDD = browser.find_element_by_id("shop")
action = ActionChains(browser) #create action chain object
action.click_and_hold(on_element = elementDD) #click and hold the item 
action.perform() #SHOP DROP DOWN ELEMENT
time.sleep(10)
browser.find_element_by_id('supplements').click()
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1t.png')
browser.back()
#BIG KIBBLE XPATH = //*[@id="Merchandise"]
#MERCHANDISE################################################################################################
elementDD = browser.find_element_by_id("shop")
action = ActionChains(browser) #create action chain object
action.click_and_hold(on_element = elementDD) #click and hold the item 
action.perform() #SHOP DROP DOWN ELEMENT
time.sleep(10)
browser.find_element_by_id('Merchandise').click() #BIG KIBBLE
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot1u.png')
browser.back()
#-----------------TIMING PLUS CLEANUP--------------------------- 
#print("--- %s seconds ---" % (time.time() - start_time))
#f.write("--- %s seconds ---" % (time.time() - start_time))
#---------------------------------------------------------------
#start = timeit.default_timer()
#end = timeit.timeit()
#print ("EXECUTION TIME")
#print(end - start)
#execT = (end - start)
#f.write('EXECUTION TIME: execT \n')
#endT = time.time()
#print ("EXECUTION TIME")
#print(endT - startT)
#elapT = (endT - startT)
#print ("HEADLESS ELAPSED TIME SECS")
#f.write('HEADLESS ELAPSED TIME SECS: elapT \n')
#FILE/APP CLOSE############################################################################################
#print ("CLOSE FILE")
#f.write('CLOSE FILE \n')
#f.close()
#--------------------------------------------------------------------------------------------------
#JFFD HOME PAGE LINK#########################################################################################
browser.find_element_by_css_selector(".js--logoHome > img:nth-child(1)").click()
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot2k.png')
#CALCULATOR PAGE#############################################################################################
#https://www.jffd.com/dog-food-calculator/
browser.find_element_by_id("feeding-calculator").click() 
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot5.png')
#JFFD HOME PAGE XPATH JustFoodForDogs link /html/body/div[2]/header/nav/div/div[3]/div/div/div[1]/a/img
browser.find_element_by_xpath("/html/body/div[2]/header/nav/div/div[3]/div/div/div[1]/a/img").click()
#--------------------------------------------------------------------------------------------------
#ABOUT US ELEMENT############################################################################################
#elementAU = browser.find_element_by_id("about-us") 
#action = ActionChains(browser) #create action chain object
#action.click_and_hold(on_element = elementAU) #click and hold the item 
#action.perform() #perform the operation (show drop down) #ABOUT US DROPDOWN
browser.find_element_by_id("about-us").click() #ABOUT US DROPDOWN
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot6.png') #SAME AS ScreenShot5.png
#Our Mission XPATH = /html/body/div[2]/header/nav/div/div[3]/div/div/div[2]/div[3]/ul/li[4]/div/div/div/div/div[1]/ul/li[1]/a
browser.find_element_by_xpath("/html/body/div[2]/header/nav/div/div[3]/div/div/div[2]/div[3]/ul/li[4]/div/div/div/div/div[1]/ul/li[1]/a").click()
browser.back() #FEEDING CALCULATOR
##ABOUT US DROPDOWN
#about-us
#XPATH //*[@id="about-us"]
browser.find_element_by_id('about-us').click()
time.sleep(15)

#Our Guarantee
browser.find_element_by_xpath("/html/body/div[2]/header/nav/div/div[3]/div/div/div[2]/div[3]/ul/li[4]/div/div/div/div/div[1]/ul/li[2]/a").click()
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot7.png')
browser.back()
#Our Nutrition Team
browser.find_element_by_id('about-us').click()
time.sleep(25)
browser.find_element_by_css_selector(".col-xl-3 > ul:nth-child(2) > li:nth-child(3) > a:nth-child(1)").click()
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot8.png')
browser.back()
time.sleep(15)

#Careers
browser.find_element_by_id('about-us').click()
time.sleep(15)
browser.find_element_by_xpath("/html/body/div[2]/header/nav/div/div[3]/div/div/div[2]/div[3]/ul/li[4]/div/div/div/div/div[1]/ul/li[4]/a").click()
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot9.png')
browser.back()
#Transitioning †o Free Food
browser.find_element_by_id('about-us').click()
#CSS SELECTOR .col-xl-4 > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)
#browser.find_element_by_xpath("//*[@id="aa"]").click()
#Evidence-Based Research
#browser.find_element_by_xpath("//*[@id="aa"]").click()
browser.find_element_by_css_selector(".col-xl-4 > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)").click()
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot10.png')
browser.back()

#FAQs
browser.find_element_by_id('about-us').click()
time.sleep(5)
#browser.find_element_by_xpath("").click()
browser.find_element_by_css_selector(".col-xl-4 > ul:nth-child(2) > li:nth-child(3) > a:nth-child(1)").click()
time.sleep(25)
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot11.png')
browser.back()

#Customer Reviews
browser.find_element_by_id('about-us').click()
time.sleep(15)
#browser.find_element_by_xpath("").click()
browser.find_element_by_css_selector(".col-xl-4 > ul:nth-child(2) > li:nth-child(4) > a:nth-child(1)").click()
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot12.png')
browser.back()

#Autoship
browser.find_element_by_id('about-us').click()
time.sleep(15)
#browser.find_element_by_xpath("").click()
browser.find_element_by_css_selector(".col-xl-4 > ul:nth-child(2) > li:nth-child(5) > a:nth-child(1)").click()
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot13.png')
browser.back()

#Book A Remote Consult
browser.find_element_by_id('about-us').click()
time.sleep(15)
#browser.find_element_by_xpath("").click()
browser.find_element_by_css_selector(".findus-content > ul:nth-child(3) > li:nth-child(1) > a:nth-child(1)").click()
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot14.png')
browser.back()
#UPCOMING EVENTS
browser.find_element_by_id('about-us').click()
browser.find_element_by_css_selector(".findus-content > ul:nth-child(3) > li:nth-child(2) > a:nth-child(1)").click()
browser.save_screenshot('/Users/scott/Desktop/SCREENSHOTS/ScreenShot15.png')
browser.back()
#BROWSER QUIT################################################################################################
browser.quit()
#--------------------------------------------------------------------------------------------------
