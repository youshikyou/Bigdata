from sklearn.model_selection import train_test_split

# Break off validation set from training data
X_train, X_valid, y_train, y_valid = train_test_split(X, y,train_size=0.8, test_size=0.2,random_state=0)

================================================================
# manually split the data into train, test, valid 

def get_data_splits(dataframe, valid_fraction=0.1):
    valid_size = int(len(dataframe) * valid_fraction)
    train = dataframe[:-valid_size * 2]
    # valid size == test size, last two sections of the data
    valid = dataframe[-valid_size * 2:-valid_size]
    test = dataframe[-valid_size:]

    
=================================================================
#RandomizedSearchCV/GridSearchCV are used to find the best hyperparameter combination. 
#https://towardsdatascience.com/hyperparameter-tuning-the-random-forest-in-python-using-scikit-learn-28d2aa77dd74
