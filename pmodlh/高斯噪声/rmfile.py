#删除之前生成的数据文件

import os, sys

if(os.path.exists("abc_wz.dat")):
	os.remove("abc_wz.dat")
	print "remove abc_wz.dat"
else:
	print "abc_wz.dat not exist"

if(os.path.exists("abc_sj.dat")):
	os.remove("abc_sj.dat")
	print "remove abc_sj.dat"
else:
	print "abc_sj.dat not exist"

if(os.path.exists("abc_xz.dat")):
	os.remove("abc_xz.dat")
	print "remove abc_xz.dat"
else:
	print "abc_xz.dat not exist"