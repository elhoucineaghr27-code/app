import streamlit as st

st.title("Music Personality Analyzer 🎧")

genre_input = st.text_input("What is your favourite genre in music?")

gt = {
    'Rock': ['Rebellious', 'Energetic', 'Creative'],
    'Pop': ['Social', 'Energetic', 'Emotional'],
    'Jazz': ['Intellectual', 'Creative', 'Peaceful'],
    'Hip Hop': ['Rebellious', 'Social', 'Creative'],
    'Classical': ['Intellectual', 'Peaceful', 'Emotional'],
    'Metal': ['Rebellious', 'Energetic', 'Emotional'],
    'Electronic': ['Creative', 'Adventurous', 'Energetic'],
    'Country': ['Peaceful', 'Emotional', 'Social'],
    'R&B': ['Emotional', 'Social', 'Peaceful'],
    'Reggae': ['Peaceful', 'Social', 'Creative'],
    'Blues': ['Emotional', 'Intellectual', 'Creative'],
    'Indie': ['Creative', 'Adventurous', 'Rebellious'],
    'Funk': ['Energetic', 'Social', 'Creative'],
    'Soul': ['Emotional', 'Social', 'Peaceful'],
    'Punk': ['Rebellious', 'Energetic', 'Adventurous'],
    'Folk': ['Peaceful', 'Intellectual', 'Emotional'],
    'Rap': ['Rebellious', 'Social', 'Creative'],
    'Tarab': ['Social', 'Creative', 'Emotional'],
    'sex sound': ['sir t7wa']

}

if st.button("Analyze"):
    genres = genre_input.lower().split(",")
    genres = [g.strip().title() for g in genres]

    all_traits = []

    for genre in genres:
        if genre in gt:
            all_traits.extend(gt[genre])

    unique_traits = list(set(all_traits))[:3]

    if unique_traits:
        st.success(f"Your personality is {', '.join(unique_traits).lower()} ✨")
    else:
        st.error("Genre not found. Try: Rap, Pop, Rock, Lofi...")