# credit-card-default-prection



# Problem Statement
The goal of the project is to predict fraudulent credit card transations using machine learnings. it is pretty much important from the bank as well as customer point of view.Banks cannot afford for clients' money to be stolen by scammers. Each fraud results in a loss for the bank since the bank is accountable for the fraudulent transactions.

# Dataset link
https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset

# Dataset information
This dataset contains information on default payments, demographic factors, credit data, history of payment, and bill statements
of credit card clients in Taiwan from April 2005 to September 2005.

# Choosing the best model
Over-sampling with XGBoost gave us best accuracy in the train and the test, with the better training and testing ROC score as well as pretty good sensitivity and specificity.

# Cost Benefit Analysis
Even though XGBoost , Decision tree and Random forest taking much higher computational power in comparison to the logistic regression but we have to go with them.

Because we are building the model for the financial case, Ammount scam can be huge. so to get rid of these types of huge losses we have to build the accurate and precise model even though model take good ammount of computational cost.

# Summary For the Business
High Accuracy : We would need high precision for banks with lesser average transaction values because we only want to flag relevant transactions as fraudulent. We may add the human element to every transaction that is reported as fraudulent, calling the customer to confirm that the transaction actually took place.

But it wiil be difficult, when accuracy is poor because the human component must be increased.

If the recall is low, i.e., it is unable to identify transactions that are flagged as non-fraudulent, this will affect banks with higher transaction values. so for the high transaction scam not to be happen, we need high recall.

After performing the lot of models, I saw that balanced data with Over-sampling technique, XGBoost model has very good accuracy, best ROC score and high Recall as well as High accuracy. Therefore we can go with the XGBoost model. That will reduce the scam till the most extreem cases.

what we need --> 1. High Accuracy 2. High Recall 3. High Roc score




# To change the branch from master to main
git branch -M main

# Enviornment Setting Info
create a new enviornment
''' conda create -p venv python==3.7 -y'''

for activating conda enviornment
''' conda activate venv/ '''

for deactivating conda enviornment
''' conda deactivate '''