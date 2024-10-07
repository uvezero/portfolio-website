def projects():
    st.title("Projects")

    # Project title and image
    st.markdown("""
        ### Time-dependent Problems: Solving the Heat Equation Using Finite Difference Methods
    """)
    st.image("https://ethic.es/wp-content/uploads/2023/03/imagen.jpg", use_column_width=True, caption="Heat Equation Project")

    # Highlights section
    st.markdown("""
    #### Highlights:
    - Solved a time-dependent heat conduction problem using explicit and implicit finite difference methods.
    - Demonstrated the use of parallel computing with CUDA for high-performance simulations.
    - Optimized performance using HPC techniques, leveraging Numba for CPU acceleration and CUDA for GPU acceleration.
    - Generated 2D and 3D visualizations to illustrate temperature distribution and evolution over time.
    """)

    # Tags section
    st.markdown("**Tags:** `Scientific computing`, `High-performance computing`, `Data visualization`")

    # CSS for the Read More / Read Less button
    st.markdown("""
    <style>
    .content-wrapper {
        max-height: 0;
        overflow: hidden;
        transition: max-height 0.5s ease-in-out;
    }

    input[type="checkbox"] {
        display: none;
    }

    input[type="checkbox"]:checked ~ .content-wrapper {
        max-height: 500px; /* Adjust this value if the text is longer */
    }

    input[type="checkbox"]:checked ~ label span::before {
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
    </style>
    """, unsafe_allow_html=True)

    # HTML structure for the Read More / Read Less functionality
    st.markdown("""
    <div>
        <input type="checkbox" id="toggle">
        <div class="content-wrapper">
            <p>
            This project explores solving the heat equation using finite difference methods, focusing on both explicit and implicit schemes. We also utilized high-performance computing techniques such as GPU acceleration with CUDA and CPU acceleration with Numba to optimize simulation times. The project also includes visualizations that demonstrate the temperature evolution over time in both 2D and 3D representations.
            </p>
        </div>
        <label for="toggle"><span></span></label>
    </div>
    """, unsafe_allow_html=True)

    # Buttons section with consistent styling for GitHub and Web App
    st.markdown("#### Explore More:")

    # CSS for buttons
    st.markdown("""
    <style>
        .button-container {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-top: 20px;
        }
        .button {
            background-color: #ff4b4b;
            color: white;
            padding: 12px 30px;
            border-radius: 8px;
            text-align: center;
            font-weight: bold;
            cursor: pointer;
        }
        .button-blue {
            background-color: #1e90ff;
        }
    </style>
    """, unsafe_allow_html=True)

    # Create the button container using HTML
    st.markdown("""
    <div class="button-container">
        <a href="https://github.com/your-repo-link" target="_blank">
            <div class="button">GitHub Repo</div>
        </a>
        <a href="https://your-web-app-link" target="_blank">
            <div class="button button-blue">Web App</div>
        </a>
    </div>
    """, unsafe_allow_html=True)
