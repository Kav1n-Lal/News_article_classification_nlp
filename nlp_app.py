import pickle
import streamlit as st 

import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('omw-1.4')
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
nltk.download('punkt')

def main():
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;"> News Article Classification ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
  

    with open('nlp_news_saved_steps_classifier.pkl','rb') as file:
        data=pickle.load(file)
        
    cv=data['count_vectorizer']
    classifier=data['model']

    form = st.form("form1")
    st.write('Copy And Paste Article Inside The Box')
    z=form.text_area('Able to classify -"politics","sports","economics" and "climate" related articles')
    ok=form.form_submit_button("classify")
    
    if ok:
        #removing newline from the input
        remove_newline=(z[1:-1].replace('\\n      ','').replace('\\n  ','').replace('\\n',''))

        #removing special_characters from the input
        def special_char(text):
            reviews = ''
            for x in text:
                if x.isalnum():
                    reviews = reviews + x
                else:
                    reviews = reviews + ' '
            return reviews

        remove_special_chars=special_char(remove_newline)

        #converting the input to lowercase
        def convert_lower(text):
            return text.lower()

        remove_lowercase=convert_lower(remove_special_chars)

        #removing stopwords from the input 
        def remove_stopwords(text):
            stop_words = set(stopwords.words('english'))
            words = word_tokenize(text)
            return [x for x in words if x not in stop_words]
            
        remove_stpwds=remove_stopwords(remove_lowercase)

        #lemmatizing the input
        def lemmatize_word(text):
            wordnet = WordNetLemmatizer()
            return " ".join([wordnet.lemmatize(word) for word in text])

        lemmatize=lemmatize_word(remove_stpwds)

        #predicting the article category

        y_pred1 = cv.transform([lemmatize])
        yy = classifier.predict(y_pred1)
        #print(yy)
        result = ""
        if yy == [1]:
            result = "Sports News"
        elif yy == [2]:
            result = "Politics News"
        elif yy == [3]:
            result = "Economics News"
        elif yy == [4]:
            result = "Climate News"
        
        if z!='':
            st.write('The article is classified as')
            st.success(result)
        else:
            st.warning('Copy and paste any news articles in the box above')
if __name__=='__main__':
        main()

