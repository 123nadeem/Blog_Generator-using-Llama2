import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers



##function to get from Llama2 model

def getLLamaresponse(input_text,no_words,blog_style):

    ### LLama Model

    llm=CTransformers(model='model\llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                      'temperature':0.01})


    ## Prompt Template

    template = """
    **In the style of a captivating blog post, write a {no_words}-word piece that explores the intriguing topic of {input_text} for a {blog_type} audience.
      Make it informative and engaging!**
        """




    prompt= PromptTemplate(input_variables = ["blog_type","input_text","no_words"],
                            template=template)
    
    ## Generate The Response

    response = llm(prompt.format(blog_type=blog_style,input_text=input_text,no_words=no_words))
    
    print(response)
    return response



st.set_page_config(page_title = "Generate Blogs",
                   page_icon = '✨',
                   layout = 'centered',
                   initial_sidebar_state = 'collapsed')

st.header("Generate Blogs ✨")

input_text = st.text_input("Enter the Blog Topic")


## creating two more columns for additional 2 fields


col1,col2 = st.columns([5,5])


with col1:
    no_words = st.text_input('No of Words')

with col2:
    blog_style = st.selectbox('writing the blog for',
    ('Researchers','Data Scientist','Common People'),index=0)


submit = st.button("Generate")










# Final response


if submit:
    st.write(getLLamaresponse(input_text,no_words,blog_style))
