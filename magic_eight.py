# coding:utf-8
# !/usr/bin/python3

question = input("What is your question? ")
while(question != "quit"):
    if (len(question) == 0 or question[-1] != "?"):
        print("I’m sorry, I can only answer questions.")
    else:
        answer_question()
    question = input("What is your question? ")