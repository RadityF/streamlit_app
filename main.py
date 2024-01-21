import streamlit as st

from pathlib import Path
from PIL import Image

#---Path settings --------------------------------
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume_file.pdf"
profile_pic = current_dir / "assets" / "foto_cv.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Raditya Fauzan"
PAGE_ICON = ":wave:"
NAME = "Raditya Fauzan"
DESCRIPTION = """
Undergraduate Mathematics Student at University of Indonesia.
"""
EMAIL = "raditya.fauzan05@gmail.com"
NUMBER = "081283033350"
HOME = "Jakarta Timur, Daerah Khusus Ibukota Jakarta, 13890"
SOCIAL_MEDIA = {
    "instagram": "https://www.instagram.com/ditdit._/",
    "LinkedIn": "https://www.linkedin.com/in/raditya-fauzan-333828254/",
    "GitHub": "https://github.com/RadityF",
    "Spotify": "https://open.spotify.com/user/jl46jm7n4fjcg1p6acrjbdel7?si=cbb41ed237504931",
}
PROJECTS = {
    '-'
}
# --- O ---
EXPERIENCE = [
    {
        "title": "Data Analyst,",
        "company": "Kimia Farma",
        "start_date": "January 2024",
        "end_date": "Ferbuary 2024",
        "description": "Developed and maintained software systems using Java and Spring Boot. Collaborated with cross-functional teams to design and implement new features. Improved system performance by optimizing database queries and implementing caching strategies."
    }]
education_info = """
**Bachelor in Mathematics**, Universitas Indonesia, Indonesia <div style="text-align: right">2023 - present</div>
"""

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.write("☎️",NUMBER)
    st.write("📍",HOME)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- About ---
st.write('\n')
st.subheader("About")
st.write('An undergraduate student majoring in Mathematics at the University of Indonesia, I am an individual dedicated to continually expanding my experience and knowledge. With a profound interest in the realms of both Mathematics and data, I actively seek opportunities to deepen my understanding and skills in these fields. Eager to embrace new challenges and learning experiences, I am poised to contribute effectively to the intersection of Mathematics and data exploration.')

# --- Education  ---
st.write('\n')
st.subheader("Education")
col1, col2 = st.columns([4,1])
with col1:
    st.write('**Bachelor in Mathematics**, Universitas Indonesia, Indonesia')
with col2:
    st.write('2023 - present')

col1, col2 = st.columns([4,1])
with col1:
    st.write('**High School in Science**, SMA Islam PB Soedirman, Indonesia')
    st.write(
    """
-  Graduated at acceleration program from PB Soedirman islamic high school majoring in science
-  Vice Chairman of the class
"""
)
with col2:
    st.write('2021 - 2023')

# --- WORK EXPERIENCE  ---
st.write('\n')
st.subheader("Work Experience")
col1, col2 = st.columns([5,2])
with col1:
    st.write('**Data Analyst intern**, Kimia Farma , Indonesia')
    st.write(
    """
- Implementing big data on Kimia Farma Sales Data
- Combining several sales datasets into one database for analysis regarding a problem
- Create a dashboard from Salicyl Brand sales data
- Create a dashboard from Kimia Farma sales data
"""
)
with col2:
    st.write('Jan 2024 - Feb 2024')

# --- Organization  ---
st.write('\n')
st.subheader("Organization")
col1, col2 = st.columns([5,2])
with col1:
    st.write('**intern at Variansi**, Himpunan Mahasiswa Departement Matematika , Indonesia')
    st.write(
    """
- Currently interning at Variansi, a bureau within the Himpunan Mahasiswa Departement Matematika
- Contribute in a work program focused on organizational leadership surveys during the internship.
- Responsible for conducting surveys and analyzing data to assess the progress of each bureau within the Mathematics Department
Student Association.
- Gaining hands?on experience in data analysis and obtaining valuable insights into the dynamics of student departmental
organizations
"""
)
with col2:
    st.write('Nov 2024 - Feb 2024')
# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL
- 📊 Data Visulization: matpolib, MS Excel
- 📚 Modeling: Logistic regression, linear regression, K-means clustering
- 🗄️ Databases: SQlite 
"""
)
