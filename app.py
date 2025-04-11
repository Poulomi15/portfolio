import streamlit as st
from PIL import Image

# ---- PAGE CONFIG ----
st.set_page_config(page_title="My Portfolio", page_icon=":wave:", layout="wide")

# ---- LOAD ASSETS ----
#profile_pic = Image.open("your_profile_photo.jpg")  # Replace with your photo file

# ---- HEADER SECTION ----
with st.container():
    left_col, right_col = st.columns([1, 3])
    #with left_col:
        #st.image(profile_pic, width=150)
    with right_col:
        st.title("Poulomi Chowdhury")
        st.write("📍 Kolkata, India | 📧 chowdhurypoulomi7@gmail.com | 📱 +91-8017739221")
        st.write("🔗 [LinkedIn](https://www.linkedin.com/in/poulomichowdhury-business-analyst-trainee/) | [GitHub](https://github.com/Poulomi15) | [Portfolio](https://yourwebsite.com)")

# ---- SUMMARY ----
st.write("---")
st.subheader("👋 Summary")
st.write("""
A passionate and detail-oriented professional with a strong foundation in [Your Domain e.g., Data Science, Software Development]. 
Skilled in [Skill 1], [Skill 2], and [Skill 3]. Eager to solve real-world problems and build impactful solutions.
""")

# ---- EDUCATION ----
st.write("---")
st.subheader("🎓 Education")
st.write("""
**MBA in Business Analytics & Data Science**  
Bengal Institute of Business Studies, Kolkata (2024–2026)

**B.Tech in Electronics & Communication Engineering**  
Camellia Institute Of Technology, Kolkata (2019–2023) | CGPA: 8.96
""")

# ---- EXPERIENCE ----
st.write("---")
st.subheader("💼 Experience")
st.write("""
**Software Developer Intern**  
Company Name | June 2023 – August 2023  
- Developed REST APIs using Flask and Django  
- Worked with MySQL databases and performed CRUD operations  

**Web Development Intern**  
Another Company | Jan 2023 – March 2023  
- Built responsive websites using HTML, CSS, JS  
- Collaborated with design and backend teams
""")

# ---- SKILLS ----
st.write("---")
st.subheader("🛠️ Skills")
st.write("""
- Programming: Python, SQL, JavaScript  
- Tools: Power BI, Excel, Tableau, Git  
- Web: HTML, CSS, React, Flask, Django  
- Concepts: Machine Learning, Data Analysis, Deep Learning
""")

# ---- PROJECTS ----
st.write("---")
st.subheader("📂 Projects")
st.write("""
**1. News Summarization & Text-to-Speech App** – Akaike Technologies Internship  
- Built an end-to-end application for summarizing news articles and converting text to speech.

**2. Career Path Recommendation System**  
- Designed a system using psychometric data to suggest suitable career paths for Class 9–10 students.

**3. Resume Parser Web App**  
- Developed a Streamlit-based app to parse resumes and extract relevant information.

More on GitHub 👉 [github.com/yourusername](https://github.com/yourusername)
""")

# ---- CERTIFICATIONS ----
st.write("---")
st.subheader("📜 Certifications")
st.write("""
- IBM: Machine Learning with Python  
- IIT Kanpur SDP: Machine Learning with Python (Sept 2024 & Dec 2024)  
- Forage: Data Analytics Job Simulation  
- Udemy: Python and Flask Demonstrations  
- HackerRank: Problem Solving (Basic)
""")

# ---- ACHIEVEMENTS ----
st.write("---")
st.subheader("🏆 Achievements")
st.write("""
- Top 10 finalist in Codegoda 2022 (Unstop)  
- Winner in Codefiesta 2022  
- Participation in Jumpstart 2022  
""")

# ---- HOBBIES ----
st.write("---")
st.subheader("🎨 Hobbies")
st.write("""
Reading rom-com and self-help books 📚 | Exploring new tech 🧪 | Listening to music 🎧  
""")

# ---- FOOTER ----
st.write("---")
st.write("Made with ❤️ using Streamlit")
