import sys
from Library import hello
from Library import goodbye
if len(sys.argv) == 2:
    hello(sys.argv[1])
    goodbye(sys.argv[1])


