# encoding=utf8 
'''
Created on 2017年7月6日

@author: liff
'''
import urllib

def reporthook(block_read,block_size,total_size):
    if not block_read:
        print "connection opened";
        return
    if total_size<0:
        #unknown size
        print "read %d blocks (%d bytes)" %(block_read,block_read*block_size);
    else:
        amount_read=block_read*block_size;
        print 'Read %d blocks,or %d/%d' %(block_read,amount_read,total_size);
        return 


url = 'http://www.sina.com.cn'
local = 'sina.html'
urllib.urlretrieve(url, local, reporthook)
