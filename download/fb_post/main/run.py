from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
from time import sleep
from random import choice
import requests
import re

USER = 'dinhdongiak@gmail.com' # typing your email
PASS = 'nopass224' # typing your password
SCROLL_PAUSE_TIME = [10.5, 10, 11, 13, 15]
LOGIN_URL = 'https://www.facebook.com/login'
# DH_URL = 'https://www.facebook.com/duy.huynh.501'
# POST_URL = 'https://www.facebook.com/duy.huynh.501/posts/2698101366918044'
CLASS_NAME = '''oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw'''
# OPEN CHROME AND LOGIN
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block - CONFIG THE NOTIFICATION SETTINGS
option.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 2})
def remove_tag(data):
	flag = True
	new_data = ''
	if '</div></div>' in data:
		data = data.replace('</div></div>', '\n')
	for i in data:
		if i == '<':
			flag = False
		if i == '>':
			flag = True
		if flag:
			new_data += i
	symbol = '< > = ,'
	for i in symbol.split(' '):
		if i in new_data:
			new_data = new_data.replace(i, '')
	return new_data

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

def download_file(url, name):
	# NOTE the stream=True parameter below
	with requests.get(url, stream=True, allow_redirects=True) as r:
		r.raise_for_status()
		with open(name, 'wb') as f:
			for chunk in r.iter_content(chunk_size=8192):
				# If you have chunk encoded response uncomment if
				# and set chunk_size parameter to None.
				#if chunk:
				f.write(chunk)
	return name
def login ():
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

# GET LINK FROM THE FILE
with open('link_to_down', 'r+') as f:
	body = f.read()
list_link = body.split ('\n')
web = login()
for POST_URL in list_link:
	# web.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
	sleep(2)
	web.get(POST_URL)
	sleep(10)
	page_source = web.page_source	
	page_b = BeautifulSoup(page_source)
	time = page_b.findAll("b", {"class":"b6zbclly myohyog2 l9j0dhe7 aenfhxwr l94mrbxd ihxqhq3m nc684nl6 t5a262vz sdhka5h4"})
	content = page_b.findAll("span", {"class" : "d2edcug0 hpfvmrgz qv66sw1b c1et5uql b0tq1wua a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb hrzyx87i jq4qci2q a3bd9o3v knj5qynh oo9gr5id hzawbc8m"})
	img_link = page_b.findAll("a", {"class" : "oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 q9uorilb mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso pmk7jnqg i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l i09qtzwb n7fi1qx3 j9ispegn kr520xx4 tm8avpzi"})
	time = remove_tag(str(time[0]))
	content = remove_tag(str(content[0]))
	img_link = get_link(str(img_link[0]))
	with open("post_test", "a+") as f:
		f.write (f'Post {list_link.index(POST_URL)}\n')
		f.write (f'Time: {time}\n')
		f.write (f'Content:\n{content}\n')
		# f.write (f'Image Link: {img_link}')
		# image = download_file(img_link, f'pic/post-{list_link.index(POST_URL)}.jpg')

	# close the old tab
	# web.find_element_by_tag_name('body').send_keys(Keys.COMMAND + '1')
	# web.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
web.close()
