import feedparser
from deluge_client import DelugeRPCClient

horriblesubsrss720 = "http://www.horriblesubs.info/rss.php?res=720"
delugeClient = DelugeRPCClient('127.0.0.1', 12345, 'username', 'password')
# List for anime currently watching, might change to a dic
animeWatching = ['[HorribleSubs] Gegege no Kitarou (2018)']

d = feedparser.parse(horriblesubsrss720)
urls = []

# Prints the length of the urls
#  Print len(d.entries)

# Finds all magnet links and appends them to array
for i in range(0, len(d.entries) - 1):
    urls.append(d.entries[i].title)
    urls.append(d.entries[i + 1].link)

print urls[0]
