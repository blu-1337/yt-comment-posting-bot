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
import requests
from random import randint
import os       
from urllib.parse import urlparse, parse_qs
from contextlib import suppress


def read_password_file(filepath):
    """
    Read and return the user/password file.
    """
    try:
        with open(filepath, 'r') as fd:
            lines = fd.readlines()
            fd.close()
            return lines
    except IOError:
        raise ValueError("Can't open password file for reading.")

# from submodules.password_hashing import say_hi


# # Step 01: Chrome Driver Setup

# In[2]:


driver = uc.Chrome(use_subprocess=True)
driver.maximize_window()  # full screen
url = 'https://www.youtube.com/account'
search_page = ''
driver.get(url)

wait = WebDriverWait(driver, 30)  # time in seconds to wait until timeout

# # Step 02: Inputs Setup
#####################################
#CONFIGURE THIS BEFORE RUNNING SCRIPT
#####################################



username = 'penori.craiova@gmail.com'
password = read_password_file('./.pass')
channel_name = '@soundsolace'  # will be used to detect duplicate comments


search_phrase = 'relaxing sounds'  # what are we searching for?
total_comments = 40  # how many comments should this bot leave?

comment_array = ["Just for anyone that needed to see this: everything will be ok ❤️🥺",
                 "✨💕I'm sending out positive vibes to everyone here. 😘❣💕Have a nice day  🙏 ✨",
                 "Don't know if someone is reading this, but if you are: *You are amazing and beautiful! I believe in you!* ❤️",
                 "To anybody who’s reading this, I pray that whatever is hurting you or whatever you are constantly stressing about gets better. May the dark thoughts, the overthinking, and the doubt exit your mind right now. May clarity replace confusion. May peace and calmness fill your life. 💜💜",
                 "Whoever is reading this, Success is not final, failure is not fatal: it is the courage to continue that counts 💜💜",
                 "Whoever listening to this, may your heart healed from stress and fulfill it with peace. 🌱🌲🌳🌴🌞💕💗",
                 "I wish people aren’t cruel 💜💜", "We all have come here for peace of mind of whatever it is. Just remember that someone loves you. May peace be with you 💜💜",
                 "Literally to the 1% who's reading this, God bless you, and may your dreams come true, stay safe and have a wonderful day 💜💜",
                 "This is Bob. \n 😊 \n 👚 \n 👖 \n 👞 \n He is 0 years old. Every like this comment gets he gets 1 year older. How old will he get?",
                 "Don't press read more... \n \n \n \n \n You now have good luck, press like to activate! 💜💜💜💜",
                 "Everyone has a gift. Find your gift...then pursue it to no end; then that will be your destiny. Your an absolute marksman with your words. I really would like to open my unopened gift. I will try till I am no longer. I figure if you can see and feel the gift, you will be able to open it. 💜💜",
                 "You will face many defeats in life, but never let yourself be defeated 💜💜",
                 "Twenty years from now you will be more disappointed by the things that you didn't do than by the ones you did do. So, throw off the bowlines, sail away from safe harbor, catch the trade winds in your sails. Explore, Dream, Discover 💜💜",
                 "Life is a song - sing it. Life is a game - play it. Life is a challenge - meet it. Life is a dream - realize it. Life is a sacrifice - offer it. Life is love - enjoy 💜💜",
                 "Life is a series of natural and spontaneous changes. Don't resist them; that only creates sorrow. Let reality be reality, let things flow naturally forward in whatever way they like 💜💜",
                 "When I stand before God at the end of my. life, I would hope that I would not have a single bit of talent left, and could say 'I used everything you gave me' 💜💜",
                 "Success is to be measured not so much by the position that one has reached in life as by the obstacles which he has overcome while trying to succeed 💜💜",
                 "What matters in life is not what happens to you but what you remember and how you remember it 💜💜",
                 "Throughout life people will make you mad, disrespect you and treat you bad. Let God deal with the things they do, cause hate in your heart will consume you too 💜💜",
                 "Sometimes you've got to let everything go - purge yourself. If you are unhappy with anything... whatever is bringing you down, get rid of it. Because you'll find that when you're free, your true creativity, your true self comes out 💜💜",
                 "We are what our thoughts have made us; so take care about what you think. Words are secondary. Thoughts live; they travel far 💜💜",
                 "Thousands of candles can be lighted from a single candle, and the life of the candle will not be shortened. Happiness never decreases by being shared 💜💜",
                 "Presence is when you’re no longer waiting for the next moment, believing that the next moment will be more fulfilling than this one 💜💜",
                 "Life’s meaning is not in following someone else, it is in the unfolding of one’s own self. It is not a process of becoming like someone else, it is to be oneself 💜💜",
                 "You have to grow from the inside out. None can teach you; none can make you spiritual. There is no other teacher but your own soul 💜💜",
                 "Don’t let others tell you what you can’t do. Don’t let the limitations of others limit your vision. If you can remove your self-doubt and believe in yourself, you can achieve what you never thought possible 💜💜💜💜",
                 "Whenever you want to achieve something, keep your eyes open, concentrate and make sure you know exactly what it is you want. No one can hit their target with their eyes closed 💜💜",
                 "Those who improve with age embrace the power of personal growth and personal achievement and begin to replace youth with wisdom, innocence with understanding, and lack of purpose with self-actualization 💜💜",
                 "Property may be destroyed and money may lose its purchasing power but, character, health, knowledge and good judgement will always be in demand under all conditions 💜💜"]

comment = comment_array[randint(0,len(comment_array)-1)]

print(comment)


# Functions
def accept_conditions():
    accept_all_conditions_01 = driver.find_element(By.XPATH,
                                                   '//span[text()="Accept all"]')
    if accept_all_conditions_01:
        accept_all_conditions_01.click()
    sleep(2)    


def sign_in():
    sign_in_input_form = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
    sign_in_input_form.send_keys(username)

    next_button = driver.find_element(By.XPATH, '//span[text()="Next"]')
    next_button.click()
    

    password_input_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@type="password"]')))
    password_input_field.send_keys(password)

    # passwordNext > div > button

    next_button = driver.find_element(By.XPATH, '//span[text()="Next"]')
    next_button.click()

    sleep(7)


def search_youtube(search_phrase):
    url = 'https://www.youtube.com/'
    driver.get(url)

    # search_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#search')))
    search_field = driver.find_element(By.XPATH, '//input[@id="search"]')
    search_field.click()
    for letter in search_phrase:
        search_field.send_keys(letter)
        wait_time = random.randint(0, 250) / 1000
        sleep(wait_time)

    # search_field.click()
    search_field.send_keys(Keys.RETURN)
    


def select_filters():
    # click on filters
    filters = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@aria-label="Search filters"]')))
    filters.click()

    # choose from this week
#     this_week = wait.until(EC.visibility_of_element_located((By.XPATH,
#                                                              '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/iron-collapse/div/ytd-search-filter-group-renderer[1]/ytd-search-filter-renderer[3]/a/div/yt-formatted-string')))
#     this_week.click()
    
    today = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                             '//yt-formatted-string[text()="Today"]')))
    today.click()
    
    # get the current url
    return driver.current_url  # returns the current search url
    print(search_page)


def fetch_videos(loop_length):
    def fetching_loop(loop_length):
        while loop_length > 0:
            driver.execute_script(
                'window.scrollTo(0, document.documentElement.scrollHeight)')
            sleep(2)
            loop_length -= 1

    if "No more results" in driver.page_source:
        print("end of search term reached, use another earch term")
        return 
    fetching_loop(loop_length)  # this defines how many times it scrolls down to fetch more videos

    wait.until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, 'ytd-video-renderer')))
    return driver.find_elements(By.CSS_SELECTOR, 'ytd-video-renderer')  # list all videos


def find_comment_section():
    # ActionChains(driver).key_down(Keys.END).key_up(Keys.END).perform()
    driver.execute_script(
        'window.scrollTo(0, document.documentElement.scrollHeight / 4)')  # scroll down to comment section, if this does not work, it will keep on scrolling down

    print('should of went down now a bit')

    comments_found = False
    
    sleep(3)

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
        print("Comment section has been found.")
        return True


def duplicate_comments_found():  # returns true if duplicates found
    sleep(2)  # wait until the comments appear
    all_comments = driver.find_element(By.CSS_SELECTOR, '#comments').get_attribute('innerHTML')
    own_comments_counter = all_comments.count(channel_name)  # apare de două ori când nu e niciun comment
    print('comment found: ', own_comments_counter)

    return own_comments_counter > 1

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


def is_a_yt_shorts(url):
    if 'shorts' in url:
        return True
    else:
        return False
    
def is_video_in_file(video_link):
    with open('./visited_links.txt', 'r') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if video_link in content:
            return True
        else:
            return False


# noinspection PyTypeChecker
def get_yt_id(url, ignore_playlist=False):  # this returns just the id of the video, no www's
    # Examples:
    # - http://youtu.be/SA2iWivDJiE
    # - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
    # - http://www.youtube.com/embed/SA2iWivDJiE
    # - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
    query = urlparse(url)
    if query.hostname == 'youtu.be': return query.path[1:]
    if query.hostname in {'www.youtube.com', 'youtube.com', 'music.youtube.com'}:
        if not ignore_playlist:
        # use case: get playlist id not current video in playlist
            with suppress(KeyError):
                return parse_qs(query.query)['list'][0]
        if query.path == '/watch': return parse_qs(query.query)['v'][0]
        if query.path[:7] == '/watch/': return query.path.split('/')[1]
        if query.path[:7] == '/embed/': return query.path.split('/')[2]
        if query.path[:3] == '/v/': return query.path.split('/')[2]
   # returns None for invalid YouTube url


        


def file_too_large_updater(path):
    if os.path.getsize(path) > (10 * 1024 * 1024):  # bigger than 10MB, dimension is given in Bytes
        os.remove(path)
        with open(path, 'w') as f:  # this makes a new file
            f.write('Create a new text file!')
        print("anewtextfilewascreated")
    else:
        print('nothing happened with file too large updater')

        
def post_comments(total_commentsl: int, comment: str, loop_length: int):
    videos = fetch_videos(loop_length)
    comments_counter = 0
    vid_counter = 0

    print(f'videos have length of {len(videos)}')



            
    # save all videos to text file, if they are not a yt shorts
    for i in range(1, len(videos)+1): 
        try:
            video_views = videos[i-1].find_element(By.CSS_SELECTOR,'#metadata-line > span').get_attribute("innerHTML")
            print(video_views) 
        except Exception as e:
            print("____we are not appending this video number", i)
            print('there is no meta for views, we will continue with next video', 'exception was: ', e)
            continue
        else:  # this gets executed if the try is successful
            if 'views' in video_views:  # check if the word is in there, 1K views denotes a video, all else is a live or playlist
                print('views' in video_views, "is true, the value is", video_views)
                # go to video and do shit
                print('saving video to file...')
                
                
                xpath_string = '(//a[@id="video-title"])[' + str(i) + ']'
                href = videos[i-1].find_element(By.XPATH, xpath_string)
                print(href.get_attribute('href'))
                href = href.get_attribute('href')
                with open('./fetched_videos.txt', 'a') as f:  # this overwrites file and starts it from scratch
                    f.write(href + '\n')  # also puts a new line
            else: 
                print('word views not found, continuing to next file')
                continue
    print("wrote video links to visited_links.txt file")

    # read contents of fetched videos and sanve them to variable        
    with open("fetched_videos.txt", 'r+') as fp:  # r+ is for truncation
        # read an store all lines into list
        lines = fp.readlines()        
#         f.truncate(0) # need '0' when using r+, 
    open('fetched_videos.txt', 'w').close()  # this deletes the file contents

    for line in lines:  # go through each line of fetched videos file
        print(line)
        line = line.replace(" ", "")
        if line == "":
            print('empty line')
            continue
        else:
            print("not empty line")
        if is_a_yt_shorts(line):
            continue
        else:
            video_id = get_yt_id(line)
            if is_video_in_file(video_id):
                print("this video id was found in the visited_links.txt file, continuing...")
                continue
            else:  
                if comments_counter == total_comments:
                    print(f'We reached {total_comments} comments. Stopping script. Goodbye!')
                    break
                    
                # writes link to file
                visited_links_path = "./visited_links.txt"
                with open(visited_links_path, 'a') as f:
                    f.write(video_id)  # also puts a new line
                    print("wrote video link to txt file")
                file_too_large_updater(visited_links_path)  # check if file got too large, to avoid filling up of memory
                # post comment here...
                vid_counter += 1
                print(f'comments counter is {comments_counter}')
                print(f'vid counter is: {vid_counter}')
                print('videocacat________________________')
                

                print('going to video...')




                main_video_list_window = driver.current_window_handle
#                 video = videos[i].find_element(By.CSS_SELECTOR, '#video-title')
                video_link = line
                print('link for video is:', video_link)

#                 if is_a_yt_shorts(video_link):
#                     print("This video already is a YT shorts, skipping it with continue...")
#                     continue
#                 print('this video is not a yt shorts')
#                 video_id = get_yt_id(video_link)

#                 if is_video_in_file(video_id):
#                     print('we already visited this video, lets continue with the next one')
#                     continue  # we already visited this vid, sorry
#                 else:
                    # write video to file
#                 print('video not visited, write to file')
#                 visited_links_path = './visited_links.txt'
#                 with open(visited_links_path, 'a') as f:
#                     f.write(video_id + '\n')  # also puts a new line
#                     print("wrote video link to txt file")


                driver.switch_to.new_window('tab')
                driver.get(video_link)
                print('___opened video in new tab')


                sleep(2)  # wait a bit until the page fully loads


                if(find_comment_section() == False):
#                     driver.execute_script('window.history.go(-1)')
                    driver.close()   
                    driver.switch_to.window(main_video_list_window)
                    print("This video has comment section disabled, going back...")
                    continue


                if duplicate_comments_found():
#                     driver.execute_script('window.history.go(-1)')
                    driver.close()
                    driver.switch_to.window(main_video_list_window)
                    print("This video already has a comment on it! Going back...")
                    continue
                else:
                    wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '#title > h1')))
                    print('found the title :), page is loaded')
                    # do main shit
                    write_comment()
                    comments_counter += 1
                    driver.close()
                    driver.switch_to.window(main_video_list_window)
    if comments_counter != total_comments:
        print('comments counter is not reached, we are increasing loop length')
        post_comments(total_comments - comments_counter, comment, loop_length + 5) 

    






# #     for video in videos:
#     for i in range(0, len(videos)):

        


#         print(videos[i].get_attribute('innerHTML'))

        

# Step 03: accept terms and rights
accept_conditions()
# Step 04: Sign in
sign_in()
# Step 05: Search
# wait for search button to appear, you need to tap yes on phone before this...
search_youtube(search_phrase)
search_page = select_filters()
post_comments(total_comments, comment, 1)

print('____________REACHED END OF PROGRAM')



