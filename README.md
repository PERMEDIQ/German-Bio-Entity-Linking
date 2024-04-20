

# README

Python Version: 3.8.0


## Scispacy


### Installation: 

* Update pip

```bash
python -m pip install --upgrade pip
```

* Install the scispacy using `setup.py`
  
```bash
pip install -e .
```

### Folder structure:

The `data` folder has following structure. The folder labeled as `(not in repo)` can be generated as described in the `scispacy.iypnb` notebook. 

```bash
│   de_1k_test_query.txt # mention dataset
│   de_wikimed_bel_dev_query.txt # mention dataset
│   de_wikimed_bel_test_query.txt # mention dataset
│   de_wikimed_bel_train_query.txt # mention dataset
│   qids_with_cui_kb.txt # UMLS_Wikidata KB
│  umls_onto_all_lang_cased_wikimed_only_399931.txt # UMLS_SapBERT KB
│
├───processed (not in repo)
│   └───kbs
│           kb_from_sapbert.jsonl
│           kb_from_wikidata_sparql.jsonl
│
└───raw 
    ├───BEL-silver-standard
    │   │   .DS_Store
    │   │
    │   └───WikiMed-DE-BEL
    │           .DS_Store
    │           dev_data_bel.json
    │           test_data_bel.json
    │           train_data_bel.json
    │           WikiMed-DE-BEL.json
    │
    └───kbs (not in repo)
            qids_with_cui.csv
            qids_with_cui_output.jsonl
```

The `artifacts` contains ANN indexes and vectorizers for KBs.

```bash 
├───sapbert
│       concept_aliases.json
│       nmslib_index.bin
│       tfidf_vectorizer.joblib
│       tfidf_vectors_sparse.npz
│
└───sparql
        concept_aliases.json
        nmslib_index.bin
        tfidf_vectorizer.joblib
        tfidf_vectors_sparse.npz
```
  


### Reproduce Results

Follow the steps in the `scispacy.iypnb` to reproduce results.


## Embedding based models:

[cambridgeltl/SapBERT-UMLS-2020AB-all-lang-from-XLMR](https://huggingface.co/cambridgeltl/SapBERT-UMLS-2020AB-all-lang-from-XLMR): Multilingual model trained on UMLS

[jinaai/jina-embeddings-v2-base-de](https://huggingface.co/jinaai/jina-embeddings-v2-base-de): a German/English bilingual text embedding model 

[BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3) : Multilingual model which can generate dense, sparse, and [colbert style](https://til.simonwillison.net/llms/colbert-ragatouille) embeddings. We only use dense embeddings.

### Installation: 

Installed in the same virtual environment. 

```bash
pip install torch --index-url https://download.pytorch.org/whl/cu118
```
You may need to select cuda version for `torch` according to your GPU.

```bash
pip install -r requirements_encoders.txt
```

For Faiss ANN index.

```bash
pip install faiss-gpu
```

### Reproduce Results



**Preferable:** Follow the steps in the `embedding_encoders_ann.iypnb` for using the FAISS ANN index.

**Alternative:** Follow the steps in the `embedding_encoders.iypnb` to reproduce results.


### Reference Dependencies

The exact dependencies used are mentioned in `reference_requirements.txt` for reference.

Python 3.8.0 

# References:

The Repository is based on [ScispaCy](https://github.com/allenai/scispacy) Repository. 












