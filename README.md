euler.py
========

A framework for running Project Euler solution programs competitively.

Originally written by John Newbery, Mark Brenig-Jones and Jonathan Basseri in summer 2012. Any value from the project can be attributed to Mark and Jonathan. Any crassness can be attributed to John.

To set the framework up, add users to the the users.cfg file, add a directory for each user to the base directory and add the user's solution programs to their directory. The user's directory must be named &lt;user&gt;_euler and the solution program must be named eul&lt;x&gt;.py (but you can add different naming schemes by altering the make_command() function. The solution should output just the solution to the problem.

The solutions.txt file is incomplete.