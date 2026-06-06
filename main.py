import streamlit as st
import json
from pathlib import Path

# Set page config
st.set_page_config(
    page_title="Favorite Coding Language Poll",
    page_icon="💻",
    layout="centered"
)

# Title
st.title("💻 What is Your Favorite Coding Language?")
st.markdown("---")

# Define storage file
VOTES_FILE = "votes.json"

# Initialize votes from file if it exists
def load_votes():
    if Path(VOTES_FILE).exists():
        with open(VOTES_FILE, "r") as f:
            return json.load(f)
    return {"Python": 0, "JavaScript": 0, "Java": 0, "Go": 0}

# Save votes to file
def save_votes(votes):
    with open(VOTES_FILE, "w") as f:
        json.dump(votes, f, indent=2)

# Load current votes
votes = load_votes()

# Display poll options
st.markdown("### Cast Your Vote")
selected_language = st.radio(
    "Choose your favorite coding language:",
    options=list(votes.keys()),
    key="language_poll"
)

# Vote button
if st.button("📊 Vote", key="vote_button"):
    votes[selected_language] += 1
    save_votes(votes)
    st.success(f"✅ Vote recorded for {selected_language}!")
    st.balloons()

# Display results
st.markdown("### 📈 Poll Results")
st.markdown("---")

# Create columns for results display
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Languages:**")
    for lang in votes.keys():
        st.write(f"• {lang}")

with col2:
    st.markdown("**Votes:**")
    total_votes = sum(votes.values())
    for lang, count in votes.items():
        st.write(f"• {count}")

# Bar chart
st.markdown("### Vote Distribution")
st.bar_chart(votes)

# Statistics
st.markdown("---")
col1, col2, col3 = st.columns(3)
total_votes = sum(votes.values())
leading_lang = max(votes, key=votes.get) if total_votes > 0 else "None"
leading_count = votes[leading_lang] if total_votes > 0 else 0

with col1:
    st.metric("Total Votes", total_votes)
with col2:
    st.metric("Leading Language", leading_lang)
with col3:
    st.metric("Top Vote Count", leading_count)

# Footer
st.markdown("---")
st.markdown("*This is a simple Streamlit poll application to find your team's favorite coding language!*")
