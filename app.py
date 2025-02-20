import streamlit as st
import pickle
import requests
import numpy as np

# Page Configuration
st.set_page_config(page_title="GOT Personality Matcher", layout="wide")

# Custom Styling for UI
st.markdown(
    """
    <style>
        /* Background */
        .stApp {
            background: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)), 
                        url('https://wallpapercave.com/wp/wp12401548.jpg');
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }
        /* Titles & Headers */
        .title {
            color: #FFD700;
            font-size: 50px;
            font-weight: bold;
            text-align: center;
            text-shadow: 2px 2px 10px rgba(255, 215, 0, 0.8);
        }
        .subheader {
            color: white;
            font-size: 22px;
            text-align: center;
            font-style: italic;
        }
        .character {
            color: #FFD700;
            font-size: 28px;
            font-weight: bold;
            text-shadow: 2px 2px 10px rgba(255, 215, 0, 0.8);
        }
        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: rgba(20, 20, 20, 0.9);
        }
        /* Buttons */
        .stButton>button {
            background-color: #444;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #FFD700;
            color: black;
            transform: scale(1.05);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Fetch API Data
api_data = requests.get("https://thronesapi.com/api/v2/Characters").json()

# Load Data
df = pickle.load(open("data.pkl", "rb"))
df = df.head(25)

# Character Name Adjustments
character_corrections = {
    "Jaime": "Jamie",
    "Lord Varys": "Varys",
    "Bronn": "Lord Bronn",
    "Sandor Clegane": "The Hound",
    "Robb Stark": "Rob Stark",
}
df["character"] = df["character"].replace(character_corrections)

# Function to Fetch Character Image
def fetch_image(name, api_data):
    for item in api_data:
        if item["fullName"] == name:
            return item["imageUrl"]
    return "https://via.placeholder.com/300"  # Default image if not found

# Function to Fetch Character Description
def fetch_description(name, api_data):
    for item in api_data:
        if item["fullName"] == name:
            return item.get("title", "No description available.")
    return "No description available."

# Title and Subtitle
st.markdown('<h1 class="title">⚔️ Game of Thrones Personality Matcher ⚔️</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="subheader">Find your closest personality match in the Seven Kingdoms</h3>', unsafe_allow_html=True)
st.write("---")

# Sidebar for Selection
st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/d/d8/Game_of_Thrones_title_card.jpg", use_container_width=True)
st.sidebar.title("🔎 Choose Your Character")
characters = df["character"].values
selected_character = st.sidebar.selectbox("🛡️ Select from the list", characters)

# Fetch Closest Match
character_id = np.where(df["character"].values == selected_character)[0][0]
x = df[["x", "y"]].values

distances = []
for i in range(len(x)):
    distances.append(np.linalg.norm(x[character_id] - x[i]))

recommended_id = sorted(list(enumerate(distances)), key=lambda x: x[1])[1][0]
recommended_character = df["character"].values[recommended_id]

# Calculate Similarity Score
similarity_score = round(100 - (distances[recommended_id] * 10), 2)

# Fetch Images & Descriptions
image_url = fetch_image(selected_character, api_data)
recommended_character_image_url = fetch_image(recommended_character, api_data)

description = fetch_description(selected_character, api_data)
recommended_description = fetch_description(recommended_character, api_data)

# Columns for Character Display
col1, col2 = st.columns(2)

col1, col2 = st.columns(2)

with col1:
    st.markdown(f'<h2 class="character">{selected_character}</h2>', unsafe_allow_html=True)
    st.image(image_url, caption=selected_character, width=300)  # Fixed image size
    st.info(f"**📝 Description:** {description}")

with col2:
    st.markdown(f'<h2 class="character">{recommended_character}</h2>', unsafe_allow_html=True)
    st.image(recommended_character_image_url, caption=recommended_character, width=300)  # Fixed image size
    st.success(f"**🔥 Closest Match:** {recommended_character}")
    st.info(f"**📝 Description:** {recommended_description}")
    st.markdown(f"<h3 style='color:#FFD700; text-align:center;'>🔥 Personality Match: {similarity_score}% 🔥</h3>", unsafe_allow_html=True)

# Animated Button
st.markdown(
    """
    <div style="display: flex; justify-content: center;">
        <button class="stButton">⚔️ Find Another Match ⚔️</button>
    </div>
    """,
    unsafe_allow_html=True,
)

# Footer
st.write("---")
st.markdown(
    "<h4 style='text-align: center; color: white;'>⚔️ Built for Game of Thrones Fans | Winter is Coming ⚔️</h4>",
    unsafe_allow_html=True,
)
