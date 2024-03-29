#!/usr/bin/python
from operator import itemgetter
import sys


def main(argv):
	current_fromData = None
	current_count = 0
	author = None
    
	# input comes from STDIN
	for line in sys.stdin:
	    # remove leading and trailing whitespace
	    line = line.strip()
	
	    # parse the input we got from mapper.py
	    fromData, count = line.split('\t', 1)
	
	    # convert count (currently a string) to int
	    try:
	        count = int(count)
	    except ValueError:
	        # count was not a number, so silently
	        # ignore/discard this line
	        continue
	
	    # this IF-switch only works because Hadoop sorts map output
	    # by key (here: word) before it is passed to the reducer
	    if current_fromData == fromData:
	        current_count += count
	    else:
	        if current_fromData:
	            # write result to STDOUT
	            print '%s\t%s' % (current_fromData, current_count)
	        current_count = count
	        current_fromData = fromData
	
	# do not forget to output the last word if needed!
	if current_fromData == fromData:
	    print '%s\t%s' % (current_fromData, current_count)

if __name__ == "__main__":
    main(sys.argv)
	
