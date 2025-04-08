# Welcome!
Within this repository is a collection of Python code you can use to manipulate (and get insight) into your Twitter data. To do this, you'll need to go through a few steps.

## 1. Download your Twitter data.
You can do this by heading to https://x.com/settings/download_your_data (only works on desktop). Enter your password, request your data, and you'll recieve an email / in-app notification within 24-48 hours. Click the download button, then extract the .zip file.

## 2. Find the *tweets.js* file.
This is the file you'll be getting all your data from. Copy this across to an empty folder.

## 3. Ensure Python and a Python IDE are installed. 
Python can be downloaded at https://www.python.org/downloads/.
For an IDE, I'd reccomend you use IDLE, which comes pre-installed with Python.

## 4. Download and run the Python code that you want to use.
> Before trying to get any code to work, make sure your downloaded .py files are in the same folder as your *tweets.js* file.

[mention-text-counter.py](https://github.com/autumngender/twitter-download-manip/blob/main/mention-text-counter.py) - A simple piece of code that calculates how many times a user has been mentioned in your tweets. Allows for searching of any word, but unless your *tweets.js* file has been run through the other code, it will likely give innacurate counts, as the file at this point is unedited.

[tweets-js-cull-lines.py](https://github.com/autumngender/twitter-download-manip/blob/main/tweets-js-cull-lines.py) - A piece of code that gives you two outputs - "tweets_only.txt" (a file containing every tweet you've ever sent (with some extra elements that can be removed), and "trash.txt" (excess metadata).

> If you wanted to turn your tweets into a wordcloud of your most used words, you can do this with a few extra steps.
> > ## 1. Use https://gillmeister-software.com/online-tools/text/filter-and-remove-lines.aspx to remove retweets.
> Retweets appear as seperate tweets, and aren't actually your tweets. To get rid of them, copy and paste the text from "tweets_only.txt", paste it into the website, and in the box labelled "Lines containing the text", type (inc. spaces) ```      "full_text" : "RT ```, press remove lines, then copy the output and replace the contents of your "tweets_only.txt" file with this.
> ## 2. Use the "Find and Replace" tool in a word processor (Notepad, TextEdit, etc)
Find the following text: ```     "full_text" : ``` (copy the block as it is, with all spaces), and replace it with nothing. This gives you a pretty clean list of everything you've ever tweeted.
> ## 3. Create a wordcloud.
> Any site works, but I used https://worditout.com/word-cloud/create. Paste in your formatted text from "tweets_only.txt", and click Generate.

# I have no idea if anyone will bother to do all of this, but I hope it works! Let me know if you have any issues. I may try to streamline this (maybe by experimenting with text removal methods within Python) to save the jumping around to create wordclouds.
