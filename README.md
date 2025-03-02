# Career Chatbot 🎯

## Overview
The **Career Chatbot** is an AI-powered chatbot designed to assist job seekers in exploring career opportunities, job roles, required skills, salary expectations, and other career-related queries. The chatbot is built using **Streamlit**, **Google Generative AI (Gemini-1.5-flash)**, and **Machine Learning techniques** like TF-IDF and Cosine Similarity for job recommendation.

The chatbot fetches relevant career advice based on user queries, compares them with a dataset of job listings, and refines the response using an AI-powered text generation model. The project has been **successfully deployed**.

## Features
- 📂 **Job Data Processing**: Loads and preprocesses a CSV dataset of job listings.
- 🔍 **Job Matching Algorithm**: Uses **TF-IDF Vectorization** and **Cosine Similarity** to find the best job matches.
- 🧠 **AI-Powered Career Advice**: Generates refined career guidance using **Google Generative AI**.
- 🗣️ **Interactive Chat Interface**: Provides a smooth user experience with an intuitive **Streamlit** UI.
- 🚀 **Deployment Ready**: Fully functional and **deployed** for public access.

## Tech Stack
- **Frontend**: Streamlit (Python-based web framework)
- **Backend**: Google Generative AI API (Gemini-1.5-flash), Scikit-learn, Pandas
- **Data Processing**: TF-IDF Vectorizer, Cosine Similarity
- **Deployment**: Hosted and deployed for user access

## Installation Guide
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Pip (Python package manager)

### Steps to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/Chitti333/chatbot.git
   cd career-chatbot
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place the **careerDSet.csv** dataset in the project directory.
4. Set up your **Google Generative AI API Key**:
   ```bash
   export GOOGLE_API_KEY="your-api-key-here"
   ```
5. Run the Streamlit app:
   ```bash
   streamlit run chatbot.py
   ```
6. Open the app in your browser using the displayed **local URL**.

## Usage
- Enter your career-related question in the text box.
- The chatbot finds the best job match based on **skills and job titles**.
- If a match is found, it provides a **detailed career recommendation**.
- If no match is found, the chatbot generates **general career guidance**.

## Deployment
The chatbot has been **successfully deployed**, allowing users to access it online without setting up locally.
Deployed Link - [Carrer-Guide](https://career-chatbot-hx.streamlit.app/)

## Future Enhancements
- 🏆 **User Authentication**: Personalized career suggestions.
- 📊 **More Job Data**: Expand the dataset with real-time job listings.
- 🌍 **Multilingual Support**: Support career queries in multiple languages.

## Contributors
- **Chitti Thalli Kaja** – Developer
- **Open to Contributions!**

