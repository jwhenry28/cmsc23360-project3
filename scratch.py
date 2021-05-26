import pickle
import json
import pprint
import random

# with open("results/clean", "r") as f:
#     data = json.load(f)

#     for i in range(8400):
#         print(len(data["feature"][i]))

with open("results/raw_data", "rb") as infile:
    data = pickle.load(infile)

with open("results/notated_clean", "w") as outfile:
    json.dump(data, outfile)


# def chunkIt(seq, num):
#     avg = len(seq) / float(num)
#     out = []
#     last = 0.0
#     while last < len(seq):
#         out.append(seq[int(last):int(last + avg)])
#         last += avg
#     return out

# conc = [random.randint(0, 100) for i in range(1000)]
# altconc = [sum(x) for x in chunkIt(conc, 70)]

# print("len conc:", len(conc))
# print("len altconc:", len(altconc))

"""
NOTES

Class - website classification value, first item in 'label' tuple

Instance - nth time that website was visited, second item in 'label' tuple





"""