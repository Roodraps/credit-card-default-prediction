# credit-card-default-prediction

# Contributors
  ROODRA PRATAP SINGH PARIHAR

# web link for real time prediction of fraud/non-fraud customers
 
 https://credit-card-defaulter-prediction-service.onrender.com
 
   

![credit-card-fraud-detection_image](https://user-images.githubusercontent.com/113835698/218536166-a3340aac-b3b8-4df3-a1e1-3d02255621dc.jpg)


# High Level Design Document
https://docs.google.com/document/d/1gC_UJ2YchiQtsemO2ArzUTlBCiLhyfi9_lq7y5_ORDM/edit?usp=sharing


# Low Level Design Document
https://docs.google.com/document/d/167kbDDJKw4gXHzbumnr6mVNtaNK-QkujA_1gNwWRYjw/edit?usp=sharing


# Architecture Design
https://docs.google.com/document/d/1ZfD7LvjQwUEqq_2oI3NJYpFeCMtq3eAMvDMA2fuHfII/edit?usp=sharing





# Problem Statement
The goal of the project is to predict fraudulent credit card transations using machine learnings. it is pretty much important from the bank as well as customer point of view. Banks can not afford for clients' money to be stolen by scammers. Each fraud results in a loss for the bank since the bank is accountable for the fraudulent transactions.

# Dataset link
https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset

# Dataset information
This dataset contains information on default payments, demographic factors, credit data, history of payment, and bill statements
of credit card clients in Taiwan from April 2005 to September 2005.

# Dataset lookup view
 ![img1](https://user-images.githubusercontent.com/113835698/218663213-7d4ba745-b5b6-47e1-9fef-59f5eba21770.jpg)
 ![img2](https://user-images.githubusercontent.com/113835698/218663668-5875aabc-2dfd-40ee-844c-1f45684bcfd2.jpg)



# Modeling 
 In this project 4 different classification Algorithms were tasted
  1. Logistic Regression
  2. XGboost 
  3. Decision Tree
  4. Random Forest

# Short summary of Project Approach 

  In the dataset, there are 22.12 % fradulent and 77.88 % non fraudulent.
  
  For Reducing the skewness, There have been used power Transformation.

  For Balancing the dataset, It's been used Undersampling, Oversampling, SMOTE(Synthetic minority oversampling technique) in PROJECT APPROACHdifferent-different classification algorithms mentioned above.

  Tested every model with their calculation of Accuracy,Precision,Recall,F-1 score, Roc-Auc score, Sensitivity and Specificity.


  
  
# Choosing the best model
Over-sampling with XGBoost gave us best accuracy in the train and the test, with the better training and testing ROC score as well as pretty good sensitivity and specificity.

# Cost Benefit Analysis
Even though XGBoost , Decision tree and Random forest taking much higher computational power in comparison to the logistic regression but we have to go with them.

Because we are building the model for the financial case, Amount scam can be huge. so to get rid of these types of huge losses we have to build the accurate and precise model even though model take good amount of computational cost.

# Summary from the Business point of view
 We would need high precision for banks with lesser average transaction values because we only want to flag relevant transactions as fraudulent. We may add the human element to every transaction that is reported as fraudulent, calling the customer to confirm that the transaction actually took place. But it wiil be difficult, when accuracy is poor because the human component must be increased.
 



If the recall is low, i.e., it is unable to identify transactions that are flagged as non-fraudulent, this will affect banks with higher transaction values. so for the high transaction scam not to be happen, we need high recall.


After performing the lot of models, I saw that balanced data with Over-sampling technique, XGBoost model has very good accuracy, best ROC score and high Recall. Therefore we can go with the Oversampled XGBoost Model . That will reduce the scam till the most extreem. cases.

what we need --> 1. High Accuracy 2. High Recall 3. High Roc score





# To change the branch from master to main
''' git branch -M main '''

# Enviornment Setting Info
create a new enviornment
       ''' conda create -p venv python==3.7 -y'''

for activating conda enviornment
''' conda activate venv/ '''

for deactivating conda enviornment
''' conda deactivate '''



