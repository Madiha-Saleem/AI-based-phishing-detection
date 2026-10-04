import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/phishing_model.pkl")

st.set_page_config(page_title="AI-Based Phishing Website Detection", layout="wide")

st.title("🛡 AI-Based Phishing Website Detection")
st.write("Enter the website features below and click **Predict**.")

# Feature names (same order as training data)
features = [
    "having_IPhaving_IP_Address",
    "URLURL_Length",
    "Shortining_Service",
    "having_At_Symbol",
    "double_slash_redirecting",
    "Prefix_Suffix",
    "having_Sub_Domain",
    "SSLfinal_State",
    "Domain_registeration_length",
    "Favicon",
    "port",
    "HTTPS_token",
    "Request_URL",
    "URL_of_Anchor",
    "Links_in_tags",
    "SFH",
    "Submitting_to_email",
    "Abnormal_URL",
    "Redirect",
    "on_mouseover",
    "RightClick",
    "popUpWidnow",
    "Iframe",
    "age_of_domain",
    "DNSRecord",
    "web_traffic",
    "Page_Rank",
    "Google_Index",
    "Links_pointing_to_page",
    "Statistical_report"
]

inputs = []

cols = st.columns(3)

for i, feature in enumerate(features):
    value = cols[i % 3].selectbox(
        feature,
        [-1, 0, 1],
        key=feature
    )
    inputs.append(value)

if st.button("Predict Website"):

    data = pd.DataFrame([inputs], columns=features)

    prediction = model.predict(data)[0]

    if prediction == 1:
        st.success("✅ Legitimate Website")
    else:
        st.error("🚨 Phishing Website")