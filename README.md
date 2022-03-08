### Python Package Link:
 - __https://pypi.org/project/py-text-data-clean/__

## Project Description
- This package cleans the text data such as removal of HTML tags, URLs, NLTK Stopwords, numbers, punctuations.
 
### Features
 - Remove URLs
 - Remove HTML Tags
 - Remove NLTK Stopwords
 - Remove Numbers
 - Remove Punctuations
 - Remove Additional Spaces
 - Changes to Lower Case
 
### Installation
 - In the code notebook like IPYNB use the below command\
   ```
   !pip install py-text-data-clean
   ```
 
 
 - If installing from Anaconda Prompt of CMD Terminal, use the below command\
   ```
   pip install py-text-data-clean
   ```
   
 - Note:
  ```
   Check if the package version is upgraded. If the version is not upgraded, please upgrade it.

   # To check the version, run the below code
   !pip show py-text-data-clean

   # To upgrade the package, run the below code
   !pip install py-text-data-clean -U
   ```

### Usage

#### Input:
```
 - List of text data - Example: ["Is the   time 12 Noon now, isn't it?", "It is a python link: https://pypi.org/"]
 ```
 
#### Output:
```
 - ['time noon', 'python link']
 ```
 
#### Code to clean text with a single function:
 ```
 # Import the library
 from pytextdataclean import textclean as tc
 input_text_list = ["Is the   time 12 Noon now, isn't it?", "It is a python link: https://pypi.org/"]
 result = tc.text_clean(data=input_text_list)
 print(result)
 ```

 #### Code to use each available features:

 ```
 # Pass the list of text

 # Example list:
 input_text_list = ["Is the   time 12 Noon now, isn't it?", "It is a python link: https://pypi.org/"]

 # Import the library
 from pytextdataclean import textclean as tc

 # To remove html tags
 tc.remove_html_tags(data=input_text_list)

 # To remove NLTK stop words
 tc.remove_nltk_stopwords(data=input_text_list)

 # To remove URLs
 tc.remove_url(data=input_text_list)

 # To remove punctuations
 tc.remove_punctuation(data=input_text_list)

 # To remove numerical digits
 tc.remove_digits(data=input_text_list)

 # To remove foreign languages
 tc.remove_foreign_languages(data=input_text_list)

 # To remove spaces
 tc.remove_spaces(data=input_text_list)
 ```
