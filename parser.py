# A parser for horriblesubs.info and other torrent magnet link based rss feeds

import feedparser
import transmissionrpc
import getopt

tc = transmissionrpc.Client('localhost', port=9091)

horriblesubsrss720 = "http://www.horriblesubs.info/rss.php?res=720"

animeWatchingName = ['Boku no Hero Academia',
                     'Somali to Mori no Kamisama',
                     'Ishuzoku Reviewers']

d = feedparser.parse(horriblesubsrss720)


def removeTags(rssFeed):
    """Will remove tag from titles"""
    shows = []
    # Finds titles in RSS
    try:
        # Use d['entries'] as substitute for d.entries[x].title
        for i in range(0, len(d['entries'])):
            # Appends rssFeed's titles
            shows.append(rssFeed.entries[i].title)
    except IndexError as err:
        print(err.args)
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


def categorizeLinks(feed, shows, links):
    """Will find and categorize links into ['title', 'link']"""
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
                    """ Will append title and link to list that is returned
                    through func """
                    anime.append(feed.entries[i].title)
                    anime.append(feed.entries[i].link)
                else:
                    pass
        # Exception handling
        except IndexError:
            pass
    return anime


def reformatBababoey(lol):
    """Reformat into finalised list (useless atm)"""
    for i in range(0, len(lol)):
        if i % 2:
            None
        else:
            lol[i].replace(lol[i], removeTags(d)[i])
    return lol


bababoey = categorizeLinks(d, removeTags(d), findLinks(d))


def addTorrents(mainList, trans):
    for i in range(0, len(mainList)):
        if i % 2:
            print(mainList[i])
            trans.add_torrent(mainList[i])
        else:
            pass


addTorrents(categorizeLinks(d, removeTags(d), findLinks(d)), tc)
