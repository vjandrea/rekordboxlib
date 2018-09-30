# Rekordbox library for Python
Developed in Python 3.7, tested on macOS and Windows.

Provides some methods to parse Rekordbox XML collections.

## Usage
### Import and initalization

    from rekorboxlib import Rekordbox
    
    coll = Rekordbox('path_to_my_exported_collection.xml')

### Finding duplicates

    coll.list_duplicate_songs()

#### Output:

    Duplicate: - HORN
    TrackID: 66
    file://localhost/Users/<userprofile>/Music/PioneerDJ/Sampler/OSC_SAMPLER/PRESET ONESHOT/HORN.wav  (2010816 bytes)
    TrackID: 158
    file://localhost/Users/<userprofile>/Music/PioneerDJ/Imported from Device/Contents/OSC_SAMPLER/PRESET ONESHOT/HORN.wav  (2010816 bytes)

### List songs in alphabetical order

    from rekorboxlib import Rekordbox
    
    coll = Rekordbox('path_to_my_exported_collection.xml')
    coll.list_sorted_songs()

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
- add a spellchecker for Artists and Titles