# yt-comment-posting-bot



![alt text](https://medianopol.ro/wp-content/uploads/2023/01/yt-comment-posting-bot-2048x1024.png "YouTube Comment Posting Bot Banner")

This is a Python Bot for YouTube that posts comments on the newest videos.

# Prerequisites
1. YouTube account needs to have the two step verification off in order to automatically log in. If you do not disable this, you will always have to manually log in. If you choose to do this manually, you need to modify the `automation.py` script to pause and wait for you to input the password manually. If not, this is how you disable it as per Google 2023:
```
Turn off 2-Step Verification:
1. On your Android phone or tablet, open your device's Settings app Google. Manage your Google Account.
2. At the top, tap Security.
3. Under "Signing in to Google," tap 2-Step Verification. You might need to sign in.
4. Tap Turn off.
5. Confirm by tapping Turn off.
``` 
2. Python 3
3. Jupyter Notebooks (if you want to, but it's very nice to have)

# Installation
1. Clone the repository
2. use `pip install -r requirements.txt` command to install all of the Python modules and packages listed in thre requirements.txt file
3. Create a file called `.pass` in the main folder (yt-comment-posting-bot).
4. inside the `.pass` file write your YouTube account password one the first line.
5. Open `automation.py` and go to Step 02: Inputs Setup and configure the settings for your youtube channel specifically. Also have a look at the comments array.
6. Launch `automation.py` with Python.


# Opening with jupyter notebook
To better test this program and to add new funtionalities, you can use the Jupyter Notebook. This allows you to add snippets of code without having to restart the whole application. To launch the jupyter notebook:

1. navigate to the main folder in CMD
2. launch the virtual environment by writing in CMD:
```
py -m venv ytbot-env
cd ytbot-env\Scripts\
activate
```



To disable your new virtual env write in CMD `deactivate`

3. in the virtual environment write 
`jupyter notebook`
4. click on the `automation.ipynb` notebook

I recommend copying snippets of code from `automation.py` to `automation.ipnyb` to test them out and improve them. Then copy them back to `automation.py` file.



# Contents
The contents of the application will be briefly described here.
## fetched_videos.txt
This file gets populated when the script runts and fetches videos from YouTube. After running this file is emptied.
## visited_links.txt
This file is populated with the unique (stripped) video ID's from YouTube. This ensures that videos are not visited more than once. This file is not deleted and will be constantly populated with video ID's. 
## launch_main_python_file.bat
Use this if you wish to use the Bot with Task Scheduler from Windows for example, to autoamte this script to run everyday or every couple of hours. If you intend to use it, please open it and adapt the path to your system.


# To be fixed:
1. counter resets to 0 sometimes
2. if page takes too long to load the script quits
3. task scheduler appears to not be runnig properly with script at 1 AM for example in the night
