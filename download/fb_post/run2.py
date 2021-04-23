from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
import re
from bs4 import BeautifulSoup
from time import sleep
from random import choice

# ACCOUNT
USER = 'dinhdong224@gmail.com'
PASS = 'nopass220$'
SCROLL_PAUSE_TIME = [10.5, 10, 11, 13, 15]
LOGIN_URL = 'https://www.facebook.com/login'
POST_URL = 'https://www.facebook.com/duy.huynh.501/posts/2698101366918044'

def get_link(data):
	flag = True
	# new_data = ''
	if '</div></div>' in data:
		data = data.replace('</div></div>', ' ')
	start_cut = re.findall(r'src', data)
	stop_cut = re.findall(r'/>', data)
	list_string = data.split (' ')
	tmp, meta = [], []
	for element in list_string:
		if start_cut[0] in element:
			flag=True
		if stop_cut[-1] in element:
			flag=False
			meta.append(element)
			continue
		if flag:
			tmp.append(element)
	new_data = ' '.join (tmp)
	# meta_data = ' '.join (meta)
	# symbol = '< > = ,'
	# for i in symbol.split(' '):
	# 	if i in new_data:
	# 		new_data = new_data.replace(i, '')
	meta[0] = meta[0].replace('src="','')
	meta[0] = meta[0].replace('amp;','')
	return meta[0].replace('"/>','')


# LOGIN TO FB
def login(USER, PASS, SCROLL_PAUSE_TIME, LOGIN_URL):

	# OPEN CHROME AND LOGIN
	option = Options()
	option.add_argument("--disable-infobars")
	option.add_argument("--disable-extensions")
	# Pass the argument 1 to allow and 2 to block - CONFIG THE NOTIFICATION SETTINGS
	option.add_experimental_option("prefs", { 
	    "profile.default_content_setting_values.notifications": 2 
	})

	# LOGIN FB AND REDIRECT TO THE NEW SITE
	web = Chrome(chrome_options=option)
	web.get(LOGIN_URL)
	mail = web.find_element_by_name("email")
	mail.clear()
	sleep(1)
	mail.send_keys(USER)
	sleep(2)
	pwd = web.find_element_by_name("pass")
	pwd.clear()
	sleep(1)
	pwd.send_keys(PASS)
	sleep(2)
	pwd.send_keys(Keys.RETURN)
	sleep(4)
	return web

web = login(USER, PASS, SCROLL_PAUSE_TIME, LOGIN_URL)
web.get(POST_URL)

# GET IMG LINK
sleep(10)
page_source = web.page_source
page_b = BeautifulSoup(page_source)

