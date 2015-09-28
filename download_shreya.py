import urllib, urllib2

def get_redirected_url(url):
    try:
        opener = urllib2.build_opener(urllib2.HTTPRedirectHandler)
        request = opener.open(url)
    except:
        return "https://s.yimg.com/pw/images/en-us/photo_unavailable.png"
    return request.url

fi = open("trainingset/yfcc100m_dataset-2", "r")


iter_file = open("download_tracker_shreya.txt", "r")

try:
    done = int(iter_file.readline())
except ValueError:
    done = 0

iter_file = open("download_tracker_shreya.txt", "w")

for i in range(done):
    next(fi)

for i in range(100000):
    done += 1
    img_data = next(fi)
    data = img_data.split("\t")
    id, url, isvideo = data[0], data[14], int(data[22].strip("\n")) == 1
    try:
        if (get_redirected_url(url) != "https://s.yimg.com/pw/images/en-us/photo_unavailable.png") and (isvideo is False):
            urllib.urlretrieve(url, "sampleimages/"+str(id)+".jpg")
    finally:
        iter_file.seek(0)
        iter_file.write(str(done))

iter_file.close()