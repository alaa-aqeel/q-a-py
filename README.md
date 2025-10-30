# Q&A
### A simple Q&A system that finds the most relevant answers from a predefined dataset of questions and answers using **Sentence Transformers** and **cosine similarity**.

- Compute embeddings for a dataset of questions.
- Find the top matching questions for any user query.
- Return top `k` answers along with similarity scores.
- Flag whether the best answer is relevant based on a similarity threshold.




## Overview 
```
Welcome to Q&A CLI!
1. Python
2. Facebook
3. ChatGPT
[Choose a dataset] (1/2/3): 3

Loading, please wait...
Now You can Ask About: chatgpt
```

## Answer Question
```sh
[Ask a question]: is free 

Answer => There is a free version with limitations, and paid subscriptions like ChatGPT Plus provide faster responses and access to newer models.

question  =>  Is ChatGPT free to use?
score => 0.4977

[Ask a question]: what gpt 
Answer =>  ChatGPT is an AI language model developed by OpenAI that can understand and generate human-like text.

question =>  What is ChatGPT?
score => 0.5154
```

## Don't have an answer
```
[Ask a question]: what is facebook
Sorry, I don't have an answer for that question.

Score =>  0.1973 
| question => What is the purpose of ChatGPT? 
| Answer => My purpose is to assist users with information, creative writing, coding, learning, and problem-solving tasks.

Score: 0.1554 
| question => What is ChatGPT? ->  
| Answer => ChatGPT is an AI language model developed by OpenAI that can understand and generate human-like text.

Score: 0.1553 
| question => Who created ChatGPT? 
| Answer => ChatGPT was created by OpenAI, a research organization focused on artificial intelligence.

```