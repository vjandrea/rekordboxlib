# Rekordbox library for Python
Developed in Python 3.7, tested on macOS and Windows.

Provides some methods to parse Rekordbox XML collections.

## Usage
### Dependencies
This library relies on untangle to access the XML data

    pip install untangle

### Import and initalization

    from rekorboxlib import Rekordbox
    
    collection = Rekordbox('path_to_my_exported_collection.xml')

### Finding duplicates

    collection.list_duplicate_songs()

#### Output:

    Duplicate: - HORN
    TrackID: 66
    file://localhost/Users/<userprofile>/Music/PioneerDJ/Sampler/OSC_SAMPLER/PRESET ONESHOT/HORN.wav  (2010816 bytes)
    TrackID: 158
    file://localhost/Users/<userprofile>/Music/PioneerDJ/Imported from Device/Contents/OSC_SAMPLER/PRESET ONESHOT/HORN.wav  (2010816 bytes)

### List songs in alphabetical order

    collection.list_sorted_songs()

#### Output:
     - HORN
     - NOISE
     - SINEWAVE
     - SIREN

### Background
I created this to find duplicate entries into my Rekordbox collection, since this function is available 
in Rekordbox itself. Probably I'll add more methods in the future, this is a quick & dirty start.


### TODO
- GUI (Qt5)
- add a duplicate checker for locations
- add a spellchecker for Artists and Titles