# -*- coding: utf-8 -*-

# Dependencies
import pupygrib
import csv
import os 

# File read test function
def file_read_test(checksum: bool = False):
    """will attempt to read a UTF-8 csv named testitem.csv
    If checksum == True, then it will check that item 2 in row 4
    equals the sum of item 2 in row 1 and item 0 in row 4.  Checksum
    is just a quick way to make sure the parsing is being done right.  
    Otherwise it will simply try to read through the file.  
    Main intent is to check that we can read from the large files 
    without actually having to open them.
    Returns true if successful, otherwise returns false."""

    src_path = "C:/Users/andre/Documents/Data Projects/Large_File/"
    src_testfile = 'testitem.csv'
    testfile = src_path + src_testfile
    try:
        with open(testfile, 'r', newline='') as f:
            reader = csv.reader(f)
            gridarray = [row for row in reader]
            if checksum == True:
                if int(gridarray[4][2]) == int(gridarray[1][2]) + int(gridarray[4][0]):
                    return True
                else:
                    return False
        # Close file to complete test
        # If checksum was not elected, return True if no error encountered 
        return True
    except (ValueError, FileNotFoundError, IndexError) as e:
        print(e)
        return False

def main():
    print(file_read_test(checksum = True))

if __name__ == '__main__':
    main()