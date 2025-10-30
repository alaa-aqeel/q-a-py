
Dataset = {
    1: "python",
    2: "facebook",
    3: "chatgpt",
}


def choose_dataset_input() -> str :
    print("1. Python")
    print("2. Facebook")
    print("3. ChatGPT")
    choice = input("Choose a dataset (1/2/3): ").strip()
    try :
        return Dataset.get(int(choice))
    except:
        print("Invalid choice!")
        return choose_dataset_input()
    

def ask_question_input(callback) -> any:
    
    question = input("Ask a question: ").strip()
    
    if len(question) > 4 and question != "":
        callback(question)
    else:
        print("Invalid question")
        
    return ask_question_input(callback)