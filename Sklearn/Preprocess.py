from sklearn.preprocessing import LabelEncoder

# Method1
encoder = LabelEncoder()
encoded = df[features].apply(encoder.fit_transform)  # Apply the label encoder to each column
df = df[[otherfeatures]].join(encoded)

# Method2
label_encoder = LabelEncoder()
for feature in features:
  clicks[feature + '_labels'] = label_encoder.fit_transform(clicks[feature])

  
  
  
from sklearn.preprocessing import OneHotEncoder

myOHEncoder = OneHotEncoder(sparse=False,handle_unknown='ignore') # sparse=True will be a matrix.
OH_cols_train = pd.DataFrame(myOHEncoder.fit_transform(X_train['feature list']))
OH_cols_valid = pd.DataFrame(myOHEncoder.transform(X_valid['feature_list']))
# need index again
OH_cols_train.index = X_train.index
OH_cols_valid.index = X_valid.index
