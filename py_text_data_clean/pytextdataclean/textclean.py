# import libraries
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from tqdm import tqdm

nltk_stopwords = stopwords.words('English')

# Function to remove html tags
def remove_html_tags(data: list = None):
    html_pattern = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6})')
    html_clean = [re.sub(html_pattern, '', i) if type(i) == str else i for i in data]
    return html_clean

# Function to remove NLTK stop words
def remove_nltk_stopwords(data: list = None):

    # change to lower case
    data = [i.lower().strip() if type(i) == str else i for i in data]
    l1 = []
    for i in tqdm(data):
        l2 = []
        # if str(i) != 'nan':
        if type(i) == str:
            l2 = ' '.join([m.strip() for m in i.split() if m not in nltk_stopwords])
            if l2:
                l1.append(l2)
    return l1

# Function to remove URLs
def remove_url(data: list = None):
    url_removed = [re.sub(r"http\S+", '', i) if type(i) == str else i for i in data]
    return url_removed

# Function to remove punctuations
def remove_punctuation(data: list = None):
    pun_removed = [re.sub('[^a-zA-Z0-9]', ' ', i) if type(i) == str else i for i in data]
    return pun_removed

# Function to remove digits
def remove_digits(data: list = None):
    digits_removed = [re.sub('[0-9]', ' ', str(i)) if str(i)!='nan' else np.nan for i in data]
    return digits_removed

# Function to remove foreign languages
def remove_foreign_languages(data: list = None):
    foreign_lang_removed = [re.sub("([^\x00-\x7F])+",'', i) if type(i) == str else i for i in data]
    return foreign_lang_removed

# Function to remove spaces
def remove_spaces(data: list = None):
    spaces_removed = [re.sub(' +',' ', i.strip()) if type(i) == str else i for i in data]
    return spaces_removed

# Function to clean text with customized parameters
def text_clean(data: list = None,
                html_tags: bool = True,
                url: bool = True,
                nltk_stopwords: bool = True,
                punctuations: bool = True,
                digits: bool = True,
                foreign_languages: bool = True
               ):
    
    
    # convert to lower space
    # clean_list = [i.lower().strip() if str(i)!='nan' else np.nan for i in data]
    clean_list = [i.lower().strip() if type(i) == str else i for i in data]
    
    # removes html tags
    if html_tags:
        clean_list = remove_html_tags(clean_list)
    
    # removes url
    if url:
        clean_list = remove_url(clean_list)
    
    # adds space before punctuations except '
    # while removing stopwords, if we have word followed by punctuation, it is not getting removed
    # to remove it, we will add space.
    # removes nltk stop words
    if nltk_stopwords:
        clean_list = [re.sub('([!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~])', r' \1 ', i) if type(i) == str else i for i in clean_list]
        clean_list = remove_nltk_stopwords(clean_list)
    
    # removes punctuations
    if punctuations:
        clean_list = remove_punctuation(clean_list)
    
    # removes digits
    if digits:
        clean_list = remove_digits(clean_list)
    
    # removes foreign languages
    if foreign_languages:
        clean_list = remove_foreign_languages(clean_list)
    
    # removes additional spaces and strips
    # clean_list = [re.sub(' +',' ', i.strip()) if str(i)!='nan' else np.nan for i in clean_list]
    clean_list = [re.sub(' +',' ', i.strip()) if type(i) == str else i for i in clean_list]
    
    return clean_list