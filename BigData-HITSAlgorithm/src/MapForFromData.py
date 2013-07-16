#!/usr/bin/python
import sys
import re

fromData_list = []
fromData_result = []

def main(argv):
	# input comes from STDIN (standard input)
    
    try:
        for line in sys.stdin:
            
            if "From" in line:
                processed_line = line[5:]
                fromData = processed_line.strip().split(",")
                for mailid in fromData:
                    fromData_list.append(mailid)
    except "end of file":
        return None
            
    for mailid in fromData_list:
        if mailid[0] == ' ':
            mailid = mailid[1:]
        mailid = mailid[:-1]
        #print author
        fromData_result.append(mailid)
        
    for mailid in fromData_result:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        
        print '%s\t%s' % (mailid, 1)
            
                
if __name__ == "__main__":
    main(sys.argv)
     
