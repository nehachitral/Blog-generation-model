import streamlit as st

from langchain_community.llms import CTransformers

def getLLamaresponse(input_text, no_words, blog_style):
    try:
        llm = CTransformers(model='C:\\Users\I AM HP\OneDrive\Desktop\langchain\models\llama-2-7b-chat.ggmlv3.q8_0.bin',
                            model_type='llama',
                            config={'max_new_tokens': 256, 'temperature': 0.01})
        
        prompt = """
            Write a blog for {blog_style} job profile on the topic "{input_text}"
            within {no_words} words.
        """
        
        response = llm.invoke(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
        
        st.write("Input Text:", input_text)  # Debugging statement
        st.write("No of Words:", no_words)  # Debugging statement
        st.write("Blog Style:", blog_style)  # Debugging statement
        
        response = llm(prompt)
        return response
    except Exception as e:
        st.error(f"Error: {e}")
        return None

st.set_page_config(page_title="Generate Blogs",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")

col1, col2 = st.columns([1, 1])
with col1:
    no_words = st.text_input('No of Words')
with col2:
    blog_style = st.selectbox('Writing the blog for',
                              ('Researchers', 'Data Scientist', 'Common People'), index=0)
    
submit = st.button("Generate")

if submit:
    response = getLLamaresponse(input_text, no_words, blog_style)
    if response is not None:
        st.write("Generated Response:", response)  # Debugging statement
    else:
        st.error("Failed to generate response.")

