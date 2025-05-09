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
> Before trying to get any code to work, make sure your downloaded .py files are in the same folder as your *tweets.js* file. Open the IDE of your choice, and go to File > Open, then File > Run (or equivalent).

[mention-text-counter.py](https://github.com/autumngender/twitter-download-manip/blob/main/mention-text-counter.py) - A simple piece of code that calculates how many times a user has been mentioned in your tweets. Allows for searching of any word, but unless your *tweets.js* file has been run through the other code, it will likely give innacurate counts, as the file at this point is unedited.

[tweets-js-cull-lines.py](https://github.com/autumngender/twitter-download-manip/blob/main/tweets-js-cull-lines.py) - A piece of code that gives you two outputs - "tweets_only.txt" (a file containing every tweet you've ever sent (with some extra elements that can be removed), and "trash.txt" (excess metadata). 
> As of **v2.1.0**, this also removes retweets from your file, as they're not tweets that you specifically wrote.

> As of **v2.1.1**, this also removes internal Twitter links for media and QRTs, as well as punctuation.

If you wanted to turn your tweets into a wordcloud of your most used words, you can do so!
Any site works, but I used https://worditout.com/word-cloud/create. Paste in your formatted text from "tweets_wc.txt", and click Generate.

### This is my entry back into coding, and I hope this is a useful tool! Let me know if you have any ideas or find any bugs. Thank you!
