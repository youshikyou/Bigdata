from sklearn.preprocessing import LabelEncoder

# Method1
encoder = LabelEncoder()
encoded = df[features].apply(encoder.fit_transform)  # Apply the label encoder to each column
df = df[[otherfeatures]].join(encoded)

# Method2
label_encoder = LabelEncoder()
for feature in features:
  clicks[feature + '_labels'] = label_encoder.fit_transform(clicks[feature]

======================================================================================                                                     
 
from sklearn.preprocessing import OneHotEncoder

myOHEncoder = OneHotEncoder(sparse=False,handle_unknown='ignore') # sparse=True will be a matrix.
OH_cols_train = pd.DataFrame(myOHEncoder.fit_transform(X_train['feature list']))
OH_cols_valid = pd.DataFrame(myOHEncoder.transform(X_valid['feature_list']))
# One-hot encoding removed index; put it back
OH_cols_train.index = X_train.index
OH_cols_valid.index = X_valid.index

=======================================================================================
#Count Encoding
#Count encoding replaces each categorical value with the number of times it appears in the dataset. 
#For example, if the value "GB" occured 10 times in the country feature, then each "GB" would be replaced with the number 10.
#We'll use the categorical-encodings package to get this encoding. The encoder itself is available as CountEncoder. 
#This encoder and the others in categorical-encodings work like scikit-learn transformers with .fit and .transform methods
import category_encoders as ce
