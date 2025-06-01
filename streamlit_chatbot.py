import streamlit as st
from together import Together

# Initialize Together client once
client = Together(api_key="868e7cdaad3e559398f26b7a7bca0c955f7836d4161dedc7eab3cd2a87778f42")

st.title("Chat with LLaMA-3 (via Together API)")

# Chat history saved in session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

def get_response(messages):
    response = client.chat.completions.create(
        model="meta-llama/Llama-3-8b-chat-hf",
        messages=messages
    )
    return response.choices[0].message.content

# User input
user_input = st.text_input("Your message:", key="input")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Get response from the model
    with st.spinner("Thinking..."):
        answer = get_response(st.session_state.messages)
    
    # Add assistant message
    st.session_state.messages.append({"role": "assistant", "content": answer})
    
    # Clear input box
    del st.session_state["input"]  
# Display chat messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"*You:* {msg['content']}")
    elif msg["role"] == "assistant":
        st.markdown(f"*Assistant:* {msg['content']}")