# ready
# A parser for horriblesubs.info and other torrent magnet link based rss feeds

import feedparser
import transmissionrpc

tc = transmissionrpc.Client('localhost', port=9091)
horriblesubsrss720 = "http://www.horriblesubs.info/rss.php?res=720"

animeWatchingName = ['Boku no Hero Academia',
                     'Somali to Mori no Kamisama']

# List for anime currently watching, might change to a dic
animeWatching = ['[HorribleSubs] Mairimashita! Iruma-kun - 20 [720p].mkv',
                 '[HorribleSubs] Boku no Hero Academia - 81 [720p].mkv',
                 '[HorribleSubs] Somali to Mori no Kamisama - 07 [720p].mkv',
                 '[HorribleSubs] Radiant S2 - 20 [720p].mkv']

magnetLinks = []

d = feedparser.parse(horriblesubsrss720)
urls = []


def removeTags(rssFeed):
    """Will remove tag from titles"""
    shows = []
    # Finds titles in RSS
    try:
        for i in range(0, len(d['entries'])):
            shows.append(rssFeed.entries[i].title)

    except IndexError:
        print('Ended')
        pass

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
    for i in range(0, len(rssFeed['entries'])):
        links.append(rssFeed.entries[i].link)

    return links


#def categorizeLinks(rssFeed, shows, links):
#    """Categorizes just title and remove [HorribleSubs tags]"""
#    nonameAnime = []
#    ballerAnime = []
#    for i in range(0, len(rssFeed['entries'])):
#        try:
#            if animeWatching[i]:
#                ballerAnime.append(rssFeed.entries[i].title)
#                ballerAnime.append(rssFeed.entries[i].link)
#            else:
#                nonameAnime.append(rssFeed.entries[i].title)
#        except IndexError:
#            pass
#    return ballerAnime

def categorizeLinks(feed, shows, links):
    anime = []

    # Make main loop that iterates through all entries
    for i in range(0, len(feed['entries'])):
        # For exception handling
        try:
            # Nested loop to iterate through animeWatching len
            # This loop will only iterate through itself 3 times
            for x in range(0, len(animeWatchingName)):
                # Check if anime name is in feed entries
                if animeWatchingName[x] in feed.entries[i].title:
                    #print('lol yesAHAHAHAHA')
                    # Will append title and link to list that is returned through func
                    anime.append(feed.entries[i].title)
                    anime.append(feed.entries[i].link)
                else:
                    pass
        # Exception handling
        except IndexError:
            pass
    return anime


def reformatBababoey(lol):
    """Reformat into finalised list"""
    for i in range(0, len(lol)):
        if i % 2:
            None
        else:
            lol[i].replace(lol[i], shows[i])
    return lol


shows = removeTags(d)
links = findLinks(d)


bababoey = categorizeLinks(d, shows, links)
reformatBababoey(bababoey)


def addTorrents(mainList, trans):
    for i in range(0, len(mainList)):
        if i % 2:
            print(mainList[i])
            trans.add_torrent(mainList[i])
        else:
            pass


addTorrents(bababoey, tc)

#tc.get_torrents()
#tc.add_torrent(bababoey[0])
