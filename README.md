# Taxogen Implementation
This is a implementation repo.

# About

This repo is fork from the franticnerd, author of the paper for constructing topic taxonomy from text corpora(“TaxoGen: Unsupervised Topic Taxonomy Construction by Adaptive Term Embedding and Clustering”).

I make some editing over the original code, such as changing the implementation environment to python 3.6(the original author use the python 2 to implement) and enriching some py files' code comments because of the large number of similar variable names.


# Paper

This repo is an implementation of the following paper for constructing topic taxonomy from text corpora.

"TaxoGen: Unsupervised Topic Taxonomy Construction by Adaptive Term Embedding and Clustering",
Chao Zhang, Fangbo Tao, Xiusi Chen, Jiaming Shen, Meng Jiang, Brian Sadler, Michelle Vanni, Jiawei Han,
ACM SIGKDD Conference on Knowledge Discovery and Pattern Mining (KDD), 2018.


# Input

The input consists of three files:

1. papers.txt
  - This data file contains all the documents (e.g., paper titles). 
  - Every line is a sequence of processed keywords (either uni-grams or phrases). 
  - The keywords are separated by blank spaces (words in a phrase are concatenated by '_').
2. keywords.txt
  - This data file contains all keywords extracted from the document collection (e.g., entities, noun phrases). 
  - Every line is a keyword.
3. embeddings.txt
  - This data file contains the embeddings of all the keywords. 
  - Every line is the embedding of a keyword.



The DBLP dataset used in the paper is available here:

https://drive.google.com/file/d/1GbxKrxrmFrKt5vgDHP1xe1Qr_rfvR1jh/view?usp=sharing


# How to run?

You can use "python main.py" to run TaxoGen.

A full pipeline is included in run.sh, including how we preprocess the corpus, run TaxoGen, and postproces the results for visualization.

# Structure

```
├─ code
│  ├─ embedding_deprecated
│  │  ├─ fetch_papers_relevant.py
│  │  ├─ leef.c
│  │  ├─ makefile
│  │  ├─ metrics.py
│  │  ├─ query_search
│  │  ├─ query_search.c
│  │  ├─ ransampl.c
│  │  ├─ ransampl.h
│  │  ├─ run_leef.sh
│  │  └─ word2vec.c
│  ├─ postprocess
│  │  ├─ __init__.py
│  │  ├─ plot.py
│  │  ├─ redundancy.py
│  │  └─ visualize.py
│  ├─ preprocess
│  │  ├─ AutoPhraseOutput.py
│  │  ├─ SegPhraseOutput.py
│  │  ├─ __init__.py
│  │  ├─ config.py
│  │  └─ main.py
│  ├─ tm
│  │  ├─ bin
│  │  │  └─ Taxonomy_TM.class
│  │  ├─ src
│  │  │  └─ Taxonomy_TM.java
│  │  ├─ .classpath
│  │  └─ .project
│  ├─ bdi.py
│  ├─ case_ranker.py
│  ├─ caseslim.py
│  ├─ cluster-preprocess.py
│  ├─ cluster.py
│  ├─ compress.py
│  ├─ dataset.py
│  ├─ eval.py
│  ├─ gen_eval.py
│  ├─ labeling.py
│  ├─ local_embedding_training.py
│  ├─ main.py
│  ├─ paras.py
│  ├─ preprocess.py
│  ├─ run.sh
│  ├─ sim_emb.py
│  ├─ taxonomy.py
│  ├─ utils.py
│  ├─ word2vec.c
│  ├─ word2vec.exe
│  └─ word2vec.o
├─ my code
│  └─ understandData.py
├─ windows
│  └─ pthreads-w32-2-9-1-release
├─ .gitignore
├─ LICENSE
├─ README.md
└─ requirements.txt

```

