import streamlit as st

from scanner import scan_text

from encryption import encrypt_file

import os

st.title("SecureShare AI")

uploaded_file = st.file_uploader(
    "Upload Document",
    type=["txt"]
)

if uploaded_file:

    os.makedirs("uploads", exist_ok=True)

    filepath = f"uploads/{uploaded_file.name}"

    with open(filepath, "wb") as f:
        f.write(uploaded_file.read())

    st.success("File Uploaded")

    with open(filepath, "r") as f:
        text = f.read()

    findings = scan_text(text)

    st.subheader("Sensitive Data Scan")

    if findings:

      for item in findings:
        st.warning(item)

     # Risk Score
      risk_score = min(len(findings) * 40, 100)

      st.subheader("Risk Assessment")

      if risk_score < 40:
        st.success(f"Risk Score: {risk_score}%")

      elif risk_score < 80:
        st.warning(f"Risk Score: {risk_score}%")

      else:
        st.error(f"Risk Score: {risk_score}%")

    else:
      st.success("No sensitive information detected")

      st.success("Risk Score: 0%")
      
      col1, col2 = st.columns(2)

      with col1:
       st.metric("Risk Score", f"{risk_score}%")

      with col2:
       if risk_score >= 80:
        st.error("HIGH")
       elif risk_score >= 40:
        st.warning("MEDIUM")
       else:
        st.success("LOW")
    if st.button("Encrypt File"):

        encrypted_file = encrypt_file(filepath)

        st.success("File Encrypted Successfully")

        st.write(encrypted_file)
        
    