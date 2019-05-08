from groupy.client import Client
from groupy import attachments
import os

def setTargetsFromFile(fileName):
    file=open(fileName,'r')
    targets=[]
    for line in file:
        formatedLine=line.split("\n")
        targets.append(formatedLine[0])
    file.close()
    return(targets)

def getStringFromFile(str,fileName):
    file=open(fileName,'r')
    for line in file:
        if str in line:
            nline=line.split("'")
            file.close()
            return(nline[1])
    file.close()
    return False

def post(groups=True,targetFile='targets.txt',credFile='credientials.txt'):

    token=getStringFromFile('token',credFile)

    client = Client.from_token(token)
    targets=setTargetsFromFile(targetFile)
    postTo=[]
    i=0

    if(not groups):
        for chat in client.chats.list_all():
            if (chat.other_user['name'] in targets):
                print('Adding: '+chat.other_user['name']+' to reciving list')
                postTo.append(chat)
    else:
        for group in client.groups.list():
            if (group.id in targets):
                print('Adding: '+group.name+' to reciving list')
                postTo.append(group)

    for squad in postTo:
        while (i<10):
            atts=[]
            if(not groups):
                print('Posting Meme '+str(i)+' to '+squad.other_user['name'])
            else:
                print('Posting Meme '+str(i)+' to '+squad.name)
            with open('meme'+str(i)+'.jpg','rb') as f:
                image=client.images.from_file(f)
            atts.append(image)
            message=squad.post(text='#mathMemeMonday',attachments=atts)
            f.close()
            os.remove('meme'+str(i)+'.jpg')
            i+=1

    print('All Memes Posted')
