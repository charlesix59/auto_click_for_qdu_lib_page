import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
browser = webdriver.Firefox()

headers ={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"}
url="http://10.16.164.135/"
name="输入你学号"
password="输入你的密码"
browser.get(url)
print(browser.current_url)
time.sleep(5)
browser.find_element_by_tag_name("input").click()
browser.find_element_by_id("username").send_keys(name)
browser.find_element_by_id("password").send_keys(password)
time.sleep(1)
browser.find_element_by_xpath("//form//button").click();
js = "window.open('http://10.16.164.135/redir.php?catalog_id=121&object_id=2737')"
browser.execute_script(js)
handles = browser.window_handles#获取当前浏览器的所有标签页
browser.switch_to.window(handles[1])#定位到第二个标签页
time.sleep(1)
print(browser.current_url)
while 1:
    time.sleep(305)
    print(browser.switch_to.alert.text)
    browser.switch_to.alert.accept()
    
    
