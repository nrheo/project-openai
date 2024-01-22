import os
import streamlit as st
import openai
import pinecone

from openai import OpenAI

# Replace with own API keys
os.environ["OPENAI_API_KEY"] = "sk-XXX"
client = OpenAI()

pinecone.init(
    api_key='XXX', 
    environment='XXX'
)

index = pinecone.Index('movies')

# Set the page config to wide mode
st.set_page_config(layout="wide")

# Title of the application
st.title('OpenAI API Applications')

# Sidebar for navigation
st.sidebar.title("Applications")
applications = ["Lyrics Generator", "Image Generator", "Movie Recommender"]
application_choice = st.sidebar.radio("Choose an Application", applications)

def lyrics_genertion(topic, additional_pointers):
    prompt = f"""
    You are a song writer with years of experience writing creative lyrics that uses rhymes and simple choruses.
    Your task is to write lyrics for a song on any topic system provides you with. Make sure to write in a format that works for Billboard.
    Each lyrics genertion should consist of two verses and a chorus only. Each verse should be four sentences long and the chorus should be four sentences long.

    Topic: {topic}
    Additiona pointers: {additional_pointers}
    """

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=1,
        max_tokens=700,
    )

    return response.choices[0].text.strip()

def generate_image(prompt, number_of_images=1):
    response = client.images.generate(
        prompt=prompt,
        size="1024x1024",
        n=number_of_images,
    )

    return response

# Main application logic
def main():
    if application_choice == "Lyrics Generator":
        st.header("Text Completion with GPT-3")
        st.write("Input an idea and get new lyrics.")
        input_text = st.text_area("Enter idea here:")
        additional_pointers = st.text_area("Enter additional pointers here:")
        
        if st.button("Generate lyrics"):
            with st.spinner('Generating...'):
                completion = lyrics_genertion(input_text, additional_pointers)
                st.text_area("Generated lyrics:", value=completion, height=200)

    elif application_choice == "Image Generator":
        st.header("Image Generation with DALL-E")
        st.write("Input some text and generate an image.")
        input_text = st.text_area("Enter text for image generation:")

        number_of_images = st.slider("Choose the number of images to generate", 1, 5, 1) 
        if st.button("Generate Image"):
            
            outputs = generate_image(input_text, number_of_images)
            for output in outputs.data:
                st.image(output.url)

    elif application_choice == "Movie Recommender":
        st.header("Movie Recommendation with GPT")
        st.write("Input a movie description and get a recommendation.")

        input_text = st.text_area("Enter movie description:")

        if st.button("Get movies"):
            with st.spinner('Generating...'):
                user_vector = client.embeddings.create(
                    model="text-embedding-ada-002",
                    input=input_text)

                user_vector = user_vector.data[0].embedding
                matches = index.query(
                    user_vector,
                    top_k=10,
                    include_metadata=True)

                for match in matches:
                    st.write(match['metadata']['title'])

# Run the main function
if __name__ == "__main__":
    main()
