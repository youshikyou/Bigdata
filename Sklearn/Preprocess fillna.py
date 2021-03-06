#Two methods to fill null value with mean value

  from sklearn.impute import SimpleImputer
  my_imputer = SimpleImputer()
  imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
  imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))
  
  """
  To center the data (make it have zero mean and unit standard error), you subtract the mean and then divide the result 
  by the standard deviation.x′=(x−μ)/σ
  You do that on the training set of data. But then you have to apply the same transformation to your testing set
  (e.g. in cross-validation), or to newly obtained examples before forecast. But you have to use the same 
  two parameters μ and σ (values) that you used for centering the training set.

  Hence, every sklearn's transform's fit() just calculates the parameters (e.g. μ and σ in case of StandardScaler)
  and saves them as an internal objects state. Afterwards, you can call its transform() method to apply the transformation to
  a particular set of examples.

  fit_transform() joins these two steps and is used for the initial fitting of parameters on the training set x, 
  but it also returns a transformed x′. Internally, it just calls first fit() and then transform() on the same data.
  """
  
  # Fill in the lines below: imputation removed column names; put them back
  imputed_X_train.columns = X_train.columns
  
  import pandas as pd
  imputed_X_train = X_train.fillna(value = X_train.mean())
