# llama_chatbot

A chatbot interface that leverages ~~llama2~~ quantized llama3.1 8B model in the backend

- Backend: Fastapi to expose Llama model using llama-cpp-python
- Frontend: Streamlit chat interface to ask questions
- Storage: Use sqlite to store all chat logs

## App Architecture

![App Architecture](./assets/llama-chatbot-diagram.svg "Llama Chatbot")
