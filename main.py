import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from info import KEY
import os
import openai


def generate():
    prompt = "Please generate 10 ideas for coding projects."
    language = language_dropdown.get()
    prompt += f' The programming language is {language}.'
    difficulty = difficulty_value.get()
    prompt += f' The difficulty is {difficulty}.'

    if not checkbox1.get() and not checkbox2.get():
        pass
    elif checkbox1.get() and not checkbox2.get():
        prompt += f' The project should include a database.'
    elif checkbox2.get() and not checkbox1.get():
        prompt += f' The project should include a API.'
    elif checkbox1 and checkbox2:
        prompt += f' The project should include a database and API.'

    openai.api_key = KEY
    openai.api_key = KEY
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{prompt}"}]
    )
    answer = response.choices[0].message.content
    result.delete("1.0", "end")
    result.insert('0.0', answer)


# else:
#     result.delete("1.0", "end")


root = ctk.CTk()
root.geometry('750x600')
root.title('Project Generator')
root.resizable(0, 0)

title_label = ctk.CTkLabel(root, text='Project Idea Generator',
                           font=ctk.CTkFont(size=30, weight='bold'))
title_label.pack(padx=10, pady=(40, 20))

# Building Frame
frame = ctk.CTkFrame(root)
frame.pack(fill='x', padx=100)

# Language Section
language_frame = ctk.CTkFrame(frame)
language_frame.pack(padx=100, pady=(20, 5), fill='both')
language_label = ctk.CTkLabel(
    language_frame, text='Programming Language', font=ctk.CTkFont(weight='bold'))
language_label.pack()
language_dropdown = ctk.CTkComboBox(
    language_frame, values=['Python', 'Java', 'C++', 'JavaScript', 'Golang'])
language_dropdown.pack(pady=10)

# Difficulty Section
difficulty_frame = ctk.CTkFrame(frame)
difficulty_frame.pack(padx=100, pady=5, fill='both')
difficulty_label = ctk.CTkLabel(
    difficulty_frame, text='Project Difficulty', font=ctk.CTkFont(weight='bold'))
difficulty_label.pack()
difficulty_value = ctk.StringVar(value='Easy')
radiobutton1 = ctk.CTkRadioButton(
    difficulty_frame, text='Easy', variable=difficulty_value, value='Easy')
radiobutton1.pack(side='left', padx=(20, 10), pady=10)
radiobutton2 = ctk.CTkRadioButton(
    difficulty_frame, text='Medium', variable=difficulty_value, value='Medium')
radiobutton2.pack(side='left', padx=(20, 10), pady=10)
radiobutton3 = ctk.CTkRadioButton(
    difficulty_frame, text='Hard', variable=difficulty_value, value='Hard')
radiobutton3.pack(side='left', padx=(20, 10), pady=10)

# Features Section
feature_frame = ctk.CTkFrame(frame)
feature_frame.pack(padx=100, pady=5, fill='both')
features_label = ctk.CTkLabel(
    feature_frame, text='Features', font=ctk.CTkFont(weight='bold'))
features_label.pack()
checkbox1 = ctk.CTkCheckBox(feature_frame, text='Database')
checkbox1.pack(side='left', padx=50, pady=10)
checkbox2 = ctk.CTkCheckBox(feature_frame, text='API')
checkbox2.pack(side='left', padx=50, pady=10)

# Create Button
button = ctk.CTkButton(root, text='Generate Ideas', font=ctk.CTkFont(size=15), command=generate)
button.pack(padx=100, fill='x', pady=(5, 20))

# Create Textbox
result = ctk.CTkTextbox(root, font=ctk.CTkFont(size=15))
result.pack(pady=10, fill='x', padx=100)
# openai.api_key = KEY
# openai.api_key = KEY
# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": "Hi ChatGPT. Say hi back!"}]
# )
# answer = response.choices[0].message.content

# print(answer)
root.mainloop()
