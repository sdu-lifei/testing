'''
Created on 2017-07-05
@author: liff
'''
# encoding=utf8 
import urllib
import sys
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

url='http://tieba.baidu.com/p/5204999850'

page = urllib.urlopen(url)
contents = page.read()

# print contents

page.close()

soup_page = BeautifulSoup(contents,'lxml')

img_links = soup_page.find_all('img', class_='BDE_Image')

img_counter=1

for img_link in img_links:
    img_name='%s.jpg' %img_counter
    urllib.urlretrieve(img_link['src'],img_name)
    print img_link['src']
    img_counter+=1
    if img_counter>=10 :
        break


