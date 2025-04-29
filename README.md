# CALCULATOR

#### Video Demo: [Watch the video](https://youtu.be/_hm-0D1bCBE?si=UyPQ7yIcTGlOsjCq)

#### Description:
This is a simple calculator program with a graphical user interface (GUI) built using Python's Tkinter library. The calculator supports basic arithmetic operations such as addition, subtraction, multiplication, and division. It also includes a clear function to reset the input and a solve function to evaluate the entered expression.

Name: Jesslyn Trixie Edvilie  
edX and GitHub: jesslyntrixie  
Location: Malang, Indonesia

## Features

- **Basic Arithmetic Operations**: Perform addition, subtraction, multiplication, and division.
- **Clear Function**: Reset the current input.
- **Solve Function**: Evaluate the entered arithmetic expression.
- **Customizable Design**: The calculator is designed with a color scheme that can be customized to your preference.

## How to Use

1. **Input Numbers and Operations**: Click the buttons to input numbers and arithmetic operations.
2. **Clear Input**: Click the 'C' button to clear the current input.
3. **Evaluate Expression**: Click the '=' button to evaluate the entered expression and display the result.

## Project Structure

### Files

- **calculator.py**: This is the main file containing the calculator logic and GUI setup. It includes functions for initializing the Tkinter environment, handling button clicks, clearing the input, and evaluating expressions.
- **test_calculator.py**: This file contains unit tests for the calculator functions. It uses the `pytest` framework along with `pytest-mock` to mock Tkinter components and test the functionality of the calculator.

### Design Choices

1. **Use of Tkinter**: Tkinter was chosen for its simplicity and ease of use for creating GUI applications in Python. It is part of the standard library, which means no additional installations are required.
2. **StringVar for Display Management**: The `StringVar` class from Tkinter is used to manage the value displayed on the calculator screen. This allows for easy updates and retrieval of the current input.
3. **Eval for Expression Evaluation**: The `eval` function is used to evaluate the arithmetic expressions entered by the user. While `eval` can be dangerous if used improperly, it is sufficient for this simple calculator application. In a more complex or production-level application, a safer evaluation method would be recommended.
4. **Mocking in Tests**: The `pytest-mock` library is used to mock Tkinter components in the unit tests. This allows for testing the calculator logic without the need for a graphical interface.

### Why I chose to make this project
A calculator might seem to be a really simple project, but in fact, I spent about five working days coding this project. I have been interested in GUIs in Python but sadly the CS50P course doesn't cover that, so I decided to self-study and made this calculator to implement my knowledge. 
The logic of the calculator is relatively simple, so I spent more time on learning how to make Python GUI rather than creating the logic of this final project.

Fun fact, I spent EVEN MORE time coding the pytest file. We all know that we are taught to assert the return values of our functions. The functions in my calculator doesnt return anything, as they only update the state of the GUI. I learnt that in the hard way. But overall, I enjoyed coding this project!


Enjoy using the calculator! <3  
Love, Jesslyn.