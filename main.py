import streamlit as st
import langchain_helper as lch
import textwrap
import re


def format_pointwise_text(text):

    # Merge broken lines (usually caused by LLM formatting or transcript)
    text = re.sub(r'\n+', ' ', text)  # remove all newlines
    text = re.sub(r'\s+', ' ', text)  # normalize spaces

    # Split into points using digit-dot pattern (e.g., 1. 2. 3.)
    points = re.split(r'(?=\d+\.\s+\*\*)', text)

    cleaned_points = []
    for point in points:
        point = point.strip()
        if point:
            # Fix: ensure bold title and content are properly formatted
            point = re.sub(r'\*\*(.*?)\s*\*\*', r'**\1**', point)  # fix broken bolds
            point = re.sub(r'\*\*(.*?)\*\*\s*:', r'**\1:**', point)  # bold title with colon
            cleaned_points.append(point)

    return "\n\n".join(cleaned_points)



st.title("YouTube Assistance")

# Sidebar input form
with st.sidebar:
    with st.form('my_form'):
        youtube_url = st.text_area(
            label="What is the YouTube URL?",
            max_chars=100
        )
        query = st.text_area(
            label="What is your question about the video?",
            max_chars=100,
            key="query_input"
        )
        submit_button = st.form_submit_button(label='Submit')

# Process query after submission
if submit_button and query and youtube_url:
    db = lch.create_db_from_youtube_url(youtube_url)
    response = lch.get_response_from_query(db, query)

    formatted_response = format_pointwise_text(response)

    st.subheader("Answer:")
    st.markdown(formatted_response)

