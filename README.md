How to use:
1) Create a credential file
Use the example file as a refrence below are links on how to get your Group Me and Reddit Credinetials
https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example <- Reddit
https://dev.groupme.com/tutorials/oauth <- GroupMe

2) Create targets file
This is the file containing all the groups/user you want to post to
If you only want to send messages in direct chat you can just type the users name
If you want to send to Groups you will need the group ID
https://dev.groupme.com/docs/v3#groups_index <- Get group ID with GroupMe API

3) Change downloadAndPost.py
With download you can set the number of Memes you want to download and the subreddit you want the memes from
download(limit=10, subreddit='mathmemes') <-Default

With post you can change if you are sending to groups or indiviulas and the message
post(groups=True, message='#mathMemeMonday') <-Default

4) Run
