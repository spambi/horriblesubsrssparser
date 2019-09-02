import os
import feedparser
#import ih2torrent
horriblesubsrss720 = "http://www.horriblesubs.info/rss.php?res=720"

# List for anime currently watching, might change to a dic
animeWatching = ['Arifureta Shokugyou de Sekai Saikyou']
magnetLinks = []

d = feedparser.parse(horriblesubsrss720)
urls = []

# Prints the length of the urls
#  Print len(d.entries)


# Finds all magnet links and appends them to array
for i in range(0, len(d.entries) - 1):
    urls.append(d.entries[i].title)
    urls.append(d.entries[i + 1].link)

print(urls[0])


# Will remove tags for 480p and 720p RSS
def removeTag(title):
    # Will remove [Horrible Subs Tag]
    editTitle1 = title[15:]
    # Will remove file info
    editTitle2 = editTitle1[:-16]
    return editTitle2


removeTag(urls[0])

# Might change a to i and do something with limiting it to length of
#  animeWatcihng Variable idk
a = 0


for i in range(0, len(urls)):
    if animeWatching[a] in urls[i]:
        magnetLinks.append(urls[i + 1])
        if not a >= len(animeWatching):
            i += 1

print(magnetLinks[0].encode('utf-8'))


"""
#IT WENT TO THE WRONG TORRENT BUT OK
# WTF IS COP CRAFT EVEN
# (probs because there isn't arifureta in it anymore so it breaks rip)
# (will add test to check if nothing is in it doesnt do anything)
"""
magnetTotor = "ih2torrent --file ahahaha.torrent {}".format(magnetLinks[0])
os.system(magnetTotor)
