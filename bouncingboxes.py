#!/usr/bin/env python3

"""Main file for silly bouncing box demo."""

import sys
from bb import BBDemo

def main():
    """Main function for bounding box demo."""
    sound_on = not 'soff' in sys.argv
    return BBDemo().run(sound_on)

if __name__ == '__main__':
    main()
