#!/usr/local/bin/python3

import os

def rename():

	path=os.path.abspath('.')#获得当前工作目录

	filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
	
	for files in filelist:#遍历所有文件

		Olddir=os.path.join(path,files);#原来的文件路径
		
		if os.path.isdir(Olddir):#如果是文件夹则跳过
			continue;

		filename = os.path.splitext(files)[0];#文件名

		if "_jiagu_" in filename:
			filename = "BCZP"
		elif "_1_" in filename :
			filename = "BCZP_360"
		elif "_2_" in filename :
			filename = "BCZP_sjqq"
		elif "_3_" in filename :
			filename = "BCZP_wandoujia"
		elif "_4_" in filename :
			filename = "BCZP_baidu"
		elif "_5_" in filename :
			filename = "BCZP_xiaomi"
		elif "_6_" in filename :
			filename = "BCZP_huawei"
		elif "_7_" in filename :
			filename = "BCZP_oppo"
		elif "_8_" in filename :
			filename = "BCZP_vivo"

		filetype=os.path.splitext(files)[1];#文件扩展名

		Newdir=os.path.join(path,filename+filetype);#新的文件路径

		os.rename(Olddir,Newdir);#重命名

rename();

