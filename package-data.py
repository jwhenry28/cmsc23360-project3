import pandas as pd
import pickle
import pprint

with open("results/raw_data", "rb") as infile:
    data = pickle.load(infile)

cleanData = {"siteClass": [], "siteInstance": [],
             "maxTimeIn": [], "maxTimeOut": [], "maxTimeTotal": [],
             "avgTimeIn": [], "avgTimeOut": [], "avgTimeTotal": [],
             "stdTimeIn": [], "stdTimeOut": [], "stdTimeTotal": [],
             "per75TimeIn": [], "per75TimeOut": [], "per75TimeTotal": [],
             "per25In": [], "per50In": [], "per75In": [], "per100In": [],
             "per25Out": [], "per50Out": [], "per75Out": [], "per100Out": [],
             "per25Total": [], "per50Total": [], "per75Total": [], "per100Total": [],
             "packCountIn": [], "packCountOut": [], "packCountTotal": [],
             "first30In": [], "first30Out": [], "last30In": [], "last30Out": [],
             "stdConc": [], "avgConc": [], "avgPerSec": [], "stdPerSec": [],
             "avgOrderIn": [], "avgOrderOut": [], "stdOrderIn": [], "stdOrderOut": [],
             "medConc": [], "medPerSec": [], "minPerSec": [], "maxPerSec": [],
             "maxConc": [], "perIn": [], "perOut": []} #key is colum, value empty array

for features, labels in zip(data["feature"], data["label"]):
    i = 0
    for key in cleanData.keys():
        if key == "siteClass":
            cleanData["siteClass"].append(labels[0])
        elif key == "siteInstance":
            cleanData["siteInstance"].append(labels[1])
        else:
            cleanData[key].append(features[i])
            i += 1

    print(str(cleanData["siteClass"][-1]) + "," + str(cleanData["siteInstance"][-1]))

pprint.pprint(cleanData)

# turn this into a pandas frame
# run ML on it
