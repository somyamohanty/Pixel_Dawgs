__author__ = 'SATYANARAYANAREDDY'

import csv
files = ["satya.csv", "manish.csv", "shreya.csv", "nick.csv"]

def getTaggedImages():
    count = 0
    image_data = {}
    list_of_images_tagged = []
    for file in files:
        csvfile = open(file, 'r')
        csv_dict = csv.DictReader(csvfile)
        for row in csv_dict:
            if row['tag6']!= "NULL":
                image_data[row['imgid']] = row
                list_of_images_tagged.append(row['imgid'])
                count += 1

    print count,"images have been tagged in all"

    #some string processing to make a list of coordinates separated by a colon
    li = ['tag1c', 'tag2c', 'tag3c', 'tag4c', 'tag5c', 'tag6c', 'tag7c', 'tag8c', 'tag9c', 'tag10c']
    for id in list_of_images_tagged:
        for each in li:
            if image_data[id][each] != '':
                image_data[id][each] = image_data[id][each][:-1].split(",")

    #example usage - retrieving the tag6, and tag6c for all images

    return list_of_images_tagged, image_data