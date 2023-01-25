# yt-comment-posting-bot
This is a Python Bot for YouTube that posts comments on the newest videos.



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
py -m venv envname
cd envname\Scripts\
activate
```



To disable your new virtual env write `deactivate`

3. in the virtual environment write 
`jupyter notebook`
4. click on the `automation.ipynb` notebook


# To be fixed:
1. counter resets to 0 sometimes
2. if page takes too long to load the scrip quits
