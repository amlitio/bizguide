import streamlit as st
import requests
import openai

# Constants
DATA_URL = "https://path_to_corporate_data_file.txt"  # URL

def download_corporate_data_file():
    response = requests.get(DATA_URL)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.text.splitlines()  # Split the content into lines

def check_name_availability(name):
    # Download and parse the Corporate Data File
    business_names = download_corporate_data_file()
    return name not in business_names

# Function to get advice from OpenAI's GPT-3.5 Turbo
def get_business_advice(user_input):
    openai.api_key = 'YOUR_OPENAI_API_KEY'  # Replace with your OpenAI API key
    response = openai.Completion.create(
      engine="gpt-3.5-turbo",
      prompt=user_input,
      max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    st.title("Florida Business Advisor")
    
    # Business Name Check
    st.subheader("Free Guidance & Name Check")
    business_name = st.text_input("Enter your desired business name:")
    if st.button("Check Name Availability"):
        is_available = check_name_availability(business_name)
        if is_available:
            st.success(f"The name {business_name} is available!")
        else:
            st.warning(f"The name {business_name} is already taken.")
    
    # Business Structure Guidance with Questionnaire
st.subheader("Business Structure Guidance")
option = st.selectbox(
    "Select your preference if you know:",
    ["I'm not sure", "Corporation", "LLC", "Partnership"]
)
if option == "I'm not sure":
    st.write("Let's guide you through a series of questions to determine the best structure for you.")
    
    # 1. Protection of Personal Assets
    q1 = st.selectbox(
        "Do you want to protect your personal assets from the company's liabilities?",
        ["Yes", "No", "Not Sure"]
    )
    
    # 2. Number of Owners
    q2 = st.selectbox(
        "How many owners will the business have?",
        ["Single owner", "Multiple owners"]
    )
    
    # 3. Business Profit and Loss
    q3 = st.selectbox(
        "How do you want the business profits and losses to be handled for tax purposes?",
        ["Pass through to owners", "Retained in the business", "Not Sure"]
    )
    
    # 4. Business Duration
    q4 = st.selectbox(
        "Do you want the business to continue even if an owner withdraws or passes away?",
        ["Yes", "No", "Not Sure"]
    )
    
    # 5. Business Management
    q5 = st.selectbox(
        "How do you want the business to be managed?",
        ["Owners manage directly", "Designated managers", "Not Sure"]
    )
    
    # 6. Investment Intentions
    q6 = st.selectbox(
        "Do you plan to seek significant outside investment?",
        ["Yes", "No", "Not Sure"]
    )
    
    # 7. Business Operations Location
    q7 = st.selectbox(
        "Where do you primarily plan to operate your business?",
        ["Within one state", "Multiple states", "Internationally", "Online only"]
    )
    
        if st.button("Get Guidance"):
            user_input = f"Protection of assets: {q1}, Owners: {q2}, Profit handling: {q3}, Business duration: {q4}, Management: {q5}, Investment: {q6}, Operation location: {q7}"
            advice = get_business_advice(user_input)
            st.write(advice)

if __name__ == "__main__":
    main()

    
