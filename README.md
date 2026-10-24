# Spam Email Classification Using Machine Learning

##  Project Overview

This project implements a basic spam email classifier using Machine Learning in Python. It uses the **Multinomial Naive Bayes algorithm** to classify email messages into two categories: **Spam** and **Not Spam**.

##  Objectives

* Build a basic email classification model using Machine Learning.
* Convert text emails into numerical features using `CountVectorizer`.
* Train the model using labeled email data.
* Predict labels for new email messages.
* Compare actual labels with predicted labels on test data.

##  Technologies Used

* **Language:** Python
* **Library:** Scikit-learn
* **Feature Extraction:** CountVectorizer
* **ML Algorithm:** Multinomial Naive Bayes

##  How It Works

1. **Dataset Preparation:** Prepare 8 sample emails with their corresponding labels.
2. **Data Splitting:** Split the dataset into 75% training data and 25% testing data.
3. **Text Vectorization:** Convert email text into numerical features using `CountVectorizer`.
4. **Model Training:** Train the Multinomial Naive Bayes classifier on the training emails and labels.
5. **Prediction:** Predict whether test emails are Spam or Not Spam.
6. **Result Comparison:** Display each test email's actual label alongside the predicted label.

##  Project Metrics

* **Total Samples:** 8 labeled emails
* **Training Samples:** 6
* **Testing Samples:** 2
* **Classification Categories:** 2 (Spam and Not Spam)
* **ML Algorithm:** Multinomial Naive Bayes

*Note: This is a small educational project. Model accuracy has not been calculated, and the dataset is not suitable for real-world spam detection.*

##  How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/spam-email-classification-naive-bayes.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Open the Project Folder

```bash
cd spam-email-classification-naive-bayes
```

### 3. Install the Required Library

```bash
pip install scikit-learn
```

### 4. Run the Python Script

```bash
python spam_classifier.py
```

Ensure your Python script is named `spam_classifier.py`, or replace the filename with your actual script name.

##  Future Improvements

* Use a larger, realistic email dataset.
* Evaluate the model using accuracy, precision, recall, and F1-score.
* Test the classifier on more unseen email messages.

##  Author

**ANMOL BHONSLE**

Cybersecurity Enthusiast | Machine Learning Learner
