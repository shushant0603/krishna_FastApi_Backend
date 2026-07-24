from langchain_community.vectorstores import FAISS
from app.services.embedding import embeddings
from app.services.prompt import prompt
from app.services.llm_service import ask_llm

# -----------------------------------------------------
# STEP 1 : Load already created FAISS vector database
# -----------------------------------------------------
# Ye "vector_db" folder se index.faiss aur index.pkl ko load karta hai.
# Dubara embeddings create nahi hoti, sirf existing database memory me aata hai.
vector_db = FAISS.load_local(
    "vector_db",
    embeddings,
    allow_dangerous_deserialization=True
)


# -----------------------------------------------------
# STEP 2 : Create Retriever
# -----------------------------------------------------
# Retriever ka kaam hai user ke question ke hisab se
# sabse relevant chunks search karna.
#
# k = 3 matlab top 3 similar chunks return honge.
retriever = vector_db.as_retriever(
    search_kwargs={"k": 3}
)


# -----------------------------------------------------
# TESTING PART
# -----------------------------------------------------
# Neeche wala code sirf testing ke liye hai.
# Production me iski zarurat nahi hogi.
# query = "What does Krishna say about karma?"


# # Retriever question ko vector me convert karega,
# # FAISS me similarity search karega,
# # aur top 3 documents return karega.
# docs = retriever.invoke(query)

# print(f"Retrieved {len(docs)} documents\n")


# # Har retrieved document ka thoda content print kar rahe hain.
# for i, doc in enumerate(docs, start=1):
#     print(f"---------- Chunk {i} ----------")
#     print(doc.page_content[:500])
#     print()


# -----------------------------------------------------
# PRODUCTION FUNCTION
# -----------------------------------------------------
# Future me FastAPI isi function ko call karega.
#
# User -> Route -> ask_question()
#
# Abhi ye sirf relevant documents return kar raha hai.
# Agle step me isi function ke andar
# Prompt banega
# LLM call hoga
# Final answer return hoga.
def ask_question(question: str,chat_history):

    # Step 1: Retrieve relevant chunks
    docs = retriever.invoke(question)

    # Step 2: Create context
    context = "\n\n".join(
        doc.page_content for doc in docs
    )
    history = "\n".join(
        f"{msg.role}: {msg.content}"
       for msg in chat_history
      )

    # Step 3: Fill prompt
    final_prompt = prompt.invoke({
          "history": history,
         "context": context,
         "question": question
    })

    # Step 4: Call LLM
    answer = ask_llm(final_prompt)

    return answer