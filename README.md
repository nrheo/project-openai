# OpenAI Web App

## Introduction

The web application uses the lates OpenAI's API to create a lyrics generator, image generator, and movie recommendation system. Streamlit was used to create the web interface.

[![project-openai](https://img.youtube.com/vi/MliHRrp4v-E/0.jpg)](https://youtu.be/MliHRrp4v-E)

## Applications

1. Lyrics Generator

This application uses text completion with GPT-3. Once the user inputs an idea in text, the application generates lyrics for a song which consists of verse 1, pre-chorus, chorus, verse 2, pre-chorus, chorus, bridge, chorus and outro. The prompt used to train the large language model specifically mentioned that the lyrics should have some rhyming patterns. 

2. Image Generator

This application uses image generation with DALL-E. Once the user inputs an idea in text, the application produces images directly related to the idea. The slider widget was added to allow users to choose the number of images (from 1 to 5) they want to generate. 

3. Movie Recommender

This application uses Pinecone Vectore Database and GPT. Once the user inputs an idea in text, the application generates three movie recommendations related to the idea. The movie titles or descriptions are converted into embeddings and then similarities are calculated to generate movie recommendations tailored to the user's preferences and viewing history.

