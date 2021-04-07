# HEADLESS-BROWSER

options = FirefoxOptions()
options.add_argument("--headless")
print ("FirefoxOptions %s" % options)
browser = webdriver.Firefox(options=options)
browser.get("https://www.jffd.com/#") #JFFD WEBSITE
