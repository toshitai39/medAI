# medAI
# Medical Advice Chatbot

A medical advice chatbot built using **LangChain**, **Tavily** for API calls, and an open-source **Hugging Face** model to provide trusted medical information. This chatbot assists users by providing relevant answers to their medical queries based on accurate medical data.

## Features
- **Medical Query Handling**: Users can ask any medical-related question, and the bot fetches relevant medical data using the Tavily API.
- **LLM-based Answer Generation**: The model generates human-like responses, combining the user query with relevant medical data.
- **Interactive UI**: Built using Streamlit, the application provides an interactive and easy-to-use interface for real-time communication.

## Technologies Used
- **Streamlit**: For building the interactive web interface.
- **LangChain**: To integrate the language models with custom prompts.
- **Hugging Face**: To leverage open-source models for text generation.
- **Tavily API**: To fetch trusted medical information.

## Setup

### Prerequisites
- Python 3.6+
- A **Hugging Face** API key for accessing models (e.g., `google/flan-t5-base` or another model of choice).
- A **Tavily** API key for fetching medical data.

### Step 1: Clone the Repository
Clone this repository to your local machine:
### Step 2: Install Dependencies
Make sure you have virtualenv or conda to create isolated environments.

Create a virtual environment (optional but recommended):

###Step 3: Configure API Keys
Obtain your Hugging Face API key from Hugging Face.
Obtain your Tavily API key from Tavily.

###Step 4: Run the Application
