from pyranker.rankers.bm25 import BM25Ranker
import matplotlib.pyplot as plt

def precision_recall_curve(rel_docs, return_docs):
    """
    Computes precision and recall values for different cutoff points
    :param rel: list of relevance scores (1 if relevant, 0 otherwise)
    :param score: list of scores
    :return: precision, recall, cutoffs
    """
    precision = []
    recall = []
    tp = 0
    fp = 0
    tp_fn = len(rel_docs)
    for r in return_docs:
        if r in rel_docs:
            tp += 1
        else:
            fp += 1
        
        precision.append(tp / (tp + fp))
        recall.append(tp / tp_fn)

    return precision, recall

def test():
    with open('tests/sample_docs.txt') as f:
        CORPUS = f.readlines()

    QUERY = "machine learning algorithm"
    bm_ranker = BM25Ranker(CORPUS)
    bm_rank, bm_score = bm_ranker.get_top_n(QUERY, prune=0.5, n=7)
    print("BM25 Ranking: ", bm_rank, bm_score)

    # Compute precision and recall values for different cutoff points
    rel_docs = [10, 13, 14, 16, 17 ,18, 19]
    precision, recall = precision_recall_curve(rel_docs, bm_rank)
    plt.plot(recall, precision, "-o")
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curve for BM25')
    plt.show()

if __name__ == '__main__':
    test()
