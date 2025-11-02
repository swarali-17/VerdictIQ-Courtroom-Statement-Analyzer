import json
import streamlit as st
import sys
import os

# Add notebook directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'notebook')))

# Import the validator class from your backend file
from verdict_iq import WitnessStatementValidator


# Sample training data
sample_texts = [
    "I didn't see anything that night, but I know he was there.",
    "The defendant was observed entering the building at approximately 10:30 PM.",
    "I think I might have heard something, but I'm not sure.",
    "The victim was walking after the shooting.",
    "I saw the accused with my own eyes. He was holding the weapon."
]

# Initialize model only once using Streamlit's cache
@st.cache_resource
def load_validator():
    validator = WitnessStatementValidator()
    validator.train_model(sample_texts)
    return validator

validator = load_validator()

validator = load_validator()

# Initialize session state for storing results
if 'result' not in st.session_state:
    st.session_state.result = None
if 'show_json' not in st.session_state:
    st.session_state.show_json = False

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Main", "Documentation"])

# Page Routing
if page == "Main":
    #Title of the app
    st.title('⚖️ VerdictIQ - Intelligent Justice')

    #information/disclaimer
    st.info('VerdictIQ is an intelligent courtroom assistant that leverages Natural Language Processing (NLP) to analyze witness statements and flag them as valid, potentially suspicious, or suspicious. Designed to assist legal professionals and judicial systems, this tool brings AI into the courtroom to help detect inconsistencies, emotional cues, and patterns in testimonies. The system combines machine learning with legal reasoning to enhance fairness, accuracy, and efficiency in the justice process.')

    #Input area
    witness_statement = st.text_area('', placeholder='Type the full witness statement here...', height=200)
    
    # Analysis button
    if st.button("Analyze") and witness_statement.strip():
        # Store the full analysis result in session state
        st.session_state.result = validator.validate_statement(witness_statement)
        st.session_state.show_json = False  # Reset JSON display state
    
    # Display results if available
    if st.session_state.result is not None:
        verdict = st.session_state.result["Verdict"]
        reason = st.session_state.result["Reason"]
        
        # Display verdict based on type
        if verdict == "Valid Statement":
            st.success(f"**Verdict:** Valid  \n**Reason:** {reason}")
        elif verdict == "Potentially Suspicious":
            st.warning(f"**Verdict:** Potentially Suspicious  \n**Reason:** {reason}")  
        elif verdict == "Suspicious Statement":
            st.error(f"**Verdict:** Suspicious  \n**Reason:** {reason}")
        
        # Toggle JSON button (outside of the analyze button block)
        if st.button("Show JSON response"):
            st.session_state.show_json = not st.session_state.show_json
            
        # Display JSON if toggled on
        if st.session_state.show_json:
            st.json(st.session_state.result)  # This will display the dictionary as JSON


elif page == "Documentation":
    st.title("Welcome To VerdictIQ")
    st.markdown("""
    ### About VerdictIQ  
    VerdictIQ is a courtroom AI tool designed to analyze witness statements and flag them as:
    - ✅ **Valid**
    - ⚠️ **Potentially Suspicious**
    - ❌ **Suspicious**

    ### How It Works
    - Uses NLP and machine learning
    - Trained on annotated data (from Hugging Face's AUEB-NLP/lar-echr dataset )
    - Outputs a label for each input statement
    
    ### Features
    - Streamlit-based UI
    - Modular backend
    - Customizable classes
    
    ### How to Operate?
    - On the side navigation, click the main button to go to the analyser.
    - Input the witness statement
    - Click on the 'analyse' button to get the verdict
    - To check the full response of why it was detected so, click on the 'Show JSON response' button

    """)

