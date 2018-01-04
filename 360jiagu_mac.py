#!/usr/local/bin/python3

import zipfile
import os

#测试360加固
def exec_360_jiagu():
	url = '/Users/sunshine/360jiagubao_mac/jiagu'#加固文件夹路径
	signurl = '/Users/sunshine/signkey/xxx.keystore'#签名文件夹路径
	signpw = 'xxx'#签名密码
	mulpkgurl = '/Users/sunshine/360jiagubao_mac/jiagu/多渠道模板.txt'#多渠道模板
	os.chdir(url)
	os.system('java -jar jiagu.jar -login xxx@qq.com xxx')#登录360加固 账户 密码
	sign_cmd = 'java -jar jiagu.jar -importsign /Users/sunshine/signkey/xxx.keystore xxx xxx xxx'#执行加固 jar 包命令，载入签名文件
	mulpkg_cmd = 'java -jar jiagu.jar -importmulpkg mulpkg.txt'#执行加固 jar 包命令，载入多渠道文件
	jiagu_cmd = 'java -jar jiagu.jar -jiagu app-release.apk /Users/sunshine/360jiagubao_mac/jiagu/output -autosign -automulpkg'#执行加固命令 apk 为 app-release.apk
	result = os.system(jiagu_cmd)
	if not result:
		print ("========" + str(result) + "  加固成功")
	else:
		print ( "加固失败")

		def main():
			exec_360_jiagu()

			main()




