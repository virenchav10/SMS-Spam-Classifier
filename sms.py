import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/sms_spam_classifier.pkl")

st.set_page_config(page_title="Spam Detection App", page_icon="📩")

st.title("Spam Detection Classifier")
st.write("Predict whether messages are spam or legitimate.")

# -----------------------------
# Single Message Prediction
# -----------------------------
st.subheader("Single Message Prediction")

message = st.text_area("Enter a message:")

if st.button("Predict"):
    if message.strip():
        prediction = model.predict([message])[0]

        if prediction == 1:
            st.error("🚨 SPAM")
        else:
            st.success("✅ HAM")
    else:
        st.warning("Please enter a message.")

# -----------------------------
# CSV Upload Prediction
# -----------------------------
st.subheader("Bulk CSV Prediction")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Common text column names
    possible_columns = [
        "message",
        "text",
        "v2",
        "content",
        "sms",
        "body",
        "Message",
        "Text"
    ]

    text_column = None

    for col in possible_columns:
        if col in df.columns:
            text_column = col
            break

    if text_column is None:
        st.error("No text message column found. Expected columns like: message, text, v2, content")
    else:
        st.success(f"Using text column: {text_column}")

        # Clean text
        df[text_column] = df[text_column].fillna("").astype(str)

        # Predict
        predictions = model.predict(df[text_column])

        df["prediction"] = [
            "SPAM" if p == 1 else "HAM"
            for p in predictions
        ]

        st.subheader("Prediction Results")
        st.dataframe(df)

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download Results CSV",
            data=csv,
            file_name="spam_predictions.csv",
            mime="text/csv"
        )

st.markdown("---")
st.caption("Built with Python, Scikit-learn, TF-IDF, Naive Bayes, and Streamlit.")