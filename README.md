# Html2pdf 
##description：
A python object . Converting HTML to PDF.
##Python version：
python 2.x
##Operating system (OS)：
windows
##Useage:
1.URL type:
```python
from html2pdf import html2pdf
url='http://news.163.com/photoview/00AP0001/2186853.html#p=BPC3QKHP00AP0001'
temp = html2pdf(url)
temp.getpdf()
```
2. Local HTML file type:
```python
from html2pdf import html2pdf
file_path='./test.html'
temp = html2pdf(file_path)
temp.getpdf()
```
###output
A pdf file 'result.pdf' will been created with the HTML's rendering result.



