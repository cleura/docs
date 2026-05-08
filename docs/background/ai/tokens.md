# Tokens

??? note "Invite-only access"
    Access to {{brand_ai}} services is currently invite-only.

Tokens are the basic parts of text that LLMs process.
Think of them as building blocks for LLMs.

## What they look like

Depending on the [tokenization](https://en.wikipedia.org/wiki/Large_language_model#Tokenization) scheme an LLM uses, tokens are whole words, parts of words, or single characters.
For example, the sentence "Colder is better!" may be tokenized as [`Colder`, `is`, `better`, `!`], while the sentence "Summer is overrated!" may be tokenized as [`Summer`, `is`, `over`, `rated`, `!`].

A token is about 75% of an English word.
This varies by language and text type.

## Why they matter

LLMs cannot process raw text.
They convert everything to tokens first.

Your prompts and answers are measured in tokens.

The *context window* is the maximum amount of text an LLM can handle.
It is measured in tokens.
For example, a 128K window means input and output cannot go over 128,000 tokens.
That is about 96,000 English words.

Tokenization affects how well LLMs work.
It changes how they understand word boundaries and meaning.

Tokens affect cost.
LLM APIs usually charge for input and output tokens.
