# Aryan Khedkar's Portfolio Website

## Description
A professional portfolio website built with Dash to showcase my skills, projects, certifications, and writing. This site highlights my expertise in data analytics, business intelligence, machine learning projects.

## Features
- **Multi-Page Layout:** Home, Projects, Writing, About & Contact.
- **Responsive Design:** Optimized for desktops, tablets, and mobile devices.
- **Interactive Visualizations:** Utilizing Plotly for dynamic charts.
- **Project Attachments:** PDFs, images, and code repositories linked for detailed insights.
- **Contact Form:** Allowing visitors to reach out directly.

## Technologies Used
- **Frontend:** HTML5, CSS3, JavaScript
- **Backend:** Python, Dash, Dash Bootstrap Components
- **Visualization:** Plotly
- **Version Control:** Git, GitHub

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/aryankhedkar/my_portfolio.git
    cd my_portfolio
    ```

2. **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application:**
    ```bash
    python app.py
    ```
    Open your browser and navigate to `http://127.0.0.1:8050/` to view the portfolio website.

## Usage
- **Home:** Introduction and quick overview.
- **Projects:** Detailed descriptions of key projects, including Arduino projects.
- **Writing:** Articles and essays I've authored.
- **About & Contact:** Learn more about me and get in touch.

## Contributing
Feel free to fork the repository and submit pull requests for improvements or additional features.

## License
This project is licensed under the MIT License.

## Contact
- **LinkedIn:** [Aryan Khedkar](https://www.linkedin.com/in/aryankhedkar0000/)
- **GitHub:** [aryankhedkar](https://github.com/aryankhedkar)
- **YouTube:** [Aryan Khedkar](https://www.youtube.com/@aryankhedkar0000)

Structure

my_portfolio/
  ├── app.py                <-- (Module 1) Entry point for Dash app
  ├── pages/
  │   ├── home.py           <-- (Module 2) Home Page
  │   ├── projects.py       <-- (Module 3) Projects Page
  │   ├── writing.py        <-- (Module 4) Writing Page
  │   ├── about_contact.py  <-- (Module 5) About & Contact Page
  ├── assets/
  │   ├── styles.css        <-- (Module 6) Custom CSS
  └── README.py             <-- Setup and deployment instructions



