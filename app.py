import streamlit as st

# Function to summarize text
def summarize_text(text, style, size):
    sentences = text.split('. ')
    summary_length = max(1, int(len(sentences) * size / 100))
    summary = sentences[:summary_length]

    if style == "Passage":
        return ' '.join(summary)
    elif style == "Bullet Points":
        return '\n'.join(f"- {sentence.strip()}" for sentence in summary)
    elif style == "Custom":
        return ' | '.join(summary)
    else:
        return "Invalid style selected."

# Streamlit app
st.title("Text Summarization Tool")

# Input text
text = st.text_area("Enter the text to summarize:", height=200)

# Summarization style
style = st.selectbox("Select summarization style:", ["Passage", "Bullet Points", "Custom"])

# Summary size
size = st.slider("Select summary size (% of original text):", min_value=10, max_value=100, value=50)

# Summarize button
if st.button("Summarize"):
    if text.strip():
        summary = summarize_text(text, style, size)
        st.subheader("Summary:")
        st.text_area("", summary, height=200)
    else:
        st.warning("Please enter some text to summarize.")

# Example usage
st.sidebar.title("Example")
st.sidebar.write("Input Text:")
example_text = "Streamlit is an open-source app framework for Machine Learning and Data Science projects. It allows you to create beautiful web apps with minimal effort. Streamlit is easy to use and requires no web development skills. It is widely used by data scientists and machine learning engineers."
st.sidebar.write(example_text)

st.sidebar.write("Example Summary (Bullet Points, 50%):")
example_summary = summarize_text(example_text, "Bullet Points", 50)
st.sidebar.write(example_summary)