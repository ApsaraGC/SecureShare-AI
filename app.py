import streamlit as st
from scanner import scan_text
from encryption import encrypt_file
import os
from datetime import datetime

st.set_page_config(
    page_title="SecureShare AI",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 SecureShare AI")
st.write("A secure document sharing prototype for detecting sensitive data and encrypting files.")

os.makedirs("uploads", exist_ok=True)
os.makedirs("encrypted", exist_ok=True)

menu = st.sidebar.radio(
    "Navigation",
    ["Home", "Upload & Scan", "Audit Logs", "About"]
)

if menu == "Home":
    st.header("Welcome to SecureShare AI")
    st.write("""
    SecureShare AI helps users upload documents, detect sensitive information,
    calculate risk level, and encrypt files before sharing.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Security Feature", "Encryption")

    with col2:
        st.metric("Detection", "Email & Phone")

    with col3:
        st.metric("Status", "Prototype")

elif menu == "Upload & Scan":
    st.header("Upload and Scan Document")

    uploaded_file = st.file_uploader(
        "Upload a text file",
        type=["txt"]
    )

    if uploaded_file:
        filepath = os.path.join("uploads", uploaded_file.name)

        with open(filepath, "wb") as f:
            f.write(uploaded_file.read())

        st.success("File uploaded successfully.")

        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

        st.subheader("Document Preview")
        st.text_area("File Content", text, height=150)

        findings = scan_text(text)

        st.subheader("Sensitive Data Scan")

        if findings:
            for item in findings:
                st.warning(item)

            risk_score = min(len(findings) * 40, 100)

            if risk_score >= 80:
                risk_level = "HIGH"
                st.error("Risk Level: HIGH")
            elif risk_score >= 40:
                risk_level = "MEDIUM"
                st.warning("Risk Level: MEDIUM")
            else:
                risk_level = "LOW"
                st.success("Risk Level: LOW")

            st.metric("Risk Score", f"{risk_score}%")

        else:
            risk_score = 0
            risk_level = "LOW"
            st.success("No sensitive information detected.")
            st.metric("Risk Score", "0%")

        password = st.text_input(
            "Set sharing password",
            type="password"
        )

        if password:
            st.success("Password protection enabled.")

        if st.button("Encrypt File"):
            encrypted_file = encrypt_file(filepath)

            st.success("File encrypted successfully.")
            st.info(f"Encrypted file created: {encrypted_file}")

            with open("logs.txt", "a", encoding="utf-8") as log:
                log.write(
                    f"{datetime.now()} | Uploaded: {uploaded_file.name} | Risk: {risk_level} | Score: {risk_score}% | Encrypted\n"
                )

elif menu == "Audit Logs":
    st.header("Audit Logs")

    if os.path.exists("logs.txt"):
        with open("logs.txt", "r", encoding="utf-8") as log:
            logs = log.read()

        if logs:
            st.text(logs)
        else:
            st.info("No logs available yet.")
    else:
        st.info("No logs available yet.")

elif menu == "About":
    st.header("About This Project")
    st.write("""
    This project demonstrates secure document sharing concepts:
    
    - Sensitive data detection
    - Risk assessment
    - Password-protected sharing concept
    - File encryption
    - Audit logging
    """)