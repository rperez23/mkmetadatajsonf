#! /usr/bin/python3

import re

#this will create a fastchannel.json file

#List of Metadata colums (original naming).  Will be modified to be lowercase.
metadataList = [
'Filename',
'Title',
'Description',
'Wazee Category',
'Format',
'Subtitle Language',
'Audio Language',
'Release Date',
'Season #',
'Production Episode #',
'Episode #',
'Episode Name',
'Development Type',
'Genre',
'SubGenre',
'Host',
'Panel',
'Actors',
'Guests',
'Models',
'Contestants',
'Announcer',
'Narrator',
'Program Version',
'Color',
'Keywords',
'SCC Filename',
'Box.com URL',
'Poster Frame TimeStart',
'Scc Offset',
'House Number',
'Buzzr ID',
'DMH Scope',
'VTR'
]

#run through metadataList[], remove spaces, convert to lower case, remove '#' '.'
for i in range(0,len(metadataList)):
    cat = metadataList[i].lower()
    cat = re.sub('\s+','',cat)
    cat = re.sub('#','',cat)
    cat = re.sub('.','',cat)
    metadataList[i] = cat
