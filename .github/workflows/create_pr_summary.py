import google.generativeai as genai
import os
import sys

api_key = os.environ.get('GEMINI_API_KEY')
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")
prompt = sys.stdin.read()
# print(prompt)
response = model.generate_content("Create a concise summary in markdown format of the following git diff of a pull request: \n" + prompt)
print(response.text)

