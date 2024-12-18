import streamlit as st
import pickle
import pandas as pd

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f0f4f8;
            font-family: 'Arial', sans-serif;
        }
        .main {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 20px;
            max-width: 600px;
            margin: auto;
            margin-top: 50px;
        }
        .title {
            color: #333;
            font-size: 32px;
            text-align: center;
            margin-bottom: 20px;
        }
        .input-box {
            background-color: #f7f7f7;
            border-radius: 5px;
            border: 1px solid #ddd;
            padding: 10px;
            width: 100%;
            font-size: 16px;
            box-sizing: border-box;
        }
        .button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 18px;
            cursor: pointer;
            border-radius: 5px;
            margin-top: 15px;
            width: 100%;
        }
        .button:hover {
            background-color: #45a049;
        }
        .result {
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
        }
        .error {
            color: #e74c3c;
        }
        .success {
            color: #2ecc71;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown('<div class="title">Email Spam Detection</div>', unsafe_allow_html=True)

# Create input box for the email text
text_input = st.text_area(
    "Enter the email text to check if it is spam or not:",
    placeholder="Type your email text here...",
    height=200,
    key="email_input",
    label_visibility="collapsed",
    help="Paste or type the email content to detect if it's spam."
)

# Add a "Check" button
if st.button('Check', key="check_button"):
    # Check for empty input
    if not text_input.strip():
        st.markdown('<div class="result error">Please enter an email text!</div>', unsafe_allow_html=True)
        st.stop()

    try:
        # Load the pre-trained model
        model = pickle.load(open('clf.pkl', 'rb'))

        # Preprocess input if needed (e.g., lowercasing, removing special chars)
        # Example: preprocess_text = preprocess_function(text_input)

        # Predict using the model
        prediction = model.predict([text_input])

        # Display the result
        if prediction[0] == 1:
            st.markdown('<div class="result error">This is a spam email!</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result success">This email is NOT a spam!</div>', unsafe_allow_html=True)

    except FileNotFoundError:
        st.markdown('<div class="result error">Model file not found! Please make sure "clf.pkl" is in the correct directory.</div>', unsafe_allow_html=True)
    except Exception as e:
        st.markdown(f'<div class="result error">An error occurred: {e}</div>', unsafe_allow_html=True)

