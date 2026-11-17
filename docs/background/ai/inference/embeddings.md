# Embeddings

??? note "Invite-only access"
    Access to {{brand_ai}} is currently invite-only.

Embeddings turn text into lists of numbers that machines can compare.
We explain how they work, what you can do with them, and how you can create your own in the [Playground](../../../howto/ai/inference/playground.md).

## From text to vectors

An embedding is a mathematical codification of text that captures aspects of its meaning.
Instead of treating text as a sequence of words, an AI model converts it into a *vector* (list of numbers) in a multidimensional space.

Imagine giving an embedding model this sentence:

```plain
I love using OpenBSD as a daily driver.
```

The model might produce something like this:

```plain
[0.002157, -0.002306, -0.004116, -0.005292, 0.015552, -0.002586, -0.021469, 0.011466, ...]
```

In this example, we list only 8 numbers, but in reality an embedding might contain hundreds or even thousands of numbers.
All those numbers represent the sentence in a multidimensional vector space.

Texts with similar meanings have vectors with [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity) close to 1.
Conversely, texts with dissimilar meanings have vectors with cosine similarity close to -1.

## Semantic search

Consider the following three sentences:

* **Sentence A:** `How do I configure OpenBSD for desktop use?`
* **Sentence B:** `How can I have a desktop OS based on OpenBSD?`
* **Sentence C:** `What's the weather like in Tuktoyaktuk today?`

A traditional keyword search might struggle to recognize that sentences A and B are asking essentially the same question.
An embedding-based search can recognize the semantic similarity of sentences A and B, even though they use different words.
It also recognizes that sentence C asks about something entirely different.

## Locally hosted assistants

The more a local AI assistant knows about your file collection, the more useful it becomes.

Embeddings allow the assistant to codify the contents of those files.
Then, through [Retrieval-Augmented Generation](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) (RAG), the assistant can formulate answers that are particularly useful to the file owner.
