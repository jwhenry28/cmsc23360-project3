import pickle
import json
import pprint

# with open("results/clean", "r") as f:
#     data = json.load(f)

#     for i in range(8400):
#         print(len(data["feature"][i]))

with open("results/raw_data", "rb") as infile:
    data = pickle.load(infile)

with open("results/clean", "w") as outfile:
    json.dump(data, outfile)

"""
NOTES

Class - website classification value, first item in 'label' tuple

Instance - nth time that website was visited, second item in 'label' tuple





"""