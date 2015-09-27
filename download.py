import urllib, urllib2

def get_redirected_url(url):
    opener = urllib2.build_opener(urllib2.HTTPRedirectHandler)
    request = opener.open(url)
    return request.url

fi = open("trainingset/yfcc100m_dataset-0", "r")


iter_file = open("download_tracker.txt", "r")

done = int(iter_file.readline())

for i in range(done):
    next(fi)

for i in range(10):
    done+=1
    img_data = next(fi)
    id, url, isvideo = img_data.split("\t")[0], img_data.split("\t")[14], int(img_data.split("\t")[22].strip("\n")) == 1
    if (get_redirected_url(url) != "https://s.yimg.com/pw/images/en-us/photo_unavailable.png") and (isvideo == False):
        urllib.urlretrieve(url, "sampleimages/"+str(id)+".jpg")

iter_file = open("download_tracker.txt", "w")
iter_file.write(str(done))
iter_file.close()