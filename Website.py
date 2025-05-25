import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="OM SAI TELECOM & SECURITY SOLUTIONS", layout="wide")

st.markdown("""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-VZZYFER088"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-VZZYFER088');
</script>
""", unsafe_allow_html=True)


# Load Lottie animation
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_banner = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_HpFqiS.json")

# --- DARK THEME STYLING ---
st.markdown("""
    <style>
    body, .main {
        background-color: #121212;
        color: #ffffff;
    }
    h1, h2, h3, h4, h5 {
        color: #ffffff;
    }
    .stTabs [role="tab"] {
        font-size: 18px;
        padding: 10px 20px;
        margin-right: 5px;
        background-color: #2a2a2a;
        border-radius: 5px 5px 0 0;
        color: #cfcfcf;
        font-weight: bold;
    }
    .stTabs [aria-selected="true"] {
        background-color: #256D85;
        color: white;
    }
    input, textarea {
        background-color: #1e1e1e !important;
        color: #ffffff !important;
        border: 1px solid #444 !important;
    }
    button {
        background-color: #256D85 !important;
        color: white !important;
        border: none;
        padding: 10px;
        border-radius: 5px;
    }
    button:hover {
        background-color: #194759 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
       st.markdown("""
    <div style="background-color:#001F3F; padding: 30px 20px; border-radius: 10px; text-align: center;">
        <marquee behavior="scroll" direction="left" scrollamount="15" style="white-space: nowrap;">
            <span style="font-size: 2.5em; color: #58A6FF; font-style: italic; font-weight: bold; vertical-align: middle; margin-right: 40px;">
                OM SAI TELECOM & SECURITY SOLUTIONS
            </span>
            <span style="font-size: 1.4em; color: #cfcfcf; font-style: italic; vertical-align: middle;">
                Trusted experts in CCTV, security, and IT services — protecting homes & businesses since 2012.
            </span>
        </marquee>
    </div>
""", unsafe_allow_html=True)


    with col2:
        st_lottie(lottie_banner, height=200)

st.markdown("---")

# --- NAVIGATION ---
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "🛠️ Services", "👨‍💼 About", "📞 Contact"])

# --- HOME TAB ---
with tab1:
    st.subheader("Welcome to OM SAI TELECOM & SECURITY SOLUTIONS")
    st.write("Your trusted partner for advanced security systems and tech solutions in your area.")
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.header("Why Choose Us?")
        st.write("""
        - ✅ 10+ years of experience  
        - ✅ Certified technicians  
        - ✅ Fast and affordable installations  
        - ✅ Trusted by businesses and homeowners
        """)
    with col2:
        st.image("images/cctv.jpg", caption="CCTV Solutions", use_container_width=True)

    st.markdown("---")
    st.subheader("✨ Testimonials")
    st.success("“Fast and reliable CCTV service! Highly recommended.” – A local shop owner")
    st.success("“Professional setup of intercom and biometric system at our school.” – Principal, City School")

# --- SERVICES TAB ---
with tab2:
    st.title("🛠️ Our Services")
    st.write("Explore our wide range of security and technology services.")
    st.markdown("---")

    services = [
        {"title": "📹 CCTV Installation", "desc": "24/7 surveillance solutions.", "image": "images/cctv.jpg"},
        {"title": "📼 DVR/NVR Setup", "desc": "High-def recording systems.", "image": "images/dvr.jpg"},
        {"title": "🧬 Biometric Attendance", "desc": "Fingerprint & facial recognition systems.", "image": "images/biometric.jpg"},
        {"title": "🚪 Door Access Control", "desc": "Smart control for entry points.", "image": "images/door_access.jpg"},
        {"title": "☎️ Intercom System", "desc": "Two-way video/audio systems.", "image": "images/intercom.jpg"},
        {"title": "🔥 Fire Alarm System", "desc": "Fire and smoke detection.", "image": "images/fire_alarm.jpg"},
        {"title": "💻 Computer Services", "desc": "Sales, repair, and maintenance.", "image": "images/computer.jpg"},
    ]

    for service in services:
        with st.container():
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(service["image"], use_container_width=True)
            with col2:
                st.subheader(service["title"])
                st.write(service["desc"])
            st.markdown("---")

# --- ABOUT TAB ---
with tab3:
    st.title("👨‍💼 About Us")
    st.write("---")
    st.write("""
        **OM SAI TELECOM & SECURITY SOLUTION** is your local security and IT partner, providing expert installations and service since 2012.
    """)
    st.write("""
    #### 💡 Our Vision:
    To be the most reliable name in security and technology in our region.

    #### 👨‍🔧 Our Team:
    A team of certified engineers and installers who care about safety and quality.

    #### 🏆 Achievements:
    - 1000+ successful installations  
    - Partnered with local institutions  
    - Known for prompt after-sales service
    """)

# --- CONTACT US ---
with tab4:
    st.title("📞 Contact Us")
    st.write("---")
    st.subheader("We’d love to hear from you!")

    st.markdown("""
    📍 **Location**: Shop No-3, Tare Compound, 1st Floor, Behind Shree Krishna Hotel, Dahisar Check Naka, Dahisar East - Mumbai 400068  
    📞 **Phone**: +91-7021636329  
    📧 **Email**: abhishekyadavy13@gmail.com  
    🕒 **Working Hours**: Mon–Sat, 9:00 AM – 7:00 PM
    """)

    st.write("##")
    st.subheader("Send a Message")

    contact_form = """
    <form action="https://formsubmit.co/dmp.technologies1@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="How can we help you?" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

    st.markdown("""
   <style>
    form {
        display: flex;
        flex-direction: column;
        gap: 10px;
        max-width: 500px;
        background-color: transparent;
        padding: 20px;
        border-radius: 10px;
    }
    input, textarea {
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #999;
        background-color: #f0f0f0 !important;  /* Light gray background */
        color: #000000 !important;             /* Black text */
    }
    button {
        background-color: #256D85;
        color: white;
        padding: 10px;
        border-radius: 5px;
        border: none;
    }
    button:hover {
        background-color: #194759;
    }
</style>
                
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.markdown("© 2025 **OM SAI TELECOM & SECURITY SOLUTIONS** | Designed with ❤️ in India", unsafe_allow_html=True)


#python -m streamlit run Website.py 