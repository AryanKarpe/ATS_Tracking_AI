import streamlit as st 
import google.generativeai as genai
import os
import PyPDF2 as pdf
import openai
import json
from dotenv import load_dotenv
import re #regular expression operations
import hugF_Falcon as falcon

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
def get_gemini_response(input):
    model=genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

# openai.api_key = os.getenv("OPENAI_API_KEY")
# def get_openai_response(input):
#     response = openai.Completion.create(engine="gpt-3.5-turbo-instruct", prompt=input, max_tokens=50)
#     return response.choices[0].text

def input_pdf_txt(uploadedfile):
    reader = pdf.PdfReader(uploadedfile)
    text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text()
    # print(text)
    return text

def inputprmt(txt, jd):
    return f"""
        Job Description:
        {jd}
        Candidate's Resume:
        {txt}
        Analysis:
        Based on the provided job description and the candidate's resume, please perform a comprehensive analysis to evaluate the candidate's suitability for the position. Consider the following factors:
        1. Skills Match: Assess how well the candidate's skills and qualifications align with the job requirements outlined in the job description.
        2. Experience Match: Evaluate the candidate's relevant work experience and accomplishments in comparison to the job responsibilities and desired qualifications.
        3. Education and Certifications: Review the candidate's educational background and any relevant certifications to determine their suitability for the role.
        4. Additional Considerations: Take into account any additional factors or specific requirements mentioned in the job description, such as preferred traits or specific technical expertise.
        Analysis Output:
        - Match Percentage: Provide a precise percentage indicating the degree of match between the candidate's profile and the job description. 
        - Missing Keywords: Identify any keywords or skills mentioned in the job description that are missing or not adequately represented in the candidate's resume.
        - Profile Summary: Summarize the candidate's qualifications, highlighting key skills, experiences, and achievements relevant to the position.
        - Recommendations (if applicable): Offer any additional insights or recommendations based on the analysis, such as areas for improvement or specific strengths that make the candidate well-suited for the role.
        Please ensure the analysis output is presented in a clear and structured format and simple language. Thank you.
        Provide the output in below format
        1)Match Percentage
        2)Missing Keywords
        3)Profile Summary
        4)Recommendations (if applicable)
        """












class App:
    def __init__(self):
        st.title("​ATS_Tracking_AI")
        jd=st.text_area("Paste the Job Description", height=200)
        uploadedfile = st.file_uploader("Upload Your Resume", type="pdf", help="Please Upload the file here")
        submit = st.button("Submit")

        if submit:
            if uploadedfile is not None:
                with st.spinner('Analyzing the resume...'):
                    text=input_pdf_txt(uploadedfile)
                    data = inputprmt(text,jd)
                    # print(data)
                    response = get_gemini_response(data)    
                    # response = get_openai_response(input_prompt)
                    st.write(response)
                    print(response)        

                    st.sidebar.title("Resume Analysis")
                    match_percentage = re.search(r"Match Percentage: (\d+)%", response)
                    st.sidebar.table({"Resume Name": [uploadedfile.name], "Match Percentage": [match_percentage]}) 
                    
                    
app= App()