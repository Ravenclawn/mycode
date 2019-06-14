import sys
import os
root=sys.argv[1]
for d,s,f in os.walk(root):
  print("directory:%s"%d)
  print("sub-folder"+str(s))
  for fa in f:
    print(fa)