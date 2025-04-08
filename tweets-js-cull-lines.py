import re

oldfile = open('tweets.js','r')
newfile = open('tweets_only.txt','w')
newfile2 = open('trash.txt','w')

for line in oldfile:
    if re.search('full_text',line):
        newfile.write(line)
    else:
        newfile2.write(line)

oldfile.close()
newfile.close()
newfile2.close()
