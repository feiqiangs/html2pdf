# -*- coding: utf-8 -*-
#author :sfq
#description : Rendering html to pdf
#note: change path param of main method
import subprocess
class html2pdf:
	def __init__(self,path):
		self.input_file_path = path
	def getpdf(self):
		cmd = 'phantomjs.exe ./main.js '+self.input_file_path
		stdout,stderr = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
		print stderr
		print stdout

if __name__=='__main__':
	cfile = html2pdf(path="http://news.163.com/photoview/00AP0001/2186853.html#p=BPC3QKHP00AP0001")
	cfile.getpdf()
	print 'finished!'