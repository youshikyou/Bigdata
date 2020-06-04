Univariate Feature Selection
The simplest and fastest methods are based on univariate statistical tests. 
For each feature, measure how strongly the target depends on the feature using a statistical test like  χ2  or ANOVA.

From the scikit-learn feature selection module, feature_selection.SelectKBest returns the K best features given some scoring function. 
For our classification problem, the module provides three different scoring functions:  χ2 , ANOVA F-value, and the mutual information
score. The F-value measures the linear dependency between the feature variable and the target.
This means the score might underestimate the relation between a feature and the target if the relationship is nonlinear. 
The mutual information score is nonparametric and so can capture nonlinear relationships.

from sklearn.feature_selection import SelectKBest, f_classif
feature_cols = baseline_data.columns.drop('outcome')
train, valid, _ = get_data_splits(baseline_data)
# Keep 5 features
selector = SelectKBest(f_classif, k=5)
X_new = selector.fit_transform(train[feature_cols], train['outcome'])
# Get back the features we've kept, zero out all other features
selected_features = pd.DataFrame(selector.inverse_transform(X_new), index=train.index, columns=feature_cols)
# Dropped columns have values of all 0s, so var is 0, drop them
selected_columns = selected_features.columns[selected_features.var() != 0]

=================================================================================
L1 regularization
Univariate methods consider only one feature at a time when making a selection decision.
Instead, we can make our selection using all of the features by including them in a linear model with L1 regularization. 
This type of regularization (sometimes called Lasso) penalizes the absolute magnitude of the coefficients, 
as compared to L2 (Ridge) regression which penalizes the square of the coefficients.
As the strength of regularization is increased, features which are less important for predicting the target are set to 0. 
This allows us to perform feature selection by adjusting the regularization parameter. We choose the parameter 
by finding the best performance on a hold-out set, or decide ahead of time how many features to keep.


from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectFromModel

train, valid, _ = get_data_splits(baseline_data)
X, y = train[train.columns.drop("outcome")], train['outcome']
# Set the regularization parameter C=1
logistic = LogisticRegression(C=1, penalty="l1", random_state=7).fit(X, y)
model = SelectFromModel(logistic, prefit=True)
X_new = model.transform(X)
# Get back the kept features as a DataFrame with dropped columns as all 0s
selected_features = pd.DataFrame(model.inverse_transform(X_new), index=X.index,columns=X.columns)
# Dropped columns have values of all 0s, keep other columns 
selected_columns = selected_features.columns[selected_features.var() != 0]

