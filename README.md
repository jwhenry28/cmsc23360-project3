# cmsc23360-project3
Team repo for Advanced Networks project 3

## extractor.py
This is a script provided to us to extract features from the raw data. In the context of this project, it should be run as follows:
```
python3 extractor.py path/to/raw_data
```
This will create `results/raw_data` as output

## package_data.py
This script takes the ouput of `extractor.py`, parses it into and Pandas dataframe, and outputs it as a CSV which can be used by the machine learning script.
This script requires the `pandas` and `pickle` library, as well as Python 3. It can be run as follows:
```
python3 package_data.py
```
This will create `clean_data.csv` as output.

## train_ml.py
This script trains a decision tree using the CSV obtained from `package_data.py`. It will output a CSV with all the features and the corresponding median accuracy. This script requires the `pandas`, `numpy`, and `sklearn` libraries as well as Python 3. It can be run as follows:
```
python3 train_ml.py
```
This will create `ml_ranks.csv` as output.

## pivot_data.R
An R script used to pivot and rank the CSV created by the `train_ml.py` script. It should be run on R 3.6.1. This is not necessary to run, but will pivot the data into a friendlier format for further analysis including sorting. 

This will create `ml_ranks_cleaned.csv` as output.
 
## Instructions
To run this project, simply run the scripts above sequentially as follows:
```
python3 extractor.py path/to/raw_data
python3 package_data.py
python3 train_ml.py
(optional) Rscript pivot_data.R
```

Or run pivot_data.R in RStudio
