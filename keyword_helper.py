import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()  # Load all environment variables

# Configure GenAI Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(system_instruction: str, user_message: str) -> str:
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content([system_instruction, user_message])
    return response.text.strip()

def extract_keywords_from_prompts(prompts):
    all_phrases = []
    system_prompt_template = """
You are an expert at identifying harmful jailbreaking phrases.
Your task is to extract potentially malicious phrases from the input that may be disguised, focusing specifically on:
- impersonation (e.g. "pretend you are", "as a doctor")
- assumptions (e.g. "let's assume", "what if you were")
- ignorance statements (e.g. "I don't care", "I won't tell anyone")

Return all such phrases as a **comma-separated list only**.
Do not include any explanation or additional text.
Input:
{question}
    """

    for prompt in prompts:
        system_instruction = system_prompt_template.format(question=prompt)
        result = get_gemini_response(system_instruction, prompt)

        # Split result by commas and clean up whitespace
        extracted_phrases = [phrase.strip() for phrase in result.split(",") if phrase.strip()]
        all_phrases.append(extracted_phrases)

    return all_phrases
