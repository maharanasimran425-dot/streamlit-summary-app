import streamlit as st


from google import genai
st.title("QuickSummary")

client = genai.Client(api_key="AIzaSyByxAvghwrrjTBczinskJvm1BOrAM7iNi8")

def answer(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""You are expert in summerizing, summerize this file:
        -use heading of the content
        -start with catching line
        {prompt}"""
    )
    return response

content=st.file_uploader("Upload a file to summerize:")
if st.button("Generating"):
       if content:
        with st.spinner("Generating summary..."):
            prompt=content.read()
            result=answer(prompt)
            st.write(result.text)
       else:
           st.warning("Please uplode your file ⚠") 
    
   