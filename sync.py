#!/usr/bin/python
import sys, getopt
import subprocess


# main function 
def main():
    directory = ""
    
    opts, args = getopt.getopt(sys.argv[1:], "d:")
    # print args
    for opt, arg in opts:
        print arg
        if opt == "-d":
            directory = arg
            
    print "directory is ", directory

    print "--------- commit all changes ---------------"

    

    print "--------- pull from repository ----------------"
    process = subprocess.Popen(["git", "pull"], stdout=subprocess.PIPE)
    output = process.communicate()[0]

    print "--------- push to repository ------------------"
    process = subprocess.Popen(["git", "push"], stdout=subprocess.PIPE)
    output = process.communicate()[0]
    
    print "output->", output
    

if __name__ == "__main__":
    main()
