import os


from PyPDF2 import PdfReader


from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


from langchain_groq import ChatGroq


from pinecone import Pinecone



from config import (
    PINECONE_API_KEY,
    PINECONE_INDEX,
    GROQ_API_KEY
)


from prompt.analyze_prompt import (
    RESUME_ANALYZER_PROMPT
)





# =========================
# PDF EXTRACTION
# =========================


def extract_pdf(file_path):


    reader = PdfReader(
        file_path
    )


    text = ""


    for page in reader.pages:


        page_text = page.extract_text()


        if page_text:

            text += page_text



    return text





# =========================
# TEXT CHUNKING
# =========================


def split_documents(text):


    splitter = RecursiveCharacterTextSplitter(

        chunk_size=800,

        chunk_overlap=100

    )


    chunks = splitter.split_text(
        text
    )


    return chunks





# =========================
# PINECONE
# =========================


pc = Pinecone(

    api_key=PINECONE_API_KEY

)



index = pc.Index(

    PINECONE_INDEX

)





# =========================
# EMBEDDING CREATION
# =========================


def create_embeddings(chunks):


    vectors=[]


    for i,chunk in enumerate(chunks):


        response = pc.inference.embed(

            model="llama-text-embed-v2",

            inputs=[chunk],

            parameters={

                "input_type":"passage",

                "truncate":"END"

            }

        )


        vectors.append(

            {

                "id":str(i),

                "vector":
                response[0]["values"],

                "text":chunk

            }

        )


    return vectors





# =========================
# STORE VECTORS
# =========================


def store_vectors(vectors):


    data=[]


    for item in vectors:


        data.append(

            {

                "id":
                item["id"],


                "values":
                item["vector"],


                "metadata":

                {

                    "text":
                    item["text"]

                }

            }

        )



    index.upsert(

        vectors=data

    )





# =========================
# SEARCH
# =========================


def search_vectors(
    query,
    k=5
):


    response = pc.inference.embed(

        model="llama-text-embed-v2",

        inputs=[query],

        parameters={

            "input_type":"query",

            "truncate":"END"

        }

    )


    query_vector = response[0]["values"]



    result = index.query(

        vector=query_vector,

        top_k=k,

        include_metadata=True

    )


    documents=[]



    for match in result.matches:


        documents.append(

            match.metadata["text"]

        )



    return documents





# =========================
# LLM
# =========================


llm = ChatGroq(

    api_key=GROQ_API_KEY,

    model="llama-3.1-8b-instant",

    temperature=0

)





def generate_answer(

    context,

    job_description

):


    prompt = RESUME_ANALYZER_PROMPT.format(

        context=context,

        job_description=job_description

    )



    response = llm.invoke(

        prompt

    )


    return response.content





# =========================
# COMPLETE PIPELINE
# =========================


def analyze_resume(

    file,

    job_description

):


    os.makedirs(

        "uploads",

        exist_ok=True

    )



    path = f"uploads/{file.filename}"



    with open(path,"wb") as f:


        f.write(

            file.file.read()

        )




    # Extract Resume

    text = extract_pdf(

        path

    )



    # Split

    chunks = split_documents(

        text

    )



    # Embeddings

    vectors = create_embeddings(

        chunks

    )



    # Store

    store_vectors(

        vectors

    )



    # Retrieve

    docs = search_vectors(

        "skills experience projects education",

        k=5

    )



    context = "\n\n".join(

        docs

    )



    # LLM Analysis

    result = generate_answer(

        context,

        job_description

    )



    return result