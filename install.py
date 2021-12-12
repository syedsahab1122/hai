from Cython.Build.BuildExecutable import *
import sys, os
name = os.path.splitext(sys.argv[1])
ccompile(name)
clink(name)
os.remove(name+".o")
os.system("strip %s"%name)

