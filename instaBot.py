from selenium import webdriver
from time import sleep
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

count = 0
list_xpath = "//div[@role='dialog']//li"
profile_url = 'abboud.zaher/'
# profile_url = 'hannaa_farha/'


def login(driver):
    driver.get("https://www.instagram.com")
    sleep(2)
    # Accept coockies
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Accept')]"))).click()

    sleep(4)
    driver.find_element_by_xpath("//input[@name=\"username\"]").clear()
    driver.find_element_by_xpath("//input[@name=\"username\"]") \
        .send_keys(os.environ.get("instaUsername"))

    driver.find_element_by_xpath("//input[@name=\"password\"]").clear()
    driver.find_element_by_xpath("//input[@name=\"password\"]") \
        .send_keys(os.environ.get("instaPassword"))
    driver.find_element_by_xpath("//button[@type=\"submit\"]") \
        .click()
    sleep(4)


def click_button(driver, buttonname):
    driver.find_element_by_partial_link_text(buttonname).click()
    sleep(4)


def check_difference_in_count(driver):
    global count

    new_count = len(driver.find_elements_by_xpath(list_xpath))

    if count != new_count:
        count = new_count
        return True
    else:
        return False


def scroll_down(driver):
    global count
    iter = 0
    while 1:
        scroll_top_num = str(iter * 1000)
        iter += 1
        driver.execute_script("document.querySelector('div[role=dialog] ul').parentNode.scrollTop=" + scroll_top_num)
        try:
            WebDriverWait(driver, 30).until(check_difference_in_count)
        except:
            count = 0
            break



def get_list_from_dialog(driver):


    WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.XPATH, list_xpath)))


    scroll_down(driver)

    list_elems = driver.find_elements_by_xpath(list_xpath)
    users = []

    for i in range(len(list_elems)):
        try:
             row_text = list_elems[i].text
              # if ("Following" == row_text):
             username = row_text[:row_text.index("\n")]
             users += [username]

        except:
            print("continue")

    return users

def check_unfollower(follower_list, following_list):
    # follower_list.sort()
    # following_list.sort()
    unfollower = []

    follower_list = set(follower_accounts)
    followings = set(following_accounts)
    targetusers = followings - followers

    for i in targetusers:
        unfollower.append(i)

    return unfollower


def __main__():
    driver = webdriver.Chrome("D:\ChromDriver\chromedriver.exe")

    # login
    login(driver)
    driver.get('https://www.instagram.com/%s' % profile_url)

    # following_number
    following_number = int(driver.find_element_by_xpath("(//span[@class='g47SY '])[3]").text)
    print(following_number)

    # click following button
    following = click_button(driver, "following")

    print("the following number from the web is {0}".format(following_number))

    # follwing list

    following_list = get_list_from_dialog(driver)
    print("following first length list is {0}".format(len(following_list)))
    following_list=set(following_list)
    following_list = list(following_list)
    print("following length list is {0}".format(len(following_list)))

    # wait
    sleep(5)

    # click close button
    driver.find_element_by_xpath('//div[@class="QBdPU "]/*[name()="svg"][@aria-label="Close"]').click()

    # follower number
    follower_number = int(driver.find_element_by_xpath("(//span[@class='g47SY '])[2]").text)

    print("the follower number from the webis {0}".format(follower_number))

    # click the follwers button
    follower = click_button(driver, "followers")

    # follwers List
    follower_list = get_list_from_dialog(driver)
    print("follower length list is {0}".format(len(follower_list)))

    # print(len(follower_list))
    # for i in follower_list :
    #     print(i)
    print("Ennnnnnnnnnnnndd")
    # wait
    sleep(5)

    # unfollower = check_unfollower(follower_list, following_list)
    # for i in unfollower:
    #     print(i)
    #
    # print(len(unfollower))
    #


__main__()
