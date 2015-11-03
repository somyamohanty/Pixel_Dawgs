import csv
import operator
fi = open("validTags.csv", "r")
dictionary = {}
for each in fi:
    tagslist = each.split(",")
    dictionary[tagslist[0]] = tagslist[1::]

imageslist = []
import os
for root, dirs, files in os.walk("segmented"):
    for file in files:

        if file.endswith(".jpg"):
            if not file.endswith("segmented.jpg"):
                imageslist.append(file.strip(".jpg"))

#print imageslist


csvfile = open("newValidTags.csv", "w")
fieldnames = ['ind', 'imgid', 'tag1','tag2', 'tag3','tag4', 'tag5', 'tag1c','tag2c', 'tag3c','tag4c', 'tag5c']


writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()

imagecounter = 1
for each_id in imageslist:
    d = {'ind': "", 'imgid': "",
     'tag1': "", 'tag2': "", 'tag3': "", 'tag4': "", 'tag5': "",
     'tag1c': "",'tag2c': "",'tag3c': "",'tag4c': "",'tag5c': ""}
    #get the list of tags associated with each image
    tags = dictionary[each_id]

    di = {}
    for tag in tags:
        pair = tag.split(":")
        di[pair[0]] = float(pair[1].strip("\n"))
    sorted_di = sorted(di.items(), key=operator.itemgetter(1), reverse=True)

    d.update({fieldnames[0]:imagecounter})
    d.update({fieldnames[1]:each_id})
    print d
    inde = 2
    for ea in sorted_di:
        if inde <= 6:
            d.update({fieldnames[inde]:ea[0]})
            inde+=1
    writer.writerow(d)
    imagecounter+=1