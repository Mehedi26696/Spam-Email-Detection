# Spam Email Detection

This project is a **Spam Email Detection System** that utilizes machine learning algorithms to classify emails as `Spam` or `Not Spam`. The project includes a user-friendly interface built with **Streamlit** for real-time predictions.

## Features
- **Machine Learning Algorithm:** Implements a trained model to detect spam emails with high accuracy.
- **Streamlit UI:** Allows users to input email text and get predictions instantly.
- **Preprocessing Pipeline:** Cleans and preprocesses text data for model compatibility.

## Installation

Follow these steps to set up the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/spam-email-detection.git
   cd spam-email-detection
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the following files are present in the directory:
   - `model.pkl`: Trained machine learning model.
   - `vectorizer.pkl`: Pretrained TF-IDF vectorizer.

## Usage

Run the Streamlit application:
```bash
streamlit run app.py
```

This will launch the Streamlit interface in your default browser. Paste any email text into the input box and click the **Predict** button to classify the email.

## Project Structure
```
spam-email-detection/
├── app.py              # Main Streamlit application
├── model.pkl           # Trained machine learning model
├── vectorizer.pkl      # Pretrained TF-IDF vectorizer
├── requirements.txt    # Required Python libraries
├── README.md           # Project documentation
└── data/               # (Optional) Directory for raw datasets
```

## Preprocessing Steps
The input email text undergoes the following preprocessing steps:
1. Conversion to lowercase.
2. Removal of URLs, HTML tags, and special characters.
3. Removal of punctuation and numbers.
4. Tokenization and vectorization using TF-IDF.

## Machine Learning Algorithm
The model is trained using:
- **Algorithm:** Naive Bayes

## Future Enhancements
- Integrate more advanced NLP techniques (e.g., BERT, GPT) for improved accuracy.
- Include features like attachments or subject line analysis.
- Deployment as a standalone web or mobile app.

## Requirements
- Python 3.8+
- Streamlit
- Scikit-learn
- Pandas

Install all dependencies with:
```bash
pip install -r requirements.txt
```

## License
This project is licensed under the [MIT License](LICENSE).

---

Happy coding! 🚀
