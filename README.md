# NLP_Deploy
Predict Wheteher Patient or Not

Analysis of Patient Data.ipynb -- Describe Analysis of Data


## Prerequisites

You must have following python libararies installed on your machine. Please refer to requirements.txt file for details.

Flask (for creating web application)
NLTK (for natural language processing)
Requirements : requirements.txt (all necessary libraries)


## Project Structure

The projects has following major parts:

app.py : Contains Flask APIs that receive inputs through GUI, calls the main python script for processing and returns the output.
predict.py : Contains python code to predict pateint or not.
templates : Contains HTML files that allow user to interact with the application.


## Running the Project

1. Open Ananconda command prompt and move to your project home directory.
2. Run app.py using below command to start Flask API python app.py
3. Navigate to the localhost to view the application home page. Localhost: http://127.0.0.1:5000/ or http://localhost:5000
4. Enter the text in the texbox and hit predict button.
5. If everything goes well, you should be able to see the predict pateint type on the results page.
