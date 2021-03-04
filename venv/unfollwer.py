from selenium import webdriver
from time import sleep
import os


def login(driver) :
    driver.get("https://www.instagram.com")
    sleep(4)
    driver.find_element_by_xpath('//*[@id="uc-btn-accept-banner"]').click()
    driver.find_element_by_xpath("//input[@name=\"username\"]").clear()
    driver.find_element_by_xpath("//input[@name=\"username\"]") \
        .send_keys(os.environ.get("instaUsername"))

    driver.find_element_by_xpath("//input[@name=\"password\"]").clear()
    driver.find_element_by_xpath("//input[@name=\"password\"]") \
        .send_keys(os.environ.get("instaPassword"))
    driver.find_element_by_xpath("//button[@type=\"submit\"]") \
        .click()
    sleep(4)


def click_button(driver,buttonname):
    button=driver.find_element_by_partial_link_text(buttonname)
    button.click()
    sleep(4)


def __main__():
    driver = webdriver.Chrome("D:\ChromDriver\chromedriver.exe")
    login(driver)
    driver.get("https://www.instagram.com/abboud.zaher/")
    following=click_button(driver,"following")


__main__()


