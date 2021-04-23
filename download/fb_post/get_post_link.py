from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
from time import sleep
from random import choice

# GET THE POST LINK FROM FB PROFILE
USER = 'dinhdong224@gmail.com'
PASS = 'nopass220$'
SCROLL_PAUSE_TIME = [10.5, 10, 11, 13, 15]
LOGIN_URL = 'https://www.facebook.com/login'
DH_URL = 'https://www.facebook.com/duy.huynh.501'
# POST_URL = 'https://www.facebook.com/duy.huynh.501/posts/2698101366918044'
CLASS_NAME = '''oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw'''
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
web.get(DH_URL)
sleep(3)

