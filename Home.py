import streamlit as st
import os

# Updated Streamlit Page Configuration
st.set_page_config(page_title="Gradify AI", page_icon='src/Logo College.png', layout='wide', initial_sidebar_state="expanded")

# Load CSS file for styling
st.markdown('<style>' + open('./src/style.css').read() + '</style>', unsafe_allow_html=True)

from streamlit_lottie import st_lottie
from st_on_hover_tabs import on_hover_tabs

# Importing Menu Pages
from menu.About import main as about_page
from menu.AI_Lens import main as ai_lens_page
from menu.Ask_To_PDF import main as ask_to_pdf_page
from menu.ATS import main as ats_page
from menu.Prompt_Examples import main as prompt_examples_page
from menu.Resume_Analyser import main as resume_analyser_page
from menu.User import main as user_page
from menu.Contest_Calendar import main as contest_calendar
from menu.Projects import main as projects_page
from menu.Job_Tracker import main as job_tracker

# Define Theme Colors
themes = {
    "light": {
        "base": "light",
        "backgroundColor": "#F9FAFB",
        "primaryColor": "#629DFF",  # Using Medium Blue
        "secondaryBackgroundColor": "#627AFF",  # Dark Blue
        "textColor": "#333333"
    },
    "dark": {
        "base": "dark",
        "backgroundColor": "#1E1E1E",
        "primaryColor": "#63D3FF",  # Light Blue for contrast in dark theme
        "secondaryBackgroundColor": "#3E76E0",  # Flame Blue from logo
        "textColor": "#FFFFFF"
    }
}

# Initialize session state for theme
if "current_theme" not in st.session_state:
    st.session_state.current_theme = "light"

# Function to Change Theme
def change_theme():
    current_theme = st.session_state.current_theme
    new_theme = "dark" if current_theme == "light" else "light"
    st.session_state.current_theme = new_theme
    apply_theme()
    st.rerun()

# Apply Theme Changes Function
def apply_theme():
    theme_settings = themes[st.session_state.current_theme]
    for key, value in theme_settings.items():
        st._config.set_option(f'theme.{key}', value)

# Home Page Function
def home():
    # Add gradient animation style for the title and line below
    st.markdown("""
        <style>
        @keyframes gradient {
            0% { color: #3E76E0; }
            25% { color: #6B8DD6; }
            50% { color: #8D6AD6; }
            75% { color: #C56AD6; }
            100% { color: #3E76E0; }
        }

        @keyframes line-gradient {
            0% { border-color: #3E76E0; }
            25% { border-color: #6B8DD6; }
            50% { border-color: #8D6AD6; }
            75% { border-color: #C56AD6; }
            100% { border-color: #3E76E0; }
        }

        .animated-title {
            font-size: 80px;  /* Increased size */
            font-weight: bold;
            text-align: center;
            background: linear-gradient(270deg, #3E76E0, #6B8DD6, #8D6AD6, #C56AD6);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            animation: gradient 5s infinite;
        }

        .animated-line {
            border: 0;
            height: 3px;
            margin: 20px auto;
            width: 50%;
            animation: line-gradient 5s infinite;
        }

        /* Gradient for the description */
        .gradient-description {
            font-size: 24px;  /* Increased font size */
            font-family: 'Arial', sans-serif; /* Matching the font with the rest */
            font-weight: bold;  /* Making the text bold */
            background: linear-gradient(90deg, #ff6a95, #ff7c01, #ff0000); /* Gradient of pink to red */
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            margin-left: 20px;  /* Ensuring it doesn't overlap with the image */
            padding-top: 30px;
        }

        .feature-box {
        border-radius: 15px; /* Curved corners for rectangular shape */
        padding: 15px;
        margin: 10px;
        background: linear-gradient(90deg, rgba(99,211,255,1) 0%, rgba(170,213,255,1) 100%);
        animation: gradient-feature 5s infinite alternate;
        transition: background 0.5s ease; /* Smooth transition for hover */
        text-align: center;
        font-size: 16px;
        color: #333;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Box shadow for a subtle lift */
    }

        /* Hover Effect - Animated Gradient */
        .feature-box:hover {
            background: linear-gradient(270deg, #ff6666, #ff99cc, #ffcc99);
            animation: gradient-hover 1s ease infinite; /* Starts animation when hovered */
            color: white; /* Change text color on hover */
            box-shadow: 0px 6px 10px rgba(0, 0, 0, 0.2); /* More pronounced shadow on hover */
        }

        /* Animation for Hover Gradient */
        @keyframes gradient-hover {
            0% {
                background: linear-gradient(90deg, #ff6666, #ff99cc, #ffcc99);
            }
            50% {
                background: linear-gradient(90deg, #ff99cc, #ffcc99, #ff6666);
            }
            100% {
                background: linear-gradient(90deg, #ffcc99, #ff6666, #ff99cc);
            }
        }

        @keyframes gradient-feature {
            0% { background: linear-gradient(90deg, rgba(99,211,255,1) 0%, rgba(170,213,255,1) 100%); }
            100% { background: linear-gradient(90deg, rgba(99,211,255,0.8) 0%, rgba(170,213,255,0.8) 100%); }
        }

        /* Dark Mode Text Adjustments */
        body[data-theme='dark'] p, body[data-theme='dark'] li {
            color: #FFFFFF;
        }

        </style>
    """, unsafe_allow_html=True)

    # Gradient animated title and line below
    st.markdown("<h1 class='animated-title'>Gradify AI</h1>", unsafe_allow_html=True)
    st.markdown("<hr class='animated-line'>", unsafe_allow_html=True)

    # Centered Image with Description on the right
    col1, col2 = st.columns([1, 1.5])
    with col1:
        try:
            st.image('src/pp.png', width=400, caption=None, use_column_width=False)
        except FileNotFoundError:
            st.error("Image file not found.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    
    with col2:
        # Gradient styled description with increased font size and bold text
        st.markdown(f"""
        <p class='gradient-description'>Gradify AI is your all-in-one AI-powered companion for navigating college life, providing students with intelligent tools and insights to excel academically, manage time effectively, and stay organized. Whether you're optimizing your resume for the job market, converting notes into polished PDFs, or tracking upcoming contests and scholarships, Gradify AI streamlines every aspect of your college journey. From helping you analyze documents with AI to guiding your project management, Gradify AI is designed to empower students with the tools they need to succeed and make the most of their academic experience...</p>
        """, unsafe_allow_html=True)

    # Key Features as individual animated boxes
    st.markdown("""
    <h4 style='text-align: center; color: #3E76E0;'>Key Features:</h4>
    <div style='display: flex; flex-wrap: wrap; justify-content: center;'>
        <div class='feature-box'><b>AI Lens:</b> Harness the power of AI to analyze documents and get quick insights.</div>
        <div class='feature-box'><b>Ask to PDF:</b> Instantly convert text or assignments into organized PDFs.</div>
        <div class='feature-box'><b>Resume Analyser:</b> Get detailed feedback to optimize your resume for ATS.</div>
        <div class='feature-box'><b>ATS:</b> Check your resume against industry-standard ATS systems.</div>
        <div class='feature-box'><b>Contest Calendar:</b> Track important academic contests and scholarships.</div>
        <div class='feature-box'><b>Job Tracker:</b> Monitor the status of your job applications.</div>
        <div class='feature-box'><b>Projects:</b> Manage your college projects with AI-backed suggestions.</div>
        <div class='feature-box'><b>Prompt Examples:</b> Get inspiration and guidance with AI-generated prompts.</div>
    </div>
    """, unsafe_allow_html=True)


# Main Function
def main():
    # Style Adjustments
    st.markdown("""
        <style>
            /* Remove padding for the entire page */
            .css-1y0tads, .block-container, .css-1lcbmhc {
                padding-top: 0px !important;
                padding-bottom: 0px !important; 
            }
            /* Footer styling */
            footer {
                text-align: center;
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: #3E76E0;
                color: white;
                padding: 10px 0;
            }
        </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        # Display logo and theme change button within the sidebar
        st.image('src/gradd.png', width=150)

        # Theme Toggle Button
        btn_face = "🌞 Light Mode" if st.session_state.current_theme == "dark" else "🌜 Dark Mode"
        if st.button(btn_face):
            change_theme()

        tabs = on_hover_tabs(
            tabName=['Home', 'AI Lens', 'Ask To PDF', 'Resume Analyser', 'ATS', 'Contest Calendar', 'Job Tracker', 'Projects', 'Prompt Examples', 'About', 'Account'], 
            iconName=['home', 'center_focus_weak', 'search', 'article', 'work', 'calendar_month', 'work_outline', 'work_outline', 'edit', 'info', 'account_circle'],  
            default_choice=0
        )

    menu = {
        'Home': home,
        'AI Lens': ai_lens_page,
        'Ask To PDF': ask_to_pdf_page,
        'Resume Analyser': resume_analyser_page,
        'ATS': ats_page, 
        'Contest Calendar': contest_calendar,
        'Job Tracker': job_tracker,
        'Projects': projects_page,
        'Prompt Examples': prompt_examples_page,
        'About': about_page,
        'Account': user_page,
    }
    
    menu[tabs]()

    # Footer
    st.markdown("<p style='text-align: center; color: #FFFFFF;'>- ©️Helvetica Project</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
