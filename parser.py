# A parser for horriblesubs.info and other torrent magnet link based rss feeds

import os
import feedparser

horriblesubsrss720 = "http://www.horriblesubs.info/rss.php?res=720"

# List for anime currently watching, might change to a dic
animeWatching = ['[HorribleSubs] Boku no Hero Academia - 81 [720p].mkv']


magnetLinks = []

d = feedparser.parse(horriblesubsrss720)
urls = []


def removeTags(rssFeed):
    """Will remove tag from titles"""
    shows = []
    # Finds titles in RSS
    for i in range(0, len(rssFeed.entries[-1].title)):
        shows.append(rssFeed.entries[i].title)

    # Removes HS tags
    for i in range(0, len(shows)):
        # 15 is magic number for splitting HS tags
        # print(shows[i]) prints original
        # print(shows[i][0:15]) prints without HS tag
        shows[i] = shows[i][15:-4]  # prints without .mkv at end
        # print(shows[i]) prints edited

    return shows


def findLinks(rssFeed):
    links = []

    # Finds links in RSS
    for i in range(0, len(rssFeed.entries[-1].title)):
        links.append(rssFeed.entries[i].link)

    return links


def categorizeLinks(rssFeed, title, links):
    """Categorizes just title and remove [HorribleSubs tags]"""
    print('lol')


shows = removeTags(d)
links = findLinks(d)

print(shows)
print(links)


# magnetTotor = "ih2torrent --file ahahaha.torrent {}".format(magnetLinks[0])
# os.system(magnetTotor)
