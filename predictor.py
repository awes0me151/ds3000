import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

#Import the data
review_data_df = pd.read_csv('review_data.csv')

#Split into features and target for train-test split
features = review_data_df['user_review']
target = review_data_df['user_suggestion']

X_train, X_test, y_train, y_test = train_test_split(features, target, random_state=3000)


#Vectorize the training data
tfidf_vect = TfidfVectorizer(stop_words= "english", ngram_range = (1,2), min_df=2).fit(X_train)

X_train_tfidf_vectorized = tfidf_vect.transform(X_train)
X_test_tfidf_vectorized = tfidf_vect.transform(X_test)


#Build and train the model
log_tfidf = LogisticRegression(max_iter=1000).fit(X= X_train_tfidf_vectorized, y=y_train)

#Using the fitted model, we can make predictions using it
def pred_sentiment(comment):
    comment = [comment]
    comment_feature = tfidf_vect.transform(comment)
    sentiment = log_tfidf.predict(comment_feature)

    if sentiment == 1:
        return "yes"
    else:
        return "no"

#Allow user to test out the model by inputting their own "reviews"
print("Welcome to my sentiment analysis predictor. If you have not checked out my notebook, feel free to do so!\n")
print("The Jupyter Notebook explores various models and vectorizers to predict the sentiment of game reviews.\n")
print("This python file allows you to input a \"review\" and using Logistic Regression and a Tf-idf vectorizer, tries to guess the sentiment of that review.\n")

accuracy = 0
correct = 0
total = 0

while True:
    choice = input("Would you like to continue? (Yes/No) ")
    if choice.strip().lower() == 'yes':
        print("Current Accuracy: " + str(accuracy))
        review = input("Type a review here: ")
        if review != "":
            prediction = pred_sentiment(review)
        else:
            print("That was an invalid input. Please enter a non-empty string.")
            review = input("Type a review here: ")
            if review != "":
                prediction = pred_sentiment(review)
            else:
                exit("Exitted: Cannot predict with an empty string! Final accuracy: " + str(accuracy) + " percent.")
        user_sentiment = input("Was this review recommending of the game? (Yes/No) ")
        if user_sentiment.strip().lower() == "yes" or user_sentiment.strip().lower() == "no":
            if user_sentiment.strip().lower() == prediction:
                correct += 1
                total +=1
                accuracy = (correct / total) * 100
                print("The model guessed correctly! Your current accuracy is " + str(accuracy))
            else:
                total +=1
                accuracy = (correct / total) * 100
                print("The model guessed incorrectly! Your current accuracy is " + str(accuracy))
        else:
            print("That was an invalid input. Please type \"yes\" or \"no\".")
            user_sentiment = input("Was this review recommending of the game? (Yes/No) ")
            if user_sentiment.strip().lower() == "yes" or user_sentiment.strip().lower() == "no":
                if user_sentiment.strip().lower() == prediction:
                    correct += 1
                    total +=1
                    accuracy = (correct / total) * 100
                    print("The model guessed correctly! Your current accuracy is " + str(accuracy))
                else:
                    total +=1
                    accuracy = (correct / total) * 100
                    print("The model guessed incorrectly! Your current accuracy is " + str(accuracy))
            else:
                exit("Exitted: Invalid input. Final accuracy: " + str(accuracy) + " percent.")
    else:
        exit("Congrats! The model finished this experiment with " + str(accuracy) + " percent accuracy.")