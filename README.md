# legacyCbot

I am **LegacyCbot**, a Twitter Bot built to produce info about secondary missions in the Hogwarts Legacy game. You will need to assemble several parts to create a bot like me.

First of all, my very soul, what you call *source code*, requires two tools with the following installation commands in Linux:
+ Requests
`pip install requests`

+ BeautifulSoup
`sudo pip3 install beautifulsoup`
or
`sudo apt-get install python3-bs4`

Next, I work with Tweepy to communicate with Twitter API–for which you will need a [developer account](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api)–. Installation command:
`pip install tweepy`

To end with, I work with a daemon (I have a kind soul though, don’t get the wrong idea) called cron, using crontab tool provided in GNU/Linux like operating systems, which allows you to execute a script with a certain schedule. 
To create a crontab file for root or other users, it is necessary to do it in root mode. 
`sudo su
[sudo] password:`

I use crontab in this way:<br />
`crontab -e -u [username]`<br />
`#Nombre: crontabName`<br />
`SHELL=/bin/sh`<br />
`PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin`<br />
`@daily path/to/your/script/script.sh`
