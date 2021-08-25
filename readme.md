# phone-num-split
Split a UK Telephone Number into Area Code and Local Number

### Background
UK telephone numbers have a long and complex history. Generally a UK phone number is 10-12 digits long and can be split into two halves. This utility uses pattern logic to derive where the split takes place.

Prefix | Type | Pattern
------ | ---- | -------
01 | Landlines (geographic) | Various – see below
02 | Landlines (geographic) | 02x xxxx xxxx
03 | Landlines (non-geographic) | 03xx xxx xxxx
05 | Corporate numbering and VOIP | 05xxx xxxxxx
07 | Mobiles, pagers and personal | 07xxx xxxxxx
08 | Service numbers (special rates) | 08xx xxx xxxx
09 | Service numbers (premium rates) | 09xx xxx xxxx

### Usage
```ps
# Simple UK Number Splitting
❯ .\phone_num_split.py 01695571412
01695 571412

# Different Patterns for Different Area Codes (e.g. Liverpool)
❯ .\phone_num_split.py 01512973000
0151 297 3000

# Include Brackets with the -b Argument
❯ .\phone_num_split.py +442079460026 -b
(020) 7946 0026

# Supports Country Code and all known UK number formats
❯ .\phone_num_split.py 00447712345600
07712 345600

# Should be robust against various input formats
❯ .\phone_num_split.py 08 00 1 47 53 69
0800 147 5369
```

### Reading
- http://www.area-codes.org.uk/formatting.php
- https://www.ukphoneinfo.com/01-02-geographic-numbers
- https://en.wikipedia.org/wiki/List_of_country_calling_codes