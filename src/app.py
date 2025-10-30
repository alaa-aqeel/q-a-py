from src.helpers import load_dataset
from src.cli import choose_dataset_input, ask_question_input
from src.semantic_search import compute_embeddings, find_best_answer
from torch import Tensor

def proccess_answer(dataset: str, text: str, embeddings: Tensor):
    haveBestAnswer, answers = find_best_answer(dataset, text, embeddings)

    if haveBestAnswer:
        answer = answers[0]
        print("")
        print(f"Answer: {answer['answer']}")
        print(f"question: {answer['question']}")
        print(f"score: {answer['score']}")
        print("\n")
    else:
        print("Sorry, I don't have an answer for that question.\n")
        for answer in answers:
            print(f"Score: {answer['score']} | {answer['question']} ->  {answer['answer']}")
        print("\n")
        


def main() :
    dataset = choose_dataset_input()
    print("Loading, please wait...\n")
    data = load_dataset(dataset)
    if data == None:
        return 
    embeddings = compute_embeddings(data) 
    print(f"Now You can Ask About: {dataset}\n")
    ask_question_input(lambda q: proccess_answer(data, q,embeddings ))
    print("")