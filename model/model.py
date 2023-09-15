import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn import metrics
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def read_datasets():
    """ Reads users profile from csv files """
    genuine_users = pd.read_csv("users.csv")
    fake_users = pd.read_csv("fusers.csv")
    # print genuine_users.columns
    # print genuine_users.describe()
    # print fake_users.describe()
    x = pd.concat([genuine_users, fake_users])
    y = len(fake_users)*[0] + len(genuine_users)*[1]
    return x, y


def extract_features(x):
    feature_columns_to_use = ['profile pic',
                              'name==username',
                              'description length',
                              'external URL',
                              'private',
                              '#posts',
                              '#followers', '#follows']
    x = x.loc[:, feature_columns_to_use]
    return x

# def plot_confusion_matrix(cm, title='Confusion matrix', cmap=plt.cm.Blues):
#     target_names=['Fake','Genuine']
#     plt.imshow(cm, interpolation='nearest', cmap=cmap)
#     plt.title(title)
#     plt.colorbar()
#     tick_marks = np.arange(len(target_names))
#     plt.xticks(tick_marks, target_names, rotation=45)
#     plt.yticks(tick_marks, target_names)
#     plt.tight_layout()
#     plt.ylabel('True label')
#     plt.xlabel('Predicted label')

# def plot_roc_curve(y_test, y_pred):
#     false_positive_rate, true_positive_rate, thresholds = sklearn.metrics.roc_curve(y_test, y_pred)

#     print("False Positive rate: ",false_positive_rate)
#     print("True Positive rate: ",true_positive_rate)

#     roc_auc = sklearn.metrics.auc(false_positive_rate, true_positive_rate)

#     plt.title('Receiver Operating Characteristic')
#     plt.plot(false_positive_rate, true_positive_rate, 'b', label='AUC = %0.2f'% roc_auc)
#     plt.legend(loc='lower right')
#     plt.plot([0,1],[0,1],'r--')
#     plt.xlim([-0.1,1.2])
#     plt.ylim([-0.1,1.2])
#     plt.ylabel('True Positive Rate')
#     plt.xlabel('False Positive Rate')
#     plt.show()


def setupModel():
    global sc, trained_model

    x, y = read_datasets()

    x.head()
    x = extract_features(x)

    # print(x.columns)
    # print(x.describe())
    X_train, X_test, y_train, y_test = train_test_split(x,
                                                        y,
                                                        test_size=0.20,
                                                        random_state=44)

    # print(X_train.iloc[10])

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    clf = RandomForestClassifier(n_estimators=40, oob_score=True)
    trained_model = clf.fit(X_train, y_train)
    # print("model stats: ",clf)
    # Predict
    # y_pred = clf.predict(X_test)
    # print('Classification Accuracy on Train dataset: ' ,sklearn.metrics.accuracy_score(y_train, trained_model.predict(X_train)))
    # print('Classification Accuracy on Test dataset: ' ,sklearn.metrics.accuracy_score(y_test, y_pred))


def predict(input):
    column_names = ['profile pic',
                    'name==username', 'description length', 'external URL',
                    'private', '#posts', '#followers', '#follows']
    # fake = [0, 0, 0, 0, 0, 0, 9, 0]
    # real = [1, 0, 0, 0, 1, 5, 866, 953]

    # input = fake

    X_test_custom = pd.DataFrame([input], columns=column_names)
    # print(X_test_custom)
    X_test_custom = sc.transform(X_test_custom)

    y_pred_custom = trained_model.predict(X_test_custom)
    # print(y_pred_custom)
    return y_pred_custom[0]


# setupModel()
# print(predict())
