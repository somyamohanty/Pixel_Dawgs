import urllib, urllib2

def get_redirected_url(url):
    opener = urllib2.build_opener(urllib2.HTTPRedirectHandler)
    request = opener.open(url)
    return request.url

fi = open("C:/Users/nrosetti94/Desktop/yfcc100m_dataset-0", "r")

done = 10000
for i in range(done):
    next(fi)

for i in range(50000):
    img_data = next(fi)
    id, url, isvideo = img_data.split("\t")[0], img_data.split("\t")[14], int(img_data.split("\t")[22].strip("\n")) == 1
    if (get_redirected_url(url) != "https://s.yimg.com/pw/images/en-us/photo_unavailable.png") and (isvideo == False):
        urllib.urlretrieve(url, "C:/Users/nrosetti94/Documents/Flickr/sampleimages/"+str(id)+".jpg")

