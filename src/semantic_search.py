from sentence_transformers import SentenceTransformer, util
from torch import Tensor, topk

model = SentenceTransformer('all-MiniLM-L6-v2')

def top_answer(scores: Tensor, dataset: dict, top_k: int = 3) -> list[dict]:
    top_results = topk(scores[0], k=top_k)
    
    return [
        {
            "score": f"{score.item():.4f}", 
            "question": dataset[idx]['question'], 
            "answer": dataset[idx]['answer'],
        } 
        for score, idx in zip(top_results.values, top_results.indices)
    ]

def compute_embeddings(dataset) -> Tensor:
    questions = [item['question'] for item in dataset]
    embeddings = model.encode(questions, convert_to_tensor=True)
    return embeddings


def find_best_answer(dataset, question, embeddings) -> list[bool, dict]:
    query_embedding = model.encode(question, convert_to_tensor=True)
    cos_scores = util.cos_sim(query_embedding, embeddings)
    best_idx = cos_scores.argmax()
    isBestAnswer = cos_scores[0][best_idx] > 0.3

    return isBestAnswer, top_answer(cos_scores, dataset, 3)


