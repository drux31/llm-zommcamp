import pandas as pd
import requests

docs_url = 'https://github.com/alexeygrigorev/llm-rag-workshop/raw/main/notebooks/documents.json'
docs_response = requests.get(docs_url)
documents_raw = docs_response.json()

documents = []

for course in documents_raw:
    course_name = course['course']

    for doc in course['documents']:
        doc['course'] = course_name
        documents.append(doc)

#print(documents[2])
# create the dataframe
df = pd.DataFrame(documents, columns=['course', 'section', 'question', 'text'])

#print(df.head())
#print(df.tail())
#print(df[df.course == 'data-engineering-zoomcamp'])

## sickit learn for text-search
# Vector spaces
# Take the document and turn it into vectors
# term-document matrix:
#   - rows: documents;
#   - columns: words/tokens

from sklearn.feature_extraction.text import CountVectorizer

docs_example = [
    "Course starts on 15th Jan 2024",
    "Prerequisites listed on GitHub",
    "Submit homeworks after start date",
    "Registration not required for participation",
    "Setup Google Cloud and Python before course"
]

cv = CountVectorizer(stop_words='english')
x = cv.fit_transform(docs_example)

names = cv.get_feature_names_out()

df_docs = pd.DataFrame(x.toarray(), columns=names).T
print(df_docs)