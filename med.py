import streamlit as st
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import HuggingFaceHub
from tavily import TavilyClient

    HUGGINGFACE_API_KEY = "YOUR API KEY"
TAVILY_API_KEY = "YOUR API KEY"

llm = HuggingFaceHub(
    repo_id="google/flan-t5-base",  # You can change to another lightweight model
    huggingfacehub_api_token=HUGGINGFACE_API_KEY,
    model_kwargs={"temperature": 0.7, "max_new_tokens": 200},
)

tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

prompt_template = PromptTemplate(
    input_variables=["user_query", "medical_data"],
    template=(
        "You are a medical assistant. The user asked: {user_query}\n\n"
        "Here is trusted medical information: {medical_data}\n\n"
        "Provide a detailed response."
    ),
)

chat_chain = LLMChain(llm=llm, prompt=prompt_template)

def fetch_medical_info(query):
    try:
        response = tavily_client.qna_search(query)
        return response or "No relevant medical advice found."
    except Exception as e:
        return f"Error fetching data from Tavily: {e}"

def generate_response(user_query):
    medical_data = fetch_medical_info(user_query)
    response = chat_chain.run(user_query=user_query, medical_data=medical_data)
    return response

def main():
    st.set_page_config(page_title="Medical Chatbot", layout="centered")
    
    st.title("🩺 Medical Advice Chatbot")
    st.markdown("Ask your medical questions, and I'll provide helpful advice based on trusted sources.")

    user_query = st.text_input("Your Question:", placeholder="Type your question here...")

    if user_query.strip():
        with st.spinner("Fetching response..."):
            response = generate_response(user_query)
        st.markdown("### Response")
        st.write(response)
    else:
        st.warning("Please enter a question.")

    st.markdown("---")
    st.caption("Powered by LangChain, Tavily, and Hugging Face")

if __name__ == "__main__":
    main()
