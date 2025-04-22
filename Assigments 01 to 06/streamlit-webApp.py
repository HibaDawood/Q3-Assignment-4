import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Page configuration
st.set_page_config(
    page_title="Moodify - Mood Tracker",
    page_icon="😊",
    layout="centered"
)

# Custom styling
st.markdown("""
<style>
    .title {
        font-size: 42px;
        font-weight: bold;
        color: #8B5CF6;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 20px;
        color: #6B7280;
        text-align: center;
        margin-bottom: 30px;
    }
    .card {
        padding: 20px;
        border-radius: 10px;
        background-color: #F9FAFB;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .mood-emoji {
        font-size: 40px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# App title
st.markdown("<div class='title'>Moodify</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Track your daily mood and emotions</div>", unsafe_allow_html=True)

# Initialize session state for storing mood data
if 'mood_data' not in st.session_state:
    # Check if data file exists
    if os.path.exists('mood_data.csv'):
        st.session_state.mood_data = pd.read_csv('mood_data.csv')
    else:
        st.session_state.mood_data = pd.DataFrame(columns=['Date', 'Mood', 'Energy', 'Notes'])

# Create tabs for different sections
tab1, tab2 = st.tabs(["Log Mood", "View History"])

with tab1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("How are you feeling today?")
    
    # Date selection (default to today)
    date = st.date_input("Date", datetime.now().date())
    
    # Mood selection
    mood_options = {
        "😄 Great": 5,
        "🙂 Good": 4,
        "😐 Okay": 3,
        "🙁 Bad": 2,
        "😞 Terrible": 1
    }
    
    mood = st.select_slider(
        "Select your mood:",
        options=list(mood_options.keys())
    )
    
    # Energy level
    energy = st.slider("Energy level:", 1, 10, 5)
    
    # Notes
    notes = st.text_area("Notes about your day (optional):", height=100)
    
    # Submit button
    if st.button("Save Mood"):
        # Check if entry for this date already exists
        date_str = date.strftime("%Y-%m-%d")
        existing_entry = st.session_state.mood_data[st.session_state.mood_data['Date'] == date_str]
        
        if len(existing_entry) > 0:
            # Update existing entry
            st.session_state.mood_data.loc[st.session_state.mood_data['Date'] == date_str, 'Mood'] = mood
            st.session_state.mood_data.loc[st.session_state.mood_data['Date'] == date_str, 'Energy'] = energy
            st.session_state.mood_data.loc[st.session_state.mood_data['Date'] == date_str, 'Notes'] = notes
            st.success(f"Updated mood for {date_str}!")
        else:
            # Add new entry
            new_entry = pd.DataFrame({
                'Date': [date_str],
                'Mood': [mood],
                'Energy': [energy],
                'Notes': [notes]
            })
            st.session_state.mood_data = pd.concat([st.session_state.mood_data, new_entry], ignore_index=True)
            st.success(f"Mood logged for {date_str}!")
        
        # Save to CSV
        st.session_state.mood_data.to_csv('mood_data.csv', index=False)
    
    st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    if len(st.session_state.mood_data) > 0:
        # Sort data by date
        sorted_data = st.session_state.mood_data.sort_values(by='Date', ascending=False)
        
        # Display mood history
        st.subheader("Your Mood History")
        
        # Create a chart of mood over time
        if len(sorted_data) > 1:
            chart_data = sorted_data.copy()
            chart_data['Mood Value'] = chart_data['Mood'].apply(lambda x: mood_options.get(x, 3))
            chart_data = chart_data.sort_values(by='Date')
            
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.subheader("Mood Trends")
            st.line_chart(chart_data.set_index('Date')['Mood Value'], color="#8B5CF6")
            st.markdown("</div>", unsafe_allow_html=True)
        
        # Display recent entries
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Recent Entries")
        
        for i, row in sorted_data.head(5).iterrows():
            col1, col2 = st.columns([1, 3])
            
            with col1:
                st.markdown(f"<div class='mood-emoji'>{row['Mood'].split()[0]}</div>", unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"**{row['Date']}**")
                st.markdown(f"Energy: {row['Energy']}/10")
                if row['Notes']:
                    st.markdown(f"Notes: {row['Notes']}")
            
            st.divider()
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Show all entries in a table
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("All Entries")
        st.dataframe(
            sorted_data[['Date', 'Mood', 'Energy', 'Notes']], 
            use_container_width=True,
            hide_index=True
        )
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("No mood data yet. Start logging your mood to see history!")

# Footer
st.markdown("---")
st.caption("Moodify - Track your mood and improve your mental well-being")

# Print some information for demonstration
print("Moodify App Summary:")
print(f"Total mood entries: {len(st.session_state.mood_data)}")
if len(st.session_state.mood_data) > 0:
    print(f"Date range: {st.session_state.mood_data['Date'].min()} to {st.session_state.mood_data['Date'].max()}")
    mood_counts = st.session_state.mood_data['Mood'].value_counts()
    print("Mood distribution:")
    for mood, count in mood_counts.items():
        print(f"  {mood}: {count}")