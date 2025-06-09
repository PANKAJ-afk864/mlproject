# END TO END MACHINE LEARNING PROJECT

#  Student Exam Performance Indicator

This is a **Machine Learning Web App** built using Python and Flask that predicts a student's **math exam score** based on various academic and personal features.

>  URL: `http://127.0.0.1:5000/predictdata`

---

##  Features

- Predict student's **Math Score** based on:
  - Gender
  - Race/Ethnicity
  - Parental Level of Education
  - Lunch Type
  - Test Preparation Course
  - Writing Score
  - Reading Score
- Simple and clean HTML UI using Flask Jinja templates
- Backend Machine Learning pipeline for training and prediction

---

##  Tech Stack

| Technology | Description                        |
|------------|------------------------------------|
| Python     | Programming language               |
| Flask      | Web framework                      |
| scikit-learn | ML modeling                     |
| HTML/CSS   | Frontend UI                        |
| Pandas, NumPy | Data handling                   |
| Jupyter Notebook | EDA and model development   |

---

##  Folder Structure

Student_Exam_Performance_Indicator/
│
├── static/ # Static files (CSS, images if any)
├── templates/
│ ├── home.html # Form UI for input and prediction
│ └── index.html # Welcome or landing page
│
├── src/
│ ├── components/ # Data ingestion, transformation, model trainer
│ ├── pipeline/ # Prediction pipeline
│ ├── logger.py
│ └── utils.py
│
├── app.py # Main Flask application
├── requirements.txt # Required Python packages
├── setup.py # Setup script
└── README.md # You're here!