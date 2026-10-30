
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# 1. Training dataset
X_train = [
    "Win money now",
    "Claim your free prize",
    "Meeting is scheduled for tomorrow",
    "Please find the project report",
    "Congratulations you won a cash prize",
    "Click here to claim your reward",
    "Team meeting is scheduled for Monday",
    "Please review the attached document"
]

# 2. Correct labels
y_train = [
    "Spam",
    "Spam",
    "Not Spam",
    "Not Spam",
    "Spam",
    "Spam",
    "Not Spam",
    "Not Spam"
]

# 3. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    emails,
    labels,
    test_size=0.25,
    random_state=42,
    stratify=labels
)

# 4. Create the machine learning model
model = make_pipeline(
    CountVectorizer(),
    MultinomialNB()
)

# 5. Train the model
model.fit(X_train, y_train)

# 6. Predict labels for the test emails
predictions = model.predict(X_test)

# 7. Display actual and predicted labels
for email, actual, predicted in zip(X_test, y_test, predictions):
    print("Email:", email)
    print("Actual label:", actual)
    print("Predicted label:", predicted)
    print()
```
