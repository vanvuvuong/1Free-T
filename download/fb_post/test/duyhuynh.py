from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
from time import sleep
from random import choice


class get_fb_post():
	'''This Object would download the facebook post from a FB profile automating'''
    def __init__(self):
    	# DECLARE THE PARAMETER
    	self.USER = 'dinhdong224@gmail.com'
    	self.PASS = 'nopass220$'
    	self.SCROLL_PAUSE_TIME = [6, 10, 8, 9, 15]
    	self.LOGIN_URL = 'https://www.facebook.com/login'
    	self.DH_URL = 'https://www.facebook.com/duy.huynh.501'

	def login(self) :
		'''This method will login the facebook and redirect to the Target Profile'''

		# SET UP THE CUSTOM OPTIONS FOR CHROME
		option = Options()
		option.add_argument("--disable-infobars")
		option.add_argument("--disable-extensions")
		# Pass the argument 1 to allow and 2 to block - CONFIG THE NOTIFICATION SETTINGS
		option.add_experimental_option("prefs", { 
		    "profile.default_content_setting_values.notifications": 2 
		})
		# LOGIN FB AND REDIRECT TO THE NEW SITE
		web = Chrome(chrome_options=option)
		web.get(self.LOGIN_URL)
		mail = web.find_element_by_name("email")
		mail.clear()
		sleep(1)
		mail.send_keys(self.USER)
		sleep(2)
		pwd = web.find_element_by_name("pass")
		pwd.clear()
		sleep(1)
		pwd.send_keys(self.PASS)
		sleep(2)
		pwd.send_keys(Keys.RETURN)
		sleep(4)
		web.get(self.DH_URL)
		web.maximize_window()
		return web

	def scroll_down(self, browser):
		# get the current document height
		last_height = browser.execute_script("return document.body.scrollHeight")

		# scroll down
		browser.execute_script("window.scrollTo(0, document.body.scrollHeight) ;")

		# get the post data
		self.get_post()

		# waiting for the loading
		pause = choice(self.SCROLL_PAUSE_TIME)
		sleep(pause)

		# compare the profile height to continue run the script
		new_height = browser.execute_script("return document.body.scrollHeight")
		if new_height == last_height:
			return "The Downloading Progress is Done"

	def pre_get_post(self, browser):
		# click the "READ MORE" button
		browser.find_element_by_xpath('//*[@id=\"jsc_c_q\"]/div/div/span/div[3]/div/div').click()
		browser.find_element_by_xpath('//*[@id="jsc_c_1v"]/div/div/span/div[3]/div/div').click()

	def get_post(self,page_source):
		# click on "READ MORE"
		pass




