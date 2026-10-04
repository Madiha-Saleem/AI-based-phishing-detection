import streamlit as st
import joblib

# Page Configuration
#sets title of the browser tab
st.set_page_config(
    page_title="AI Phishing Website Detection",
    page_icon="🛡️",
    layout="wide"
)

# Load the ML Model
model = joblib.load("models/phishing_model.pkl")

# Sidebar
st.sidebar.title("🛡️ Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "🏠 Dashboard",
        "🔍 Predict",
        "📊 Model Performance",
        "ℹ️ About Project"
    ]
)

# -------------------------
# DASHBOARD PAGE
if page == "🏠 Dashboard":

    st.title("🛡️ AI-Based Phishing Website Detection")

    st.markdown("""
This project uses **Machine Learning** to detect whether a website is **Legitimate** or **Phishing**.
""")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Dataset",
            value="11,055",
            delta="Records"
        )

    with col2:
        st.metric(
            label="Features",
            value="30"
        )

    with col3:
        st.metric(
            label="Best Model",
            value="Random Forest"
        )

    with col4:
        st.metric(
            label="Accuracy",
            value="96.70%"
        )

    st.divider()

    st.subheader("📌 Project Workflow")

    st.markdown("""
1. Collect phishing website dataset

2. Preprocess the data

3. Split into Training & Testing

4. Train Machine Learning models

5. Compare model accuracy

6. Select Random Forest

7. Save trained model

8. Deploy using Streamlit
""")

# -------------------------
# PREDICT PAGE

elif page == "🔍 Predict":
    
    st.title("🔍 AI Website Analysis")

    st.write("Select the website security features and click **Analyze Website**.")

    st.subheader("🌐 URL Features")

    col1, col2 = st.columns(2)

    with col1:
        ip = st.selectbox("Having IP Address", [-1, 0, 1])
        url_length = st.selectbox("URL Length", [-1, 0, 1])
        shortening = st.selectbox("Shortening Service", [-1, 0, 1])
        at_symbol = st.selectbox("@ Symbol", [-1, 0, 1])

    with col2:
        redirect = st.selectbox("Double Slash Redirecting", [-1, 0, 1])
        prefix = st.selectbox("Prefix-Suffix", [-1, 0, 1])
        subdomain = st.selectbox("Sub Domain", [-1, 0, 1])
        ssl = st.selectbox("SSL Final State", [-1, 0, 1])

    st.subheader("🔒 Domain Security")

    col3, col4 = st.columns(2)

    with col3:
        domain = st.selectbox("Domain Registration Length", [-1, 0, 1])
        favicon = st.selectbox("Favicon", [-1, 0, 1])
        port = st.selectbox("Port", [-1, 0, 1])
        https = st.selectbox("HTTPS Token", [-1, 0, 1])

    with col4:
        request = st.selectbox("Request URL", [-1, 0, 1])
        anchor = st.selectbox("URL of Anchor", [-1, 0, 1])
        links = st.selectbox("Links in Tags", [-1, 0, 1])
        sfh = st.selectbox("SFH", [-1, 0, 1])

    st.subheader("📊 Website Information")

    col5, col6 = st.columns(2)

    with col5:
        email = st.selectbox("Submitting to Email", [-1, 0, 1])
        abnormal = st.selectbox("Abnormal URL", [-1, 0, 1])
        red = st.selectbox("Redirect", [-1, 0, 1])
        mouse = st.selectbox("On Mouse Over", [-1, 0, 1])

    with col6:
        right = st.selectbox("Right Click", [-1, 0, 1])
        popup = st.selectbox("Popup Window", [-1, 0, 1])
        iframe = st.selectbox("IFrame", [-1, 0, 1])
        age = st.selectbox("Age of Domain", [-1, 0, 1])

    st.subheader("📈 Ranking Information")

    col7, col8 = st.columns(2)

    with col7:
        dns = st.selectbox("DNS Record", [-1, 0, 1])
        traffic = st.selectbox("Web Traffic", [-1, 0, 1])
        pagerank = st.selectbox("Page Rank", [-1, 0, 1])

    with col8:
        google = st.selectbox("Google Index", [-1, 0, 1])
        links_page = st.selectbox("Links Pointing to Page", [-1, 0, 1])
        statistical = st.selectbox("Statistical Report", [-1, 0, 1])

    if st.button("🚀 Analyze Website"):

        features = [[
            ip,
            url_length,
            shortening,
            at_symbol,
            redirect,
            prefix,
            subdomain,
            ssl,
            domain,
            favicon,
            port,
            https,
            request,
            anchor,
            links,
            sfh,
            email,
            abnormal,
            red,
            mouse,
            right,
            popup,
            iframe,
            age,
            dns,
            traffic,
            pagerank,
            google,
            links_page,
            statistical
        ]]

        prediction = model.predict(features)

        st.divider()

        if prediction[0] == 1:

            st.success("✅ Legitimate Website")

            st.info("""
Risk Level : LOW

Recommendation :

The website appears to be legitimate based on the selected security features.
""")

        else:

            st.error("🚨 Phishing Website Detected")

            st.warning("""
Risk Level : HIGH

Recommendation :

Avoid entering passwords, banking information or personal data.
""")

# -------------------------
# MODEL PERFORMANCE
# -------------------------
elif page == "📊 Model Performance":

    st.title("📊 Model Performance")

    st.table({
        "Model": [
            "Logistic Regression",
            "Decision Tree",
            "Random Forest"
        ],
        "Accuracy": [
            "92.45%",
            "95.75%",
            "96.70%"
        ]
    })

# -------------------------
# ABOUT PAGE
# -------------------------
elif page == "ℹ️ About Project":

    st.title("ℹ️ About Project")

    st.write("""
### Project Title

AI-Based Phishing Website Detection Using Machine Learning

### Dataset

UCI Phishing Websites Dataset

- Records : 11,055
- Features : 30

### Algorithms Used

- Logistic Regression
- Decision Tree
- Random Forest

### Best Model

Random Forest

### Accuracy

96.70%

### Software Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- VS Code
""")