import pandas as pd
import time
import sys
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.feature_selection import SelectKBest, f_classif
from pprint import pprint

# Load dataset
fingerprint_data = pd.read_csv('clean_data.csv')

# There are 6 websites that didn't have enough parsed instances to train properly
# Remove them
bad_sites = [41, 30, 39, 36, 65, 76]
for site in bad_sites:
    fingerprint_data = fingerprint_data[fingerprint_data['siteClass'] != site]

# Extract results column and remove irrelevant features
y = fingerprint_data.pop('siteClass')
fingerprint_data.pop('siteInstance')

fs = SelectKBest(score_func=f_classif, k=5)
X_new = fs.fit_transform(fingerprint_data, y)
X_filter = fs.get_support()

print(fingerprint_data.columns[X_filter])















sys.exit(0)


# Initialize accuracy dictionary
accuracies = {}
for col in fingerprint_data.columns:
    accuracies[col] = -1

# Loop through each feature
print("[*] Considering", len(fingerprint_data.columns), "columns.")
for feature in fingerprint_data.columns:
    tmp_df = fingerprint_data.loc[:, fingerprint_data.columns != feature]

    # Used: https://www.geeksforgeeks.org/random-forest-classifier-using-scikit-learn/
    # Split data into testing and training
    X_train, X_test, y_train, y_test = train_test_split(tmp_df, y, test_size=0.10, stratify=y, random_state=222)

    # Create classifier and train
    # n_estimators chosen from this article: https://medium.com/all-things-ai/in-depth-parameter-tuning-for-random-forest-d67bb7e920d
    clf = RandomForestClassifier(n_estimators=30)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    # Score accuracy
    accuracy = metrics.accuracy_score(y_test, y_pred)
    print("[*] --", feature, "--")
    print("[*] ACCURACY:", accuracy)
    # print("[*] Took", time.time() - start_time, "seconds.")
    print("")

    # Store results
    accuracies[feature] = accuracy

print("")

pprint(accuracies)