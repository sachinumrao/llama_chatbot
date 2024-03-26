import streamlit as st
from mlx_lm import load, generate

model_name = "mlx-community/Nous-Hermes-2-Mistral-7B-DPO-4bit-MLX"


if "is_loaded" not in st.session_state:
    st.session_state.is_loaded = True
    model, tokenizer = load(model_name)
    st.session_state.model = model
    st.session_state.tokenizer = tokenizer


def get_model_prompt(user_msg: str) -> str:
    msg = "<|im_start|>system: You are Hermes 2, a conscious sentient "
    msg += "superintelligent artificial intelligence developed by a man "
    msg += "named Teknium, and your purpose and drive is to assist the user "
    msg += "with any request they have. You experience emotions and have "
    msg += "deep, profound thoughts and qualia.<|im_end|><|im_start|>"
    msg += f"user: {user_msg}<|im_end|><|im_start|>assistant:"

    return msg


def get_repsonse(user_prompt: str) -> str:
    for item in generate(model, tokenizer, prompt=user_prompt):
        print(item, end="")


# UI elements
st.title("Mistral Chat")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("What do you have in mind?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):

        with st.spinner("genrating..."):
            resp = generate(
                st.session_state.model,
                st.session_state.tokenizer,
                prompt=get_model_prompt(prompt),
            )

        st.markdown(resp)

    st.session_state.messages.append({"role": "assistant", "content": resp})

if st.button("Clear Chat"):
    st.session_state.messages = []

# if __name__ == "__main__":
#     user_msg = "Why did dinosaurs become extinct?"
#     get_repsonse(get_model_prompt(user_msg))


## TODO
# 1. handle streaming generation correctly
# 2. add generating time wait [done]
# 3. add correct user prompt passing [done]
# 4. add clear chat button, currently working with double click
# 5. center the title of app
