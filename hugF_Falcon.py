import requests

API_URL = "https://api-inference.huggingface.co/models/Falconsai/text_summarization"
headers = {"Authorization": "Bearer "}

def get_Falconsai_response(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()


# class App:
#     def __init__(self):
#         st.title("​ATS_Tracking_AI")
#         jd = st.text_area("Paste the Job Description", height=300   )
#         files = st.file_uploader("Upload Your Resume", type="pdf", accept_multiple_files=True, help="Please Upload the files here")
#         submit = st.button("Submit")

#         if submit:
#             if files is not None:
#                 st.sidebar.title("Resume Analysis")
#                 i=1
#                 for file in files:
#                     if file is not None:
#                         with st.spinner(f'Analyzing {file.name}...'):
#                             text = input_pdf_txt(file)
#                             data = inputprmt(text, jd)
#                             response = get_gemini_response(data)
#                             st.header(file.name)    
#                             st.write(response)
#                             match_percentage_index = response.find("Match Percentage:")
#                             if match_percentage_index != -1:
#                                 match_percentage_str = response[match_percentage_index:].split()[2]
#                                 percentage_value = match_percentage_str.rstrip('%')
#                             else:
#                                 percentage_value = "N/A"

#                             st.sidebar.table({"Sr No.":[i],"Resume Name": [file.name], "Match Percentage": [percentage_value]})
#                             i+=1
