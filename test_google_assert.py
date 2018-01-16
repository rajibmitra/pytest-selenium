#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from selenium import webdriver


browser = webdriver.Chrome("/usr/local/bin/chromedriver")


def test_assert_title_of_homepage():
    browser.get("https://www.google.com/")
    assert browser.title == "Google"
   # browser.quit()

def test_assert_presence_of_login_button():
    browser.get("https://www.google.com/")
    assert browser.find_element_by_link_text("Sign in")
    #browser.quit()


