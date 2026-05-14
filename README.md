# Gen-AI-2.0: Gemini LLM Applications

This repository contains a collection of interactive web applications built using **Streamlit** and **Google's Gemini LLM** (via the `google-generativeai` SDK). These applications demonstrate various use cases of generative AI, including simple Q&A, conversational chatbots, and multimodal image analysis.

## 🚀 Features

*   **Simple Q&A Application (`app.py`)**: A straightforward interface where you can ask a question, and the Gemini model (`gemini-3.1-flash-lite`) will generate a response.
*   **Conversational Chatbot (`qachatbot.py`)**: A more advanced chat interface that maintains conversation history, allowing for contextual follow-up questions.
*   **Vision-Language Model (`vision.py`)**: A multimodal application that allows you to upload an image and ask questions about it or provide a text prompt to analyze the visual content.

## 🛠️ Prerequisites

*   Python 3.8+
*   A Google Gemini API Key

## ⚙️ Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Gen-AI-2.0.git
    cd Gen-AI-2.0
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Environment Variables:**
    *   Create a `.env` file in the root directory.
    *   Add your Google Gemini API Key to the file:
        ```env
        GOOGLE_API_KEY=your_actual_api_key_here
        ```

## 🏃‍♂️ Running the Applications

You can run any of the applications using Streamlit. Open your terminal and run one of the following commands:

*   **Run the Simple Q&A App:**
    ```bash
    streamlit run app.py
    ```

*   **Run the Conversational Chatbot:**
    ```bash
    streamlit run qachatbot.py
    ```

*   **Run the Vision App:**
    ```bash
    streamlit run vision.py
    ```

## 📦 Dependencies

*   `streamlit`: For building the web UI.
*   `google-generativeai`: The official SDK to interact with Google's Gemini models.
*   `python-dotenv`: To manage environment variables securely.
