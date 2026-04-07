# Tokens

Tokens are the basic units of text that an LLM processes.
You can think of them as the fundamental building blocks LLMs use to process input and produce output.

## What they look like

Depending on the [tokenization](https://en.wikipedia.org/wiki/Large_language_model#Tokenization) scheme an LLM uses, tokens are whole words, parts of words, or single characters.
For example, the sentence "Colder is better!" may be tokenized as [`Colder`, `is`, `better`, `!`], while the sentence "Summer is overrated!" may be tokenized as [`Summer`, `is`, `over`, `rated`, `!`].

A rough estimate is that a token is about 75% of an English word, but you should keep in mind that even this estimate varies significantly by language and text complexity.

## Why they matter

No LLM can process raw text.
Instead, an LLM first converts _everything_ into tokens, and only then moves on to processing.

Any prompt you type is measured in tokens, and so is any answer you get back.

The _context window_, which is the maximum amount of text an LLM can process in a single request, is also measured in tokens.
A 128K context window, for example, means the combined input and output cannot exceed 128,000 tokens, which is roughly 96,000 English words.

The way tokenization is implemented affects the efficiency of an LLM.
More specifically, it influences the way an LLM processes text, and thus how accurately it understands word boundaries and meaning.

Finally, tokens play a key role in cost calculations;
LLM APIs usually charge based on token usage, both for _input_ tokens (your prompts) and _output_ tokens (the responses you get back).
