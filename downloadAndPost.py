import downloadMemes as dm
import postMemes as pm
import sys

def dap(sr,lim,mess,grp):
    dm.download(limit=lim,subreddit=sr)
    pm.post(groups=grp,limit=lim, message=mess)

subreddit='mathmemes'
limit=10
message='#mathMemeTeusday #neverForget'
groups=True

if(len(sys.argv)>1):
    subreddit=sys.argv[1]
if(len(sys.argv)>2):
    limit=sys.argv[2]
if(len(sys.argv)>3):
    message=sys.argv[3]

dap(subreddit,limit,message,groups)
