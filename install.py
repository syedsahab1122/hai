# Codex By KangEhem
from Cython.Build.BuildExecutable import *
import sys, os
help = """
usage: %s [A|B|C] file_name.[py|c]\n
A | auto compile your file to Elf Binary C++
B | build .c extension to Elf Binary C++
C | for convert your file to .c extension
"""%sys.argv[0]
if os.getenv("HOME") not in os.getcwd():
	exit("usage this script at Termux $HOME directory")
try:arg_repr = sys.argv[1]
except:exit(help)
try:input_file = sys.argv[2]
except:exit("Nothing argument file given?")
base_name = os.path.splitext(input_file)[0]
if arg_repr in ["A","a"]:
	build(input_file,'')
	[os.remove(name) for name in [base_name+'.c', base_name+'.o']]
	os.system("strip %s"%base_name)
if arg_repr in ["B","b"]:
	ccompile(base_name)
	clink(base_name)
	os.remove(base_name+'.o')
	os.system("strip %s"%base_name)
if arg_repr in ["C","c"]:
	cycompile(input_file,'')
# Mau Nyari Apaan Cuk ?
