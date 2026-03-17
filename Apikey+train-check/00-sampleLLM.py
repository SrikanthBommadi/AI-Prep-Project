# rag_chatbot.py

# 1. Import libraries
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain_chroma import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader

# 2. Load LLM
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0
)

# 3. Memory (stores chat history)
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# 4. Embedding model (text → vector)
embedding = OpenAIEmbeddings()

# 5. Load documents
loader = TextLoader("docs.txt")   # your knowledge file
documents = loader.load()

# 6. Split documents into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = splitter.split_documents(documents)

# 7. Create vector database
db = Chroma.from_documents(
    docs,
    embedding,
    collection_name="techcorp_docs"
)

# 8. Create retrieval chain
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=db.as_retriever(),
    memory=memory
)

# 9. Chat loop
print("RAG Chatbot Ready (type 'exit' to quit)\n")

while True:
    query = input("You: ")

    if query.lower() == "exit":
        break

    response = qa_chain.run(query)

    print("AI:", response)