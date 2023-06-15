from PyPDF2 import PdfReader
from langchain.chains.api.openapi import chain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, weaviate, FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import os


os.environ["OPEN_API_KEY"] = "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"

reader = PdfReader('2023_GPT4All_Technical_Report.pdf')

# print(reader)

raw_text = ""

for i, page in enumerate(reader.pages):
    text =page.extract_text()
    if text:
        raw_text += text

# print(raw_text)

text_spliter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 2200,
    chunk_overlap=200,
    length_function= len,
)
texts = text_spliter.split_text(raw_text)
print(len(texts))

print(texts[0])

embeddings = OpenAIEmbeddings(openai_api_key = "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")

docSearch = FAISS.from_texts(texts,embeddings)

print(docSearch)
chain = load_qa_chain(OpenAI(), chain_type="stuff")

query = "Who is the Author of the article?"
docs = docSearch.similarity_search(query)
chain.run(input_documents=docs, question=query)







