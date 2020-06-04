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
count_enc = ce.CountEncoder()
count_encoded = count_enc.fit_transform(df[features])
data = baseline_data.join(count_encoded.add_suffix("_count"))

====================================================================================
#Target encoding replaces a categorical value with the average value of the target for that value of the feature. 
#For example, given the country value "CA", you'd calculate the average outcome for all the rows with country == 'CA', around 0.28. 
#This is often blended with the target probability over the entire dataset to reduce the variance of values with few occurences.

#This technique uses the targets to create new features. 
#So including the validation or test data in the target encodings would be a form of target leakage. 
#Instead, you should learn the target encodings from the training dataset only and apply it to the other datasets.

# Create the encoder itself

import category_encoders as ce
target_enc = ce.TargetEncoder(cols=features)
# Fit the encoder using the categorical features and target
target_enc.fit(train[features], train['target'])
train = train.join(target_enc.transform(train[features]).add_suffix('_target'))            

====================================================================================
#CatBoost Encoding
#Finally, we'll look at CatBoost encoding. 
#This is similar to target encoding in that it's based on the target probablity for a given value. 
#However with CatBoost, for each row, the target probability is calculated only from the rows before it. 

target_enc = ce.CatBoostEncoder(cols=features)
target_enc.fit(train[features], train['target'])
train = train.join(target_enc.transform(train[features]).add_suffix('_cb'))                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
