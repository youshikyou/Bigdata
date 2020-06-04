from sklearn.preprocessing import LabelEncoder

# Method1
encoder = LabelEncoder()
encoded = df[features].apply(encoder.fit_transform)  # Apply the label encoder to each column
df = df[[otherfeatures]].join(encoded)

# Method2
label_encoder = LabelEncoder()
for feature in features:
  clicks[feature + '_labels'] = label_encoder.fit_transform(clicks[feature])
