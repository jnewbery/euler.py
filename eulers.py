#!/usr/bin/python

from __future__ import print_function
import datetime
import subprocess
import sys,os
from collections import defaultdict as ddict

ALL_USERS = ["user1","user2"] #an array of the users. Each user must have a subdirectory containing their solutions.

def make_command(i,user):
    # function to make the command string.
    return  ["python","%s/eul%s.py" % user,i]       

def main(params):
    # Parse params
    try:
        start = int(params[1])
    except(IndexError):
        start = 1
    try:
        end = int(params[2]) + 1
    except:
        end = 2
    total = (end - start)
    try:
        if (params[3] == "all") or (params[3] not in ALL_USERS):
            users = ALL_USERS
        else:
            users = [params[3]]
    except:
        users = ALL_USERS

    # Get solutions. Index zero is null
    sols =[False]
    for sol in open("solutions.txt",'r').readlines():
        sols.append(sol.rstrip())
            
    results = ddict(list)
    for user in users:
        print(user)
        correctcount = 0
        allstart = datetime.datetime.now()
        
        for i in xrange(start,end):
            
            # Print the script number
            print(i, end='\t')
            
            # Get the time now
            scriptstart = datetime.datetime.now()

            # Construct command, try to run it and print result
            command = make_command(i,user)
            if command:
                sol = subprocess.Popen(command,stdout=subprocess.PIPE).stdout.readline().rstrip()
                if sol == sols[i]:
                    correctcount += 1
                    print("Correct!",end='\t')
                    runtime=str(datetime.datetime.now() - scriptstart)
                    results[i].append( (runtime, user) )
                else:
                    print("Incorrect",end='\t')
                    runtime = "Loser!"
            else:
                print("Missed",end='\t')
                runtime = "Did not compete"

            # Print the time taken
            print(runtime)

        print("%s of %s correct. %.1f%% coverage" % (correctcount, total, 100*float(correctcount)/total))
        print ("TOTAL\t\t" + str(datetime.datetime.now() - allstart))

    # Winner winner chicken dinner...
    for i in xrange(start, end):
        scores = results[i]
        if scores:
            scores.sort(lambda x,y: cmp(x[0],y[0]))
            print("Game %s: Winner: %s" % (i, scores[0]))
        else:
            print("Game %d: No winner" % i)

if __name__ == "__main__":
    """Usage - eulers.py <first> <last> <user>|'all'"""
    main(sys.argv)
