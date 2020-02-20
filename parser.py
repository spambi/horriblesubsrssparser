# A parser for horriblesubs.info and other torrent magnet link based rss feeds

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
        shows[i] = shows[i][15:-1]  # prints without HS tag
        shows[i] = shows[i][0:-9]  # prints without .mkv at end

    return shows


def findLinks(rssFeed):
    links = []

    # Finds links in RSS
    for i in range(0, len(rssFeed.entries[-1].title)):
        links.append(rssFeed.entries[i].link)

    return links


def categorizeLinks(rssFeed, shows, links):
    """Categorizes just title and remove [HorribleSubs tags]"""
    nonameAnime = []
    ballerAnime = []
    for i in range(0, len(rssFeed.entries[-1].title)):
        if animeWatching[0] in rssFeed.entries[i].title:
            ballerAnime.append(rssFeed.entries[i].title)
            ballerAnime.append(rssFeed.entries[i].link)
        else:
            nonameAnime.append(rssFeed.entries[i].title)
    # print(ballerAnime)
    return ballerAnime


def reformatBababoey(lol):
    """Reformat into finalised list"""
    for i in range(0, len(lol)):
        if i % 2:
            None
        else:
            lol[i].replace(lol[i], shows[i])
            print(lol[i])
    return lol


shows = removeTags(d)
links = findLinks(d)


bababoey = categorizeLinks(d, shows, links)

for i in range(0, len(bababoey)):
    if i % 2:
        print(bababoey[i-1])
        print(bababoey[i])
    else:
        None
