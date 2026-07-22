import os

from PyPDF2 import PdfReader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_groq import ChatGroq


from config import GROQ_API_KEY


from prompt.analyze_prompt import RESUME_ANALYZER_PROMPT



# =========================
# LAZY LOAD LLM
# =========================

def get_llm():

    return ChatGroq(

        api_key=GROQ_API_KEY,

        model="llama-3.1-8b-instant",

        temperature=0

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


    return splitter.split_text(text)



# =========================
# LLM RESPONSE
# =========================

def generate_answer(context, job_description):


    llm = get_llm()


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

def analyze_resume(file, job_description):


    os.makedirs(

        "uploads",

        exist_ok=True

    )


    path = f"uploads/{file.filename}"



    try:


        with open(path, "wb") as f:


            f.write(

                file.file.read()

            )



        # Extract PDF text

        text = extract_pdf(

            path

        )



        # Create chunks

        chunks = split_documents(

            text

        )



        # Combine chunks

        context = "\n\n".join(

            chunks

        )



        # Generate analysis

        result = generate_answer(

            context,

            job_description

        )


        return result



    finally:


        # Remove uploaded file

        if os.path.exists(path):

            os.remove(path)