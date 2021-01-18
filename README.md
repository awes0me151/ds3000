# Sentiment Analysis in Video Game Reviews

Sentiment analysis is a field of machine learning that is extremely intriguing to me. The ability to convert words, no matter how simple or complex, to numerical data is truly amazing. In my project, I conducted sentiment analysis on a variety of video game reviews in order to determine whether a video game was recommended or not.

### Why is this important?

User ratings, for instance, on a 1 to 5 scale, can generally determine how good or bad a video game is. However, analyzing text can illustrate specific terms or phrases linked to a video game's rating. For example, the words "beautiful", "visual", and "breathtaking" could be associated with positive reviews, and developers can infer that their game is highly praised for its graphics, and may advertise this aspect of the game more. On the other hand, if words like "clunky", "awkward", and "movement" were associated with negative reviews, developers would assume that their game struggles with its controls, and should be addressed in an update. Without text, we could not gain this insight at all. 

Personally, I love reading video game reviews. Not only does it allow me to make an informed decision whether I should buy a game or not, I can also compare my experiences with others if I already have a certain game. My vocabulary and syntax may differ from another user, however we both attempt to express our ideas about the same video game. The fact that sentiment analysis can pick up these nuances and predict our feelings -whether they're the same or different- about a specific game is interesting to me. 

### What's in this project?

This project builds off the topics covered in my Foundations of Data Science class. Here are a list of things encapsulated in my project:

1. Data Wrangling
    * Merging DataFrames
    * Dropping unnecessary columns
    * Cleaning text input
2. Data Exploration
    * GroupBy of DataFrames
    * Plotly Express Bar Graphs
3. Model Construction
    * Count and Tf-idf Vectorizers
    * Logistic Regression, Multinomial Naive Bayes, Random Forest Classifier
4. Model Evaluation
    * Classification Accuracy
    * F1 Score
    * Confusion Matrix
    * Hyperparameter Tuning
        * GridSearch and RandomSearch
5. Summary and Discussion
    * Comparing performances
    * Next steps and possible improvements

### Necessary libraries

I would not be able to complete this project without the help of many necessary libraries. Here are some libraries you must install to run the notebook and python file for yourself.

- [ ] pandas
- [ ] sklearn
- [ ] cleantext
- [ ] plotly.express

[Link to first dataset](https://www.kaggle.com/piyushagni5/sentiment-analysis-for-steam-reviews?select=train.csv)
