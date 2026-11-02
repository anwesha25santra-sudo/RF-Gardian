import streamlit as st


def load_css():
    st.markdown("""
    <style>

    /* Main App */
    .stApp {
        background-color: #0E1117;
        color: white;
    }

    /* Sidebar */
    section[data-testid="stSidebar"]{
        background-color:#161B22;
    }

    /* Metric Cards */
    div[data-testid="metric-container"]{
        background-color:#1B2430;
        border:1px solid #2D3748;
        padding:15px;
        border-radius:12px;
        box-shadow:0px 2px 8px rgba(0,0,0,0.25);
    }

    /* Buttons */
    .stButton>button{
        width:100%;
        border-radius:10px;
        background:#2563EB;
        color:white;
        border:none;
        padding:10px;
        font-weight:600;
    }

    .stButton>button:hover{
        background:#1D4ED8;
    }

    /* Headers */
    h1,h2,h3{
        color:white;
    }

    /* Divider */
    hr{
        border:1px solid #30363D;
    }

    </style>
    """, unsafe_allow_html=True)