import praw
import urllib

def getStringFromFile(str,fileName):
    file=open(fileName,'r')
    for line in file:
        if str in line:
            nline=line.split("'")
            file.close()
            return(nline[1])
    file.close()
    return False

def download(limit=10, subreddit='mathmemes', credFile='credientials.txt'):
    clientID=getStringFromFile('clientID',credFile)
    secretID=getStringFromFile('secretID',credFile)
    userAgent=getStringFromFile('userAgent',credFile)
    myUsername=getStringFromFile('myUsername',credFile)
    myPassword=getStringFromFile('myPassword',credFile)

    topMemes=[]
    i=0

    reddit=praw.Reddit(client_id=clientID, client_secret=secretID, user_agent=userAgent,username=myUsername,password=myPassword)

    subreddit=reddit.subreddit(subreddit)
    print('Getting top: '+str(limit)+' memes from r/'+subreddit.display_name)
    for submission in subreddit.top('week'):
        if('.jpg' in submission.url or '.png' in submission.url):
            topMemes.append(submission.url)
            i+=1
            if(i>=limit):
                i=0
                break

    for meme in topMemes:
        print('Downloading Meme: '+str(i))
        urllib.request.urlretrieve(meme, 'meme'+str(i)+'.jpg')
        i+=1

    print('All Memes Downloaded')
