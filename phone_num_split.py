"""Split a UK Telephone Number into Area Code and Local Number"""
import argparse
import logging
from landline import Landline, landline

def main():
    parser = argparse.ArgumentParser(   description="split uk telephone number into area code and local number",
                                        allow_abbrev=True, #Allows abbreviation if unambiguous
                                        epilog="\"phone-num-split\" (version 0.0.0) by adam bonner, 2021")
    parser.add_argument('telephone',
                        metavar='<telephone_number>',
                        type=str,
                        nargs="+",
                        help="enter a uk mainland telephone number")
    parser.add_argument("-b", "--brackets", dest="bracket_flag",
                        action="store_true", default="False",
                        help="formatted number will include brackets")
    args = parser.parse_args()

    #argparse returns an array, use join+map to serialise it:
    joined_telephone = "".join(map(str,args.telephone))

    # Log some behind-the-scenes config passed out of argparse
    logging.basicConfig(format='%(message)s', level=logging.ERROR)
    logging.debug("raw numbers:\t" + str(args.telephone))
    logging.debug("joined num:\t" + str(joined_telephone))
    logging.debug("brackets?:\t" + str(args.bracket_flag).lower())

    # create a landline object with the joined_telephone
    landline = Landline(joined_telephone)
    print(landline.pretty)

if __name__ == "__main__":
    main()