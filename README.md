# News_article_classification_nlp
- Problem statement link-[https://drive.google.com/file/d/1XbIkKuyUifx4BQ7IWpGYgCoNkm8yrIA-/view]
- Click Here to view app-[https://newsarticleclassificationnlp-oajz5lfa7oaxzr7kfofezl.streamlit.app/]
### Project Overview
- Data or Articles from CNN News website covering various topics such as 'Politics','Economics','Sports' and 'Climate' were scraped using Beautiful Soup and Python.
- The data was cleaned of tags,punctuation marks,converted to lowercase,removed of stopwords,performed lemmatization using the NLTK,Wordcloud packages.
- Then the data was preprocessed using Countvectorizer from scikit learn package.
- Then various classification madels were trained on the data to predict to which category each article belonged to.
  - - ## Classification metrics score Table on the test set:
|    Model             |  Accuracy          |  Precision        | Recall             |  F1-score        |
| :------------------- | -----------------  |-----------------: | -----------------  |-----------------: |
| Logistic Regression  |      0.944         |0.944              | 0.944              |0.944              |
| RandomForest         |      0.953         |0.953              | 0.953              |0.953              |
|Multinomial Naive Bayes|0.929              |0.929              | 0.929              |0.929             |
|Support Vector Classifer|0.933             |0.933              | 0.933              |0.933              |
|Decision Tree Classifier|0.865             |0.865              | 0.865              |0.865              |
|Gaussian Naive Bayes  |0.746               |0.746              | 0.746              |0.746              |
- I chose randomforest as the best model and saved it in a pickle file named **nlp_news_saved_steps_classifier.pkl**
- Created **nlp_app.py** file where I used the saved model and streamlit to create an user friendly application and deployed on streamlit cloud.
