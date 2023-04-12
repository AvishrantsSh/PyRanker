from rankers.vspace import VSpaceRanker
from rankers.bm25 import BM25Ranker
import time

def main():
    with open('test/sample_docs2.txt') as f:
        CORPUS = f.readlines()

    QUERY = "artificial intelligence"
    vs_ranker = VSpaceRanker(CORPUS)
    bm_ranker = BM25Ranker(CORPUS)
    v_rank, v_score = vs_ranker.get_top_n(QUERY, 10)
    bm_rank, bm_score = bm_ranker.get_top_n(QUERY, 10)
    print("Vector Space Ranking: ", v_rank, v_score)
    print("BM25 Ranking: ", bm_rank, bm_score)

if __name__ == '__main__':
    start = time.time()
    main()
    print("Time taken: ", time.time() - start)
