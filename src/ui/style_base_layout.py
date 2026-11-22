
import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
            .stApp {
                background: #F3EEFF !important;
            }

            /* Home page cards */
            [data-testid="stColumn"] {
                background-color: #E9E0FF !important;
                padding: 2rem !important;
                border-radius: 22px !important;
                border: 1px solid #DDD0FA !important;
                box-shadow: 0 4px 15px rgba(96, 64, 174, 0.06);
                transition: all 0.25s ease;
            }

            [data-testid="stColumn"]:hover {
                border-color: #C5B2F0 !important;
                box-shadow: 0 8px 22px rgba(96, 64, 174, 0.12);
            }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background: #F3EEFF !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');

        :root {
            --lavender-bg: #F3EEFF;
            --lavender-card: #E9E0FF;
            --lavender-light: #F9F7FF;

            --primary: #7653C8;
            --primary-dark: #6040AE;
            --secondary: #A78BFA;

            --text: #29213D;
            --muted: #716783;
            --border: #DDD2F2;
        }

        /* Main background */
        .stApp {
            background: var(--lavender-bg) !important;
            font-family: 'Outfit', sans-serif !important;
            color: var(--text);
        }

        /* Main content */
        .block-container {
            padding-top: 1.8rem !important;
            padding-bottom: 3rem !important;
            max-width: 1250px;
        }

        /* Header */
        header[data-testid="stHeader"] {
            background: transparent !important;
        }

        /* Typography */
        h1, h2, h3, h4, h5, p, label {
            font-family: 'Outfit', sans-serif !important;
            color: var(--text);
        }

        h1 {
            font-size: 2.8rem !important;
            font-weight: 800 !important;
            line-height: 1.15 !important;
            letter-spacing: -1px !important;
        }

        h2 {
            font-size: 2rem !important;
            font-weight: 700 !important;
            letter-spacing: -0.5px !important;
        }

        h3 {
            font-size: 1.4rem !important;
            font-weight: 600 !important;
        }

        /* Buttons */
        .stButton > button,
        .stFormSubmitButton > button {
            border-radius: 11px !important;
            background-color: var(--primary) !important;
            color: white !important;
            padding: 10px 22px !important;
            min-height: 42px;
            border: 1px solid var(--primary) !important;
            font-family: 'Outfit', sans-serif !important;
            font-weight: 600 !important;
            transition: all 0.2s ease-in-out !important;
            box-shadow: 0 3px 8px rgba(118, 83, 200, 0.12);
        }

        .stButton > button:hover,
        .stFormSubmitButton > button:hover {
            background-color: var(--primary-dark) !important;
            border-color: var(--primary-dark) !important;
            transform: translateY(-2px);
            box-shadow: 0 6px 14px rgba(96, 64, 174, 0.22);
        }

        /* Secondary buttons */
        .stButton > button[kind="secondary"] {
            background-color: #E5D9FF !important;
            color: #6040AE !important;
            border: 1px solid #CDBAF5 !important;
            box-shadow: none !important;
        }

        .stButton > button[kind="secondary"]:hover {
            background-color: #D8C8FA !important;
        }

        /* Tertiary buttons */
        .stButton > button[kind="tertiary"] {
            background-color: #FFFFFF !important;
            color: #6040AE !important;
            border: 1px solid var(--border) !important;
            box-shadow: none !important;
        }

        /* Input fields */
        .stTextInput input,
        .stNumberInput input,
        .stTextArea textarea {
            background-color: #FFFFFF !important;
            border: 1px solid var(--border) !important;
            border-radius: 10px !important;
            color: var(--text) !important;
            font-family: 'Outfit', sans-serif !important;
            transition: all 0.2s ease;
        }

        .stTextInput input:focus,
        .stNumberInput input:focus,
        .stTextArea textarea:focus {
            border-color: var(--primary) !important;
            box-shadow: 0 0 0 3px rgba(118, 83, 200, 0.10) !important;
        }

        /* Select boxes */
        [data-baseweb="select"] > div {
            background-color: #FFFFFF !important;
            border-radius: 10px !important;
            border-color: var(--border) !important;
        }

        /* Metrics */
        [data-testid="stMetric"] {
            background: var(--lavender-card) !important;
            padding: 1rem !important;
            border-radius: 16px !important;
            border: 1px solid var(--border) !important;
            box-shadow: 0 3px 12px rgba(96, 64, 174, 0.05);
            transition: all 0.2s ease;
        }

        [data-testid="stMetric"]:hover {
            transform: translateY(-2px);
            box-shadow: 0 7px 16px rgba(96, 64, 174, 0.10);
        }

        [data-testid="stMetricLabel"] {
            color: var(--muted) !important;
            font-weight: 500 !important;
        }

        [data-testid="stMetricValue"] {
            color: var(--primary-dark) !important;
            font-weight: 700 !important;
        }

        /* Containers */
        [data-testid="stVerticalBlockBorderWrapper"] {
            background: var(--lavender-light);
            border: 1px solid var(--border);
            border-radius: 16px;
        }

        /* Tables */
        [data-testid="stDataFrame"],
        [data-testid="stTable"] {
            border-radius: 12px;
            border: 1px solid var(--border);
            overflow: hidden;
            background: white;
        }

        /* Alerts */
        [data-testid="stAlert"] {
            border-radius: 12px;
            border: 1px solid var(--border);
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background: #E5DBF7 !important;
            border-right: 1px solid var(--border);
        }

        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {
            color: var(--primary-dark) !important;
        }

        /* Tabs */
        .stTabs [data-baseweb="tab"] {
            font-family: 'Outfit', sans-serif !important;
            font-weight: 600 !important;
        }

        .stTabs [aria-selected="true"] {
            color: var(--primary) !important;
        }

        /* Expanders */
        [data-testid="stExpander"] {
            border: 1px solid var(--border);
            border-radius: 12px;
            background: white;
        }

        /* Images */
        [data-testid="stImage"] img {
            border-radius: 14px;
        }

        /* Divider */
        hr {
            border-color: var(--border) !important;
        }

        /* Responsive */
        @media (max-width: 700px) {
            .block-container {
                padding: 1rem !important;
            }

            h1 {
                font-size: 2rem !important;
            }

            h2 {
                font-size: 1.5rem !important;
            }

            [data-testid="stColumn"] {
                padding: 1rem !important;
                border-radius: 16px !important;
            }

            [data-testid="stMetric"] {
                padding: 0.8rem !important;
            }
        }

        </style>
    """, unsafe_allow_html=True)
