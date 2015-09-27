__author__ = 'SATYANARAYANAREDDY'

tags_dictionary = {}
fi = open("validTags.csv")
for each in fi:
    sep_values = each.split(",")
    image_id = sep_values[0]
    for i in range(1, len(sep_values)):
        tag = sep_values[i].split(":")[0]
        if tag not in tags_dictionary.keys():
            tags_dictionary[tag] = []
        tags_dictionary[tag].append(image_id)

strinlist = []
for each in tags_dictionary:
    strin = each
    for id in tags_dictionary[each]:
        if id != tags_dictionary[each][-1]:
            strin = strin + "," + id
        else:
            strin = strin+","+id+"\n"
    strinlist.append(strin)

outfil = open("Tagsmap.csv", "w")
strinlist.sort()
for st in strinlist:
    outfil.write(st)