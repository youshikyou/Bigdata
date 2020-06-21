#kNN regression

from sklearn.neighbors import KNeighborsRegressor
KNeighborsRegressor(n_neighbors=k)


#decision tree
  from sklearn.tree import DecisionTreeClassifier
  model = DecisionTreeClassifier()

#SVM
  from sklearn.svm import SVC
  model = SVC()

#Naive Bayes
  from sklearn.naive_bayes import GaussianNB
  model = GaussianNB()

#KNN
  from sklearn.neighbors import KNeighborsClassifier
  model = KNeighborsClassifier()  

#K means unsupervisor
  from sklearn.cluster import KMeans
  model = KMeans()  

# Random Forest
  from sklearn.ensemble import RandomForestClassifier
  model = RandomForestClassifier()

# Principal Component Analysis (PCA)

  from sklearn.decomposition import PCA
  from sklearn.linear_model import LinearRegression
  
  model = LinearRegression()
  model.fit(train_x,train_y)
  
  model_pca = PCA(n_components=12)
  new_train = model_pca.fit_transform(train_x)
  new_test  = model_pca.fit_transform(test_x)
  # create object of model
  model_new = LinearRegression()
  # fit the model with the training data
  model_new.fit(new_train,train_y)

#Gradient Boosting Algorithms
from sklearn.ensemble import GradientBoostingClassifier
model = GradientBoostingClassifier(n_estimators=100,max_depth=5)
model.fit(train_x,train_y)












