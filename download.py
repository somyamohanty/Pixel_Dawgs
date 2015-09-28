import urllib, urllib2

def get_redirected_url(url):
    try:
        opener = urllib2.build_opener(urllib2.HTTPRedirectHandler)
        request = opener.open(url)
    except:
        return ''
    return request.url

fi = open("trainingset/yfcc100m_dataset-0", "r")


iter_file = open("download_tracker.txt", "r")

try:
    done = int(iter_file.readline())
except ValueError:
    done = 0

iter_file = open("download_tracker.txt", "w")

for i in range(done):
    next(fi)

for i in range(100000):
    done += 1
    img_data = next(fi)
    id, url, isvideo = img_data.split("\t")[0], img_data.split("\t")[14], int(img_data.split("\t")[22].strip("\n")) == 1
    try:
        redirected = get_redirected_url(url)
        if (redirected != "https://s.yimg.com/pw/images/en-us/photo_unavailable.png") and redirected != '' and (isvideo is False):
            urllib.urlretrieve(url, "sampleimages/"+str(id)+".jpg")
    finally:
        iter_file.seek(0)
        iter_file.write(str(done))
        
iter_file.close()