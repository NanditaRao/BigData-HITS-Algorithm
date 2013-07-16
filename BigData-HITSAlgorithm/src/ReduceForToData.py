#!/usr/bin/python
from operator import itemgetter
import sys


def main(argv):
	current_toData = None
	current_count = 0
	toData = None
    
	# input comes from STDIN
	for line in sys.stdin:
	    # remove leading and trailing whitespace
	    line = line.strip()
	
	    # parse the input we got from mapper.py
	    toData, count = line.split('\t', 1)
	
	    # convert count (currently a string) to int
	    try:
	        count = int(count)
	    except ValueError:
	        # count was not a number, so silently
	        # ignore/discard this line
	        continue
	
	    # this IF-switch only works because Hadoop sorts map output
	    # by key (here: word) before it is passed to the reducer
	    if current_toData == toData:
	        current_count += count
	    else:
	        if current_toData:
	            # write result to STDOUT
	            print '%s\t%s' % (current_toData, current_count)
	        current_count = count
	        current_toData = toData
	
	# do not forget to output the last word if needed!
	if current_toData == toData:
	    print '%s\t%s' % (current_toData, current_count)

if __name__ == "__main__":
    main(sys.argv)
	
