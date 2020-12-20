# -*- coding: utf-8 -*-
"""DMGa2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AsRpiTKbH0yKPzPom_O2PAXv6xZvGcIJ
"""

from google.colab import drive
drive.mount("/content/drive")

#imported required ensemble methods from the libraries
import pandas as pd
import numpy as np
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import BaggingClassifier
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from imblearn.under_sampling import RandomUnderSampler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import VotingRegressor
from sklearn.ensemble import BaggingRegressor
import xgboost as xgb
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split


#function for graph plots
def plot(X_over1, y_over1,X_test,y_test):
     #Taking “n_estimator” as a hyperparameter in GradientBoostingClassifier,the train and test accuracy graph is plotted
     m1=[100,200,300,400,500,600,700,800,900,1000] #different n_estimators value
     a1=np.empty(10)
     a2=np.empty(10)
     for i in range(10):
          clf1 = GradientBoostingClassifier(max_depth=6,n_estimators=m1[i])
          clf1 = clf1.fit(X_over1, y_over1)
          y1=clf1.predict(X_test)
          yp1=pd.DataFrame(y1)
          a1[i]=accuracy_score(y_test, yp1) #accuracy score
          y2=clf1.predict(X_over1)
          yp2=pd.DataFrame(y2)
          a2[i]=accuracy_score(y_over1, yp2)
     plt.plot(m1,a1,marker='o',color='tab:cyan')
     plt.plot(m1,a2,marker='o',color='tab:orange')
     one = mpatches.Patch(color='tab:cyan', label='Test Accuracy')
     two = mpatches.Patch(color='tab:orange', label='Train Accuracy')
     plt.legend(handles=[one,two])
     plt.title("Accuracy vs Hyperparameter n_estimators")
     plt.xlabel("n_estimators")
     plt.ylabel("Accuracy")
     plt.show()
     plt.close()

 #Taking “max_depth” as a hyperparameter in GradientBoostingClassifier, the train and test accuracy graph is plotted:
     m2=[1,2,5,6,7,8,9,10,15,20] #different max_depth value
     a3=np.empty(10)
     a4=np.empty(10)
     for i in range(10):
          clf1 = GradientBoostingClassifier(max_depth=m2[i],n_estimators=500,random_state=True)
          clf1 = clf1.fit(X_over1, y_over1)
          y3=clf1.predict(X_test)
          yp3=pd.DataFrame(y3)
          a3[i]=accuracy_score(y_test, yp3)
          y4=clf1.predict(X_over1)
          yp4=pd.DataFrame(y4)
          a4[i]=accuracy_score(y_over1, yp4)
     plt.plot(m2,a3,marker='o',color='tab:cyan')
     plt.plot(m2,a4,marker='o',color='tab:orange')
     one = mpatches.Patch(color='tab:cyan', label='Test Accuracy')
     two = mpatches.Patch(color='tab:orange', label='Train Accuracy')
     plt.legend(handles=[one,two])
     plt.title("Accuracy vs Hyperparameter Depth")
     plt.xlabel("Depth")
     plt.ylabel("Accuracy")
     plt.show()
     plt.close()

 #Taking “min_samples_split” as a hyperparameter in GradientBoostingClassifier, the train and test accuracy graph is plotted :
     m3=[2,3,4,5,6,7,8,9,10,12] #different min_samples_split
     a5=np.empty(10)
     a6=np.empty(10)
     for i in range(10):
          h=m3[i]
          clf1 = GradientBoostingClassifier(max_depth=6,n_estimators=500,random_state=True,min_samples_split=h)
          clf1 = clf1.fit(X_over1, y_over1)
          y5=clf1.predict(X_test)
          yp5=pd.DataFrame(y5)
          a5[i]=accuracy_score(y_test, yp5)
          y6=clf1.predict(X_over1)
          yp6=pd.DataFrame(y6)
          a6[i]=accuracy_score(y_over1, yp6)
     plt.plot(m3,a5,marker='o',color='tab:cyan')
     plt.plot(m3,a6,marker='o',color='tab:orange')
     one = mpatches.Patch(color='tab:cyan', label='Test Accuracy')
     two = mpatches.Patch(color='tab:orange', label='Train Accuracy')
     plt.legend(handles=[one,two])
     plt.title("Accuracy vs Hyperparameter min_samples_split")
     plt.xlabel("min_samples_split")
     plt.ylabel("Accuracy")
     plt.show()
     plt.close()

 #Taking “n_estimator” as a hyperparameter in BaggingClassifier, the train and test accuracy graph is plotted :
     m4=[100,200,300,400,500,600,700,800,900,1000] # different values for n_estimator
     a7=np.empty(10)
     a8=np.empty(10)
     for i in range(10):
          h=m4[i]
          clf1 = BaggingClassifier(random_state=True,bootstrap_features=True,n_estimators=h)
          clf1 = clf1.fit(X_over1, y_over1)
          y7=clf1.predict(X_test)
          yp7=pd.DataFrame(y7)
          a7[i]=accuracy_score(y_test, yp7)
          y8=clf1.predict(X_over1)
          yp8=pd.DataFrame(y8)
          a8[i]=accuracy_score(y_over1, yp8)
     plt.plot(m4,a7,marker='o',color='tab:cyan')
     plt.plot(m4,a8,marker='o',color='tab:orange')
     one = mpatches.Patch(color='tab:cyan', label='Test Accuracy')
     two = mpatches.Patch(color='tab:orange', label='Train Accuracy')
     plt.legend(handles=[one,two])
     plt.title("Accuracy vs Hyperparameter n_estimators")
     plt.xlabel("n_estimators")
     plt.ylabel("Accuracy")
     plt.show()
     plt.close()

 #Taking “max_depth” as a hyperparameter in XGBClassifier, the train and test accuracy graph is plotted
     n1=[1,2,5,6,7,8,9,10,15,20]  #different values for max_depth
     b1=np.empty(10)
     b2=np.empty(10)
     for i in range(10):
          clf1 = xgb.XGBClassifier(max_depth=n1[i],n_estimators=500)
          clf1 = clf1.fit(X_over1, y_over1)
          yn1=clf1.predict(X_test)
          ypn1=pd.DataFrame(yn1)
          b1[i]=roc_auc_score(y_test, ypn1) #taken roc_auc score for regressor
          yn2=clf1.predict(X_over1)
          ypn2=pd.DataFrame(yn2)
          b2[i]=roc_auc_score(y_over1, ypn2)
     plt.plot(n1,b1,marker='o',color='tab:cyan')
     plt.plot(n1,b2,marker='o',color='tab:orange')
     one = mpatches.Patch(color='tab:cyan', label='Test Accuracy')
     two = mpatches.Patch(color='tab:orange', label='Train Accuracy')
     plt.legend(handles=[one,two])
     plt.title("Accuracy vs Hyperparameter Depth")
     plt.xlabel("Depth")
     plt.ylabel("Accuracy")
     plt.show()
     plt.close()

 #Taking “max_depth” as a hyperparameter in GradientBoostingRegressor, the train and test accuracy graph is plotted :
     n2=[1,2,5,6,7,8,9,10,15,20] #different max_depth values
     b3=np.empty(10)
     b4=np.empty(10)
     for i in range(10):
          clf1 = GradientBoostingRegressor(max_depth=n2[i],n_estimators=500,random_state=True)
          clf1 = clf1.fit(X_over1, y_over1)
          yn3=clf1.predict(X_test)
          ypn3=pd.DataFrame(yn3)
          b3[i]=roc_auc_score(y_test, ypn3) #taken roc_auc score for regressor
          yn4=clf1.predict(X_over1)
          ypn4=pd.DataFrame(yn4)
          b4[i]=roc_auc_score(y_over1, ypn4)
     plt.plot(n2,b3,marker='o',color='tab:cyan')
     plt.plot(n2,b4,marker='o',color='tab:orange')
     one = mpatches.Patch(color='tab:cyan', label='Test Accuracy')
     two = mpatches.Patch(color='tab:orange', label='Train Accuracy')
     plt.legend(handles=[one,two])
     plt.title("Accuracy vs Hyperparameter Depth")
     plt.xlabel("Depth")
     plt.ylabel("Accuracy")
     plt.show()
     plt.close()



#Model 3: Used GradientBoostingClassifier,BaggingClassifier,VotingClassifier with different parameter and saved the prediction in csv file
def Model3(X_over, y_over,test):
     clf1 = GradientBoostingClassifier(max_depth=6,random_state=True,n_estimators=500)
     clf2 = BaggingClassifier(n_estimators=700,random_state=True,bootstrap_features=True)
     eclf2= VotingClassifier(estimators=[('lr', clf1), ('rf', clf2)])
     eclf2 = eclf2.fit(X_over, y_over)
     xt=test
     xt=xt.drop('id',axis=1)
     xt=xt.to_numpy()
     y=eclf2.predict(xt)
     yp=pd.DataFrame(y)
     yp.columns=['T']
     yp[['id']]=test['id']
     column_names = ["id", "T"]
     yp = yp.reindex(columns=column_names) #output like kaggle format csv
     yp.to_csv (r'/content/drive/My Drive/result3.csv', index = False, header=True) #for saving as csv in drive Name = "gbv.csv"

#Model 2: Used GradientBoostingClassifier,BaggingClassifier,XGBClassifier,VotingClassifier with different parameter and saved the prediction in csv file
def Model2(X_over, y_over,test):
     clf1 = GradientBoostingClassifier(max_depth=6,random_state=True,n_estimators=500,min_samples_leaf=10)
     clf2 = BaggingClassifier(n_estimators=700,random_state=True,bootstrap_features=True)
     clf3 = xgb.XGBClassifier(n_estimators=500,max_depth=10)
     eclf3= VotingClassifier(estimators=[('lr', clf1), ('rf', clf2),('xg',clf3)])
     eclf3 = eclf3.fit(X_over, y_over)
     xt=test
     xt=xt.drop('id',axis=1)
     xt=xt.to_numpy()
     y=eclf3.predict(xt)
     yp=pd.DataFrame(y)
     yp.columns=['T']
     yp[['id']]=test['id']
     column_names = ["id", "T"]
     yp = yp.reindex(columns=column_names) #output like kaggle format csv
     yp.to_csv (r'/content/drive/My Drive/result2.csv', index = False, header=True) #for saving as csv in drive Name= "gbxv.csv"

#Model 1: Used GradientBoostingRegressor,BaggingRegressor,XGBRegressor,VotingRegressor with different parameter and saved the prediction in csv file
def Model1(X_over, y_over,test):
     clf1 = GradientBoostingRegressor(max_depth=6,random_state=True,n_estimators=500)
     clf2 = BaggingRegressor(n_estimators=700,random_state=True,bootstrap_features=True)
     clf3 = xgb.XGBRegressor(n_estimators=500,max_depth=10)
     eclf1= VotingRegressor(estimators=[('lr', clf1), ('rf', clf2), ('xg',clf3)])
     eclf1 = eclf1.fit(X_over, y_over)
     xt=test
     xt=xt.drop('id',axis=1)
     xt=xt.to_numpy()
     y=eclf1.predict(xt)
     yp=pd.DataFrame(y)
     yp.columns=['T']
     yp['id']=test['id']
     column_names = ["id", "T"]
     yp = yp.reindex(columns=column_names) #output like kaggle format csv
     yp.to_csv (r'/content/drive/My Drive/result1.csv', index = False, header=True) #for saving as csv in drive Name= "xgi.csv"


#runner function for the models
def main(data,test):
     # pre-processing the dataset, dropped 'T' and split the dataset in X and y
     X = data
     xtest = test
     xtest = xtest.drop('id', axis=1)
     Y = X[['T']]  # split in x,y
     X = X.drop('T', axis=1)
     X = X.drop('id', axis=1)

     # plotting the Original Class Distribution before pre-processing
     count_classes = pd.value_counts(data['T'], sort=True)
     count_classes.plot(kind='bar', rot=0, color=['tab:cyan', 'tab:red'])
     plt.title("Original Class Distribution")
     plt.xlabel("Class")
     plt.ylabel("Frequency")
     plt.show()
     plt.close()

     # performing random-under sampling
     undersample = RandomUnderSampler(sampling_strategy='majority')
     X_over, y_over = undersample.fit_resample(X, Y)

     # plotting Sampled Class Distribution after pre-processing
     yo = pd.DataFrame(y_over)
     yo.columns = ['T']
     count_classes = pd.value_counts(yo['T'], sort=True)
     count_classes.plot(kind='bar', rot=0, color=['tab:cyan', 'tab:red'])
     plt.title("Sampled Class Distribution")
     plt.xlabel("Class")
     plt.ylabel("Frequency")
     plt.show()
     plt.close()

     #splitting test and train data for plotting the accuracy
     X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33)
     X_over1, y_over1 = undersample.fit_resample(X_train, y_train)
     plot(X_over1, y_over1, X_test, y_test)

     Model1(X_over, y_over, test)
     Model2(X_over, y_over, test)
     Model3(X_over, y_over, test)

# reading the dataset from the drive
data = pd.read_csv('/content/drive/My Drive/given_dataset.csv')
test = pd.read_csv('/content/drive/My Drive/to_predict.csv')
main(data,test)