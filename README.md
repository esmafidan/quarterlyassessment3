### quarterlyassessment3

# Quiz Bowl GUI Project
## Overview
This project is part of the third quarterly assessment for your course. The objective is to create a Graphical User Interface (GUI) for a Quiz Bowl project. The GUI will be used by end-users to take quizzes in different categories, while the backend is managed by the programmer. The GUI is designed to be user-friendly, so that users without any coding knowledge can navigate and interact with it.

The backend includes a database with various questions categorized by course, but users will only interact with the quiz content through the GUI.

## Project Structure
### Database:

A database with 5 tables, each representing a different course or category.
Each table should contain a minimum of 10 questions related to that course.
Include functionality for adding, removing, and reading questions from the database for backend management.

### GUI:

The user interacts with two main windows:
Category Selection Window: Allows users to select a quiz category. Implement using any widgets such as combo boxes, entry boxes, or radio buttons.
Quiz Window: Displays multiple-choice questions based on the selected category. The user should be able to:
Select an answer
Submit their answer
Receive feedback on their answer

### Question Class:

Develop a class to standardize the question display format. This class will manage how questions are loaded and displayed in the GUI. The use of this class is required to streamline question display and ensure scalability.

## Instructions
Database Setup:

Use SQL to create the database with 5 tables for each course. Each table should store at least 10 questions.
Add scripts or functionality to manage the database, allowing for adding, removing, and reading questions.
Implementing the GUI:

## Project Should: 
Allow users to select a category.
Include a “Start Quiz Now” button to proceed to the quiz.
Display at least 10 multiple-choice questions from the selected category.
Provide options for the user to select and submit answers.
Show feedback based on the user's response.