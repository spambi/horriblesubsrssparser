# A parser for horriblesubs.info and other torrent magnet link based rss feeds
import argparse
import configparser
import feedparser
import sys
import transmissionrpc

animeWatchingName = []
tc = transmissionrpc.Client('localhost', port=9091)

p = configparser.ConfigParser()
# Parser
parser = argparse.ArgumentParser()
# Access through args.add
parser.add_argument('-a', '--add', type=str,
                    help='Adds an anime from the csv config file. (Only works\
                        with singular anime ATM)')
# Access through args.delete
parser.add_argument('-d', '--delete', type=str,
                    help='Deletes an anime from the csv config file. (Only works\
                         with with singular anime ATM')
args = parser.parse_args()


# Writes new anime to parser.ini
def addAnime(aniName, configFile):
    # Reading from file
    with open(configFile, "r") as curFile:
        try:
            p.read_file(curFile)
        except configparser.DuplicateSectionError as err:
            print(err)
            return False

    # Writing to file
    with open(configFile, "w") as curFile:
        # Add the anime name if it doens't pass
        p.add_section(aniName)
        try:
            p.write(curFile)
            print("[+] Wrote to %s" % aniName)
            return True
        except configparser.DuplicateSectionError as err:
            print(err)
            return False


# Deletes anime in parser.ini
def deleteAnime(aniName, configFile):
    temp = []
    sectionName = []
    # Read file to check if aniName is in parser.ini
    with open(configFile, "r") as curFile:
        p.read_file(curFile)
        temp = p.sections()
        # Iterate through read sections and check if they match aniName
        for i in range(len(temp)):
            if temp[i] in aniName:
                # Append the duplicate to tempArray
                sectionName.append(temp[i])
        # Check if there was no duplicates, then return False
        if len(sectionName) == 0:
            print("[-] No Section with that title")
            return False

    # Now delete duplicated section
    with open(configFile, "w") as curFile:
        p.remove_section(sectionName[0])
        p.write(curFile)
        # Use sectionName[0] to be accuracte
        print("[+]Removed: {0} from {1}".format(sectionName[0], configFile))
        return True


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

    # Splits HS Tags from shows
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
                # Had to fuck with nested lists cause fuck csv
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


def addTorrents(mainList, trans):
    """Will add a list of magnetLinks to transmission"""
    for i in range(0, len(mainList)):
        if i % 2:
            print(len(mainList))
            trans.add_torrent(mainList[i])
        else:
            pass


if args.add:
    if addAnime(args.add, 'parser.ini'):
        print("[+] Successfully added %s!" % args.add)
        sys.exit()
    else:
        print("[-] Something went wrong")
        sys.exit()
else:
    pass


if args.delete:
    if deleteAnime(args.delete, "parser.ini"):
        sys.exit()
    else:
        sys.exit()
else:
    pass

# bababoey = categorizeLinks(d, removeTags(d), findLinks(d))  # Is used in
# simplified form for addTorents


horriblesubsrss720 = "http://www.horriblesubs.info/rss.php?res=720"
d = feedparser.parse(horriblesubsrss720)

with open("parser.ini", "r") as f:
    p.read_file(f)
    for i in range(0, len(p.sections())):
        # Formats sections into singular lists
        animeWatchingName.append(p.sections()[i])
    print(animeWatchingName)

addTorrents(categorizeLinks(d, removeTags(d), findLinks(d)), tc)