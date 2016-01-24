#!/usr/bin/python  

import os
import os.path
rootdir = "./leetcode/"

for parent, dirnames, filenames in os.walk(rootdir):
    for filename in filenames:
        fp = file(rootdir + filename);
        s = fp.read();
        fp.close();
        arr = s.split("\n");
        if (arr[-1] != "```"):
            del arr[-1];
            print filename + arr[-1] + "!";
