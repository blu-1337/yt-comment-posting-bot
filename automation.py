#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys  # return keys and so on
from selenium.webdriver.chrome.options import Options  # disable notifications
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver import ActionChains
import undetected_chromedriver as uc
from time import sleep
import pyperclip
import random

# from submodules.password_hashing import say_hi


# # Step 01: Chrome Driver Setup

# In[2]:


driver = uc.Chrome(use_subprocess=True)
driver.maximize_window()  # full screen
url = 'https://www.youtube.com/account'
driver.get(url)

wait = WebDriverWait(driver, 30)  # time in seconds to wait until timeout

# # Step 02: Inputs Setup
#####################################
#CONFIGURE THIS BEFORE RUNNING SCRIPT
#####################################


username = 'penori.craiova@gmail.com'
password = input('Enter password for account: ')
backup_code = '4185 0442'  # not necessary
channel_name = 'SOUNDSOLACE'  # will be used to detect duplicate comments


search_phrase = 'rain sounds'  # what are we searching for?
total_comments = 5  # how many comments should this bot leave?
comment = 'beautiful, thanks for sharing I wish everyone a blessed evening <3 💜💜'  # maybe make this and array of comms
comment = "thanks for sharing =) and for everyone who's reading this: have a blessed day! 💜💜"


# Functions
def accept_conditions():
    accept_all_conditions_01 = driver.find_element(By.XPATH,
                                                   '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button')
    if accept_all_conditions_01:
        accept_all_conditions_01.click()


def sign_in():
    sign_in_input_form = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
    sign_in_input_form.send_keys(username)

    next_button_01 = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button')
    next_button_01.click()

    password_input_field = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input')))
    password_input_field.send_keys(password)

    # passwordNext > div > button

    next_button_02 = driver.find_element(By.CSS_SELECTOR, '#passwordNext > div > button')
    next_button_02.click()

    # enter_backup_code_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section > div > div > div.pQ0lne > ul > li:nth-child(5)')))
    # enter_backup_code_button.click()
    #
    # backup_code_input_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#backupCodePin')))
    # backup_code_input_field.send_keys(backup_code)
    # backup_code_input_field.send_keys(Keys.RETURN)

    while True:
        x = input('write ok if you are done and ready to go and you are on the youtube page: ')
        if x == 'ok':
            break

    # accept_all_conditions_02 = driver.find_element(By.XPATH, '//*[@id="button"]')
    # if accept_all_conditions_02:
    #     accept_all_conditions_02.click()


def search_youtube():
    url = 'https://www.youtube.com/'
    driver.get(url)

    # search_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#search')))
    search_field = driver.find_element(By.XPATH,
                                       '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
    for letter in search_phrase:
        search_field.send_keys(letter)
        wait_time = random.randint(0, 1000) / 1000
        sleep(wait_time)

    # search_field.click()
    search_field.send_keys(Keys.RETURN)


def select_filters():
    # click on filters
    filters = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                           '#container > ytd-toggle-button-renderer > yt-button-shape > button')))
    filters.click()

    # choose from this week
    this_week = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                             '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/iron-collapse/div/ytd-search-filter-group-renderer[1]/ytd-search-filter-renderer[3]/a/div/yt-formatted-string')))
    this_week.click()


def fetch_videos():
    driver.execute_script(
        'window.scrollTo(0, document.documentElement.scrollHeight)')
    sleep(2)
    driver.execute_script(
        'window.scrollTo(0, document.documentElement.scrollHeight)')
    sleep(2)
    driver.execute_script(
        'window.scrollTo(0, document.documentElement.scrollHeight)')

    wait.until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, 'ytd-video-renderer')))
    return driver.find_elements(By.CSS_SELECTOR, 'ytd-video-renderer')  # list all videos


def find_comment_section():
    # ActionChains(driver).key_down(Keys.END).key_up(Keys.END).perform()
    driver.execute_script(
        'window.scrollTo(0, document.documentElement.scrollHeight / 4)')  # scroll down to comment section, if this does not work, it will keep on scrolling down

    print('should of went down now a bit')

    comments_found = False

    try:
        driver.find_elements(By.CSS_SELECTOR, '#placeholder-area')
        comments_found = True
    except:
        comments_found = False

    if not comments_found:
        print("initial height scan not enough, proceeding back to top and slowly down by 100px...")
        driver.execute_script('window.scrollTo(0, 0)')
        while True:
            try:
                driver.find_elements(By.CSS_SELECTOR, '#placeholder-area')
                break
            except:
                print('not quite at the comment section, scrolling down a little bit more...')
                driver.execute_script('window.scrollBy(0, 100)')  # scroll down to comment section
                sleep(0.5)
    page_source_text = driver.execute_script('return document.body.innerHTML;')
    if ('Comments are turned off' in page_source_text):
        return False  # comment section found? NO, FALSE
    else:
        return True


def duplicate_comments_found():  # returns true if duplicates found
    sleep(2)  # wait until the comments appear
    all_comments = driver.find_element(By.CSS_SELECTOR, '#comments').get_attribute('innerHTML')
    own_comments_counter = all_comments.count(channel_name)  # apare de două ori când nu e niciun comment
    print('comment found: ', own_comments_counter)

    return own_comments_counter > 2


def write_comment():
    # add comment
    wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '#placeholder-area')))
    comment_box = driver.find_element(By.CSS_SELECTOR, '#placeholder-area')
    comment_box.click()
    print('clicked textbox')

    comment_box = driver.find_element(By.CSS_SELECTOR, '#contenteditable-root')
    print('writing to textbox...')
    #             for letter in comment:  # in case you do not have emojis, but we do have them
    #                 comment_box.send_keys(letter)
    #                 wait_time = random.randint(0, 1000) / 1000
    #                 sleep(wait_time)

    pyperclip.copy(comment)
    sleep(1)
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

    print('pasted comment, now waiting 1 second...')

    sleep(1)
    comment_box_submit = driver.find_element(By.CSS_SELECTOR,
                                             '#submit-button > yt-button-shape > button')
    comment_box_submit.click()
    print('finished writing to textbox, now going back one page after 3 seconds...')
    sleep(3)
    driver.execute_script('window.history.go(-1)')

def post_comments(total_commentsl: int, comment: str):
    videos = fetch_videos()

    print('fetched videos')
    comments_counter = 0
    print(f'videos have length of {len(videos)}')
    for video in videos:
        if comments_counter == total_comments:
            print(f'We reached {total_comments} comments. Stopping script. Goodbye!')
            break

        print(f'comments counter is {comments_counter}')

        try:
            video_views = video.find_element(By.CSS_SELECTOR, '#metadata-line > span:nth-child(2)').get_attribute(
                'innerHTML')
            print(video_views)

            if 'views' in video_views:  # check if the word is in there, 1K views denotes a video, all else is a live or playlist
                # go to video and do shit
                print('video also contains views, nicee, proceding to leave a comment')

                print('clicking on video...')
                video.find_element(By.CSS_SELECTOR,
                                   ' #video-title > yt-formatted-string').click()  # clicks on video title
                print('___clicked video')

                # scroll down to comment section
                #             wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'body')))
                #             driver.find_element_by_tag_name('body').send_keys(Keys.END)

                wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '#title > h1')))
                print('found the title :), page is loaded')

                sleep(2)  # wait a bit until the page fully loads
                if(find_comment_section() == False):
                    driver.execute_script('window.history.go(-1)')
                    print("This video has comment section disabled, going back...")
                    continue


                if duplicate_comments_found():
                    driver.execute_script('window.history.go(-1)')
                    print("This video already has a comment on it! Going back...")
                    continue
                else:
                    # do main shit
                    write_comment()
                    comments_counter += 1
            else:
                print("this is not a video, it's a live or something else")
        except Exception as e:
            print('there is no meta for views, we will continue with next video', 'exception was: ', e)


# Step 03: accept terms and rights
accept_conditions()
# Step 04: Sign in
sign_in()
# Step 05: Search
# wait for search button to appear, you need to tap yes on phone before this...
search_youtube()
select_filters()
post_comments(total_comments, comment)

print('____________REACHED END OF PROGRAM')

sleep(999999)
