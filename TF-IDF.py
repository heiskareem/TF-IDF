import math

# Step 1: Define documents
documents = [
    "the cat sat",
    "the cat",
    "the dog barked"
]

# Step 2: Tokenize documents
def tokenize(doc):
    return doc.lower().split()

tokenized_docs = [tokenize(doc) for doc in documents]

# Step 3: Calculate Term Frequency (TF)
def compute_tf(doc_tokens):
    tf = {}
    total_terms = len(doc_tokens)
    for word in doc_tokens:
        tf[word] = tf.get(word, 0) + 1
    for word in tf:
        tf[word] /= total_terms
    return tf

tf_list = [compute_tf(doc) for doc in tokenized_docs]

# Step 4: Calculate Document Frequency (DF)
def compute_df(tokenized_docs):
    df = {}
    for doc in tokenized_docs:
        unique_terms = set(doc)
        for term in unique_terms:
            df[term] = df.get(term, 0) + 1
    return df

df = compute_df(tokenized_docs)
total_docs = len(documents)

# Step 5: Calculate Inverse Document Frequency (IDF)
idf = {}
for term, freq in df.items():
    idf[term] = math.log(total_docs / freq)

# Step 6: Compute TF-IDF
def compute_tfidf(tf, idf):
    tfidf = {}
    for term, tf_val in tf.items():
        tfidf[term] = tf_val * idf[term]
    return tfidf

tfidf_documents = [compute_tfidf(tf, idf) for tf in tf_list]

# Display the TF-IDF scores
for i, tfidf in enumerate(tfidf_documents):
    print(f"Document {i+1} TF-IDF:")
    for term, score in tfidf.items():
        print(f"  {term}: {score:.4f}")
    print()
