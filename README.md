# 🧠 TF-IDF from Scratch

This project demonstrates how to calculate **TF-IDF (Term Frequency–Inverse Document Frequency)** from scratch in Python **without using any external libraries**. It's a fundamental technique in **natural language processing (NLP)** used to convert text into meaningful numerical representations.

---

## 📘 What is TF-IDF?
TF-IDF is a statistical measure that evaluates how relevant a word is to a document in a collection of documents. It increases with the number of times a word appears in the document but is offset by how common the word is across all documents.

### 🧮 Formula Breakdown

#### ✳️ Term Frequency (TF)
Measures how frequently a term appears in a single document.
\[ TF(t, d) = \frac{\text{Count of term } t \text{ in document } d}{\text{Total terms in document } d} \]

#### ✳️ Inverse Document Frequency (IDF)
Measures how rare a term is across the entire collection of documents.
\[ IDF(t) = \log\left(\frac{N}{df_t}\right) \]
Where:
- \( N \): total number of documents
- \( df_t \): number of documents containing term \( t \)

#### ✳️ TF-IDF
Combines both:
\[ TFIDF(t, d) = TF(t, d) \times IDF(t) \]
This gives a high score to terms that are frequent in one document but rare in others.

---

## 📂 Example Documents
```text
1. "the cat sat"
2. "the cat"
3. "the dog barked"
```

### ➗ Step-by-Step Calculation (for "cat" in Document 1):
- TF("cat", Doc1) = 1 / 3 ≈ 0.3333
- DF("cat") = 2 (appears in Doc1 and Doc2)
- IDF("cat") = log(3 / 2) ≈ 0.1761
- TF-IDF("cat", Doc1) = 0.3333 × 0.1761 ≈ 0.0587

This score reflects that "cat" appears frequently in the document, but it also appears in others — so it's not uniquely informative.

### Sample Output:
```text
Document 1 TF-IDF:
  the: 0.0000
  cat: 0.1352
  sat: 0.3662

Document 2 TF-IDF:
  the: 0.0000
  cat: 0.2027

Document 3 TF-IDF:
  the: 0.0000
  dog: 0.3662
  barked: 0.3662
```

---

## 🚀 How It Works in Code
1. Tokenize each document
2. Calculate term frequency (TF) for each term in each document
3. Calculate document frequency (DF) across all documents
4. Compute inverse document frequency (IDF) using log(N / df)
5. Multiply TF by IDF to get the final TF-IDF score for each term

---

## 📊 What It Means
- Words like **"the"** are common across all documents → IDF is 0 → TF-IDF is 0
- Words like **"sat"** or **"barked"** appear in only one document → higher IDF → higher TF-IDF

This makes TF-IDF a great way to identify **keywords** and **important terms** in documents.

---

## 🧾 Why This Matters
TF-IDF is widely used in:
- Text classification (e.g., spam detection)
- Document similarity (e.g., search ranking)
- Keyword extraction
- Topic modeling

---

## 🐍 Requirements
- Python 3.x
- No libraries required (fully native implementation)

---

## ✍️ Author
KareemShaik.com
