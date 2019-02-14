#!/usr/bin/python


#print
#print "downloading the Enron dataset (this may take a while)"
#print "to check on progress, you can cd up one level, then execute <ls -lthr>"
#print "Enron dataset should be last item on the list, along with its current size"
#print "download will complete at about 423 MB"
#import urllib
#url = "https://www.cs.cmu.edu/~./enron/enron_mail_20150507.tar.gz"
#urllib.urlretrieve(url, filename="../enron_mail_20150507.tar.gz") 
#print "download complete!"

import tarfile
import os
os.chdir('D:\\new\\ud120-projects-master\\ud120-projects-master\\tools')
tfile = tarfile.open('enron_mail_20150507.tgz', "r:gz")
tfile.extractall(".")

#print "you're ready to go!"
