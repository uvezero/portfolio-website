import streamlit as st
from streamlit_option_menu import option_menu
import base64

# Set page config for wide layout
st.set_page_config(
    page_title="Juan López-Ríos Portfolio",
    page_icon="👾",
    layout="wide",
)

# Horizontal menu with option 2 (removing the sidebar navigation)
selected = option_menu(
    menu_title=None,  # No menu title
    options=["Home", "Projects", "Contact"],  # Menu options
    icons=["house", "book", "envelope"],  # Menu icons
    menu_icon="cast",  # Default menu icon
    default_index=0,  # Default selected menu item
    orientation="horizontal",  # Horizontal layout
)

# Functions for the content of each page
def home():
    # CSS styles file
    with open("styles/main.css") as f:
        st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Profile image file
    with open("assets/profile-pic.jpeg", "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()

    # PDF CV file
    with open("assets/Juan-Lopez-Rios.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    # Top title
    st.write(f"""<div class="title"><strong>Hi! My name is</strong> Juan López-Ríos 👋</div>""", unsafe_allow_html=True)

    # Profile image with animated circular shape
    st.write(f"""
    <div class="container">
        <div class="box">
            <div class="spin-container">
                <div class="shape">
                    <div class="bd">
                        <img src="{img}" alt="Juan Lopez-Rios" style="border-radius: 50%;">
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Subtitle
    st.write(f"""<div class="subtitle" style="text-align: center;">Theoretical physicist with a passion for Machine Learning and Data Science</div>""", unsafe_allow_html=True)

    # Social Icons
    social_icons_data = {
        "LinkedIn": ["https://www.linkedin.com/in/lopez-rios", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub": ["https://github.com/uvezero", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"],
        "Twitter": ["https://x.com/juanlrios22", "https://cdn-icons-png.flaticon.com/512/733/733579.png"],
        "Medium": ["https://medium.com/@juanlopezriosdecastro", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Medium_logo_Monogram.svg/1200px-Medium_logo_Monogram.svg.png"]
    }

    social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}' width='30'></a>" for platform in social_icons_data]

    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_icons_html)}
    </div>""", unsafe_allow_html=True)

    # About me section
    st.subheader("About Me")
    st.write("""
    - 🧑‍💻 I am a **MSci Theoretical Physics graduate from UCL**
    - 🛩️ prev: ML Intern at [Encord](https://encord.com/author/juan-lopez-rios-de-castro/), built AI-powered chatbot and worked on SAM model improvements.
    - ❤️ I am passionate about **Machine Learning/Deep Learning, MLOps, Data, Computer Vision**.
    - 🎬 Also love cinema and writing reviews about TV shows or films.
    - 📫 How to reach me: juanlopezriosdecastro@gmail.com
    - 🏠 London/Madrid
    """)

    # Download button for CV
    st.download_button(
        label="📄 Download my CV",
        data=pdf_bytes,
        file_name="Juan_CV.pdf",
        mime="application/pdf",
    )



def projects():
    st.title("Projects")

    # CSS for general styling and buttons
    st.markdown("""
    <style>
    .spacer {
        margin-top: 200px;
        margin-bottom: 100px;
    }

    /* First Project Read More/Read Less */
    .content-wrapper-1 {
        max-height: 0;
        overflow: hidden;
        transition: max-height 0.5s ease-in-out;
    }

    input[type="checkbox"]#toggle-1 {
        display: none;
    }

    input[type="checkbox"]#toggle-1:checked ~ .content-wrapper-1 {
        max-height: 500px; /* Adjust this value if the text is longer */
    }

    input[type="checkbox"]#toggle-1:checked ~ label span::before {
        content: "Read Less";
    }

    /* Second Project Read More/Read Less */
    .content-wrapper-2 {
        max-height: 0;
        overflow: hidden;
        transition: max-height 0.5s ease-in-out;
    }

    input[type="checkbox"]#toggle-2 {
        display: none;
    }

    input[type="checkbox"]#toggle-2:checked ~ .content-wrapper-2 {
        max-height: 500px; /* Adjust this value if the text is longer */
    }

    input[type="checkbox"]#toggle-2:checked ~ label span::before {
        content: "Read Less";
    }
    
    /* Third Project Read More/Read Less */
    .content-wrapper-3 {
        max-height: 0;
        overflow: hidden;
        transition: max-height 0.5s ease-in-out;
    }

    input[type="checkbox"]#toggle-3 {
        display: none;
    }

    input[type="checkbox"]#toggle-3:checked ~ .content-wrapper-3 {
        max-height: 500px; /* Adjust this value if the text is longer */
    }

    input[type="checkbox"]#toggle-3:checked ~ label span::before {
        content: "Read Less";
    }

    label span::before {
        content: "Read More";
    }

    label span {
        background-color: #1e90ff;
        color: white;
        padding: 8px 16px;
        border-radius: 5px;
        cursor: pointer;
        display: inline-block;
        font-size: 14px;
        font-weight: bold;
        text-align: center;
    }

    label span:hover {
        background-color: #005f99;
    }

    .button-container {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-top: 20px;
    }

    .button {
        background-color: #007bff;
        color: white;
        padding: 12px 30px;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
        text-decoration: none;
        cursor: pointer;
    }

    .button-blue {
        background-color: #20c997;
    }

    .button:hover, .button-blue:hover {
        background-color: #005f99;
    }

    /* Styling for hacker-style smaller green tags */
    .tags {
        background-color: #1a1a1a;
        color: #00ff00; /* Hacker-style green */
        padding: 2px 6px; /* Smaller padding */
        border-radius: 3px; /* Smaller border-radius */
        display: inline-block;
        margin-right: 8px; /* Adjust margin for smaller spacing */
        font-size: 12px; /* Smaller font size */
        font-family: 'Courier New', Courier, monospace; /* Hacker-style font */
    }

    .tags-container {
        margin-bottom: 20px;
    }
    
    </style>
    """, unsafe_allow_html=True)

    # First Project
    st.markdown("""
        ### Time-dependent Problems: Solving the Heat Equation Using Finite Difference Methods
    """)

    st.image("project_1.png", width=600, caption="Heat Equation Project")

    # Highlights section
    st.markdown("""
    #### Highlights:
    - Solved a time-dependent heat conduction problem using explicit and implicit finite difference methods.
    - Demonstrated the use of parallel computing with CUDA for high-performance simulations.
    - Optimized performance using HPC techniques, leveraging Numba for CPU acceleration and CUDA for GPU acceleration.
    - Generated 2D and 3D visualizations to illustrate temperature distribution and evolution over time.
    """)

    # Tags section
    st.markdown("##### Tags:")
    st.markdown("""
    <div class="tags-container">
        <span class="tags">High-Performance Computing (HPC)</span>
        <span class="tags">Parallel Computing</span>
        <span class="tags">Numerical Methods</span>
        <span class="tags">Finite Difference Method (FDM)</span>
        <span class="tags">Python</span>
        <span class="tags">Computational Physics</span>
        <span class="tags">CUDA Programming</span>
        <span class="tags">Numba</span>
        <span class="tags">Scientific Computing</span>
    </div>
    """, unsafe_allow_html=True)
    # Read More / Read Less for the first project
    st.markdown("""
    <div>
        <input type="checkbox" id="toggle-1">
        <div class="content-wrapper-1">
            <p>
            In this project, I developed a numerical solution for a two-dimensional heat conduction problem using both explicit and implicit finite difference methods. By leveraging high-performance computing techniques, including Numba for CPU parallelization and CUDA for GPU acceleration, I optimized the performance and accuracy of the simulations. This approach allowed me to efficiently compute the temperature evolution over time, achieving precision up to 7 decimal places. Additionally, I analyzed the stability and convergence of the methods, and visualized the results using 2D and 3D plots to illustrate the dynamic behavior of the system.
            </p>
        </div>
        <label for="toggle-1"><span></span></label>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### Explore More:")


    # Create the button container using HTML
    st.markdown("""
    <div class="button-container">
        <a href="https://github.com/uvezero/High_Performance_Computing/blob/main/Assignment_4.pdf" target="_blank">
            <div class="button">GitHub Repo</div>
        </a>
    </div>
    """, unsafe_allow_html=True)

    # Add spacer between projects
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    # Second Project
    st.markdown("""
        ### Customer Churn Prediction System with Flask API and Solara Interface
    """)

    # Image for the second project
    st.image("api.svg", width=600, caption="Customer Churn Prediction System")

    # Highlights section for the second project
    st.markdown("""
    #### Highlights:
    - Developed a Flask API to handle both single and batch predictions.
    - Implemented MLflow for tracking experiments, managing model lifecycle, and ensuring reproducibility in the MLOps cycle.
    - Created a Solara-based web interface for interactive churn prediction and SHAP visualizations.
    - Contributed to the open-source Solara library by enhancing its web interface capabilities.
    """)

    # Tags section for the second project
    st.markdown("##### Tags:")
    st.markdown("""
    <div class="tags-container">
        <span class="tags">Flask</span>
        <span class="tags">Solara</span>
        <span class="tags">Machine Learning</span>
        <span class="tags">MLflow</span>
        <span class="tags">SHAP</span>
        <span class="tags">MLOps</span>
        <span class="tags">API Development</span>
        <span class="tags">Docker</span>
        <span class="tags">Python</span>
    </div>
    """, unsafe_allow_html=True)
    # Read More / Read Less for the second project
    st.markdown("""
    <div>
        <input type="checkbox" id="toggle-2">
        <div class="content-wrapper-2">
            <p>
            In this project, I developed a machine learning solution to predict customer churn using a CatBoost model, with MLflow for experiment tracking and model versioning. The solution integrates a Flask API to serve predictions and a Solara web interface for interactive user engagement, enabling both single and batch predictions. The interface provides SHAP-based visualizations for explaining feature importance. Additionally, I contributed to Solara’s open-source ecosystem, improving CSV file handling for data science applications. The entire project is Dockerized for efficient deployment.
            </p>
        </div>
        <label for="toggle-2"><span></span></label>
    </div>
    """, unsafe_allow_html=True)

    st.header("Video Demo")
    col1, col2, col3 = st.columns([1, 2, 1])  # Adjust the width ratios as needed
    with col2:
        video_file = open('video.webm','rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

    st.markdown("#### Explore More:")
    
    # Create the button container using HTML
    st.markdown("""
    <div class="button-container">
        <a href="https://github.com/uvezero/churn_prediction" target="_blank">
            <div class="button">GitHub Repo</div>
        </a>
        <a href="https://your-web-app-link" target="_blank">
            <div class="button button-blue">Web App</div>
        </a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>Web-app coming soon...</h1>", unsafe_allow_html=True)
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    
    # Third Project
    st.markdown("""
        ### Machine Learning Tools for biocatalysis
    """)

    # Image for the third project
    st.image("Protein_RASA1_PDB_1wer.png", width=600, caption="Customer Churn Prediction System")

    # Highlights section for the second project
    st.markdown("""
    #### Highlights:
    - Investigated new features and developed a new dataset that improved model accuracy and predictive performance
    - Employed advanced feature selection methods like LASSO, Mutual Information, and Random Forest feature importance to enhance dataset quality.
    - Performed equilibrium minimizations to optimize ligand geometry and improve stability for accurate protein-ligand interaction predictions.
    - Achieved a distinction honours for my dissertation based on this project
    - Improved ligand identification methods to prevent oncogenic mutations in the RAS protein.
    """)

    # Tags section for the second project
    st.markdown("##### Tags:")
    st.markdown("""
    <div class="tags-container">
        <span class="tags">Machine Learning</span>
        <span class="tags">Random Forest</span>
        <span class="tags">Support Vector Regression</span>
        <span class="tags">Deep Neural Networks</span>
        <span class="tags">Feature Selection</span>
        <span class="tags">LASSO</span>
        <span class="tags">Mutual Information</span>
        <span class="tags">Computational Biophysics</span>
        <span class="tags">PyMOL</span>
        <span class="tags">Equilibrium Minimization</span>
        <span class="tags">Protein-Ligand Interactions</span>
        <span class="tags">TabNet</span>
    </div>
    """, unsafe_allow_html=True)
    # Read More / Read Less for the second project
    st.markdown("""
    <div>
        <input type="checkbox" id="toggle-3">
        <div class="content-wrapper-3">
            <p>
            This study applied multiple machine learning models, including Random Forest, SVR, and DNN, to predict ligands capable of restoring the function of mutated Ras proteins. Feature selection techniques such as LASSO and Mutual Information were used to refine the dataset, leading to a notable improvement in model accuracy, with a 0.5 increase in Pearson correlation. PyMOL was employed to visualize and validate the structural interactions between ligands and Ras proteins, ensuring spatial accuracy and enhancing the reliability of ligand predictions.
            </p>
        </div>
        <label for="toggle-3"><span></span></label>
    </div>
    """, unsafe_allow_html=True)


    st.markdown("#### Explore More:")
    
    # Create the button container using HTML
    st.markdown("""
    <div class="button-container">
        <a href="https://github.com/your-repo-link" target="_blank">
            <div class="button">GitHub Repo</div>
        </a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>Git repo coming soon...</h1>", unsafe_allow_html=True)






# Function to display the contact page
def contacts():
    st.write("## Contact Me")
    st.write("""
        - 📧 Email: juanlopezriosdecastro@gmail.com
        - 📱 LinkedIn: [Connect with me](https://www.linkedin.com/in/lopez-rios)
        - 🐦 Twitter: [Follow me on Twitter](https://x.com/juanlrios22)
    """)

# Render the page content based on the selected menu option
if selected == "Home":
    home()
elif selected == "Projects":
    projects()
elif selected == "Contact":
    contacts()