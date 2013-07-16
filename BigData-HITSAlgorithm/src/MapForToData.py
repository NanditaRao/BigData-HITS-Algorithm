#!/usr/bin/python
import sys

toDataList_list = []
toData_result = []

def main(argv):
	# input comes from STDIN (standard input)
    for line in sys.stdin:
        if "To" in line:
            toDataList = line[3:].strip().lstrip().split(",")
            if toDataList[-1] == ''  :
                toDataList = toDataList[:-1]	
                toDataList_list.append(toDataList)
            else:
				toDataList_list.append(toDataList)
                
    for toDataL in toDataList_list:	
		for toData in toDataL:
			if toData[0] == ' ':
				toData = toData[1:]
				toData_result.append(toData)
			else:
                        	toData_result.append(toData)
                            
    for toData in toData_result:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        
        print '%s\t%s' % (toData, 1)
                            
                            
if __name__ == "__main__":
    main(sys.argv)
     
