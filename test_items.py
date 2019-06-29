import pytest
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as ec

def test_items(browser):
	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
	browser.get(link)
	# time.sleep(30)
	assert ec.presence_of_element_located(browser.find_element_by_css_selector(".btn-add-to-basket"))
