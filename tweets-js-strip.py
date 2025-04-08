import re
import os

oldfile = open('tweets.js','r')
newfile = open('newfile.txt','w')
newfile2 = open('newfile2.txt','w')

for line in oldfile:
    if re.search('full_text',line):
        newfile.write(line)
    else:
        newfile2.write(line)

oldfile.close()
newfile.close()
newfile2.close()

oldfile = open('newfile.txt','r')
newfile = open('tweets_no_rt.txt','w')
newfile2 = open('trash_file.txt','w')
rtcount = 0
tweetcount = 0

for line in oldfile:
    if re.search('RT @',line):
        newfile2.write(line)
        rtcount += 1
    else:
        newfile.write(line)
        tweetcount += 1

oldfile.close()
newfile.close()
newfile2.close()              

fin = open("tweets_no_rt.txt")
fout = open("tweets_stripped.txt", 'w')
lines = fin.readlines()
for line in lines:
    fout.write(line[21:])
fout.close()
fin.close()

fin = open("tweets_stripped.txt")
fout = open("tweets_only.txt", 'w')
lines = fin.readlines()
for line in lines:
    fout.write(line[:-3])
    fout.write("\n")
fout.close()
fin.close()

sep = 'https://t.co/'

fin = open("tweets_only.txt")
fout = open("tweets_wc.txt", 'w')
lines = fin.readlines()
for line in lines:
    fout.write(line.split(sep, 1)[0])
fout.close()
fin.close()

print(f"Task completed successfully. {str(rtcount)} retweets were removed, and {str(tweetcount)} tweets were stripped out and exported to tweets_wc.txt !")
os.remove('newfile.txt')
os.remove('newfile2.txt')
os.remove('trash_file.txt')
os.remove('tweets_no_rt.txt')
os.remove('tweets_only.txt')
os.remove('tweets_stripped.txt')
