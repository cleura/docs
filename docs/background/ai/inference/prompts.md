# Prompts

??? note "Invite-only access"
    Access to {{brand_ai}} is currently invite-only.

Prompts are the text inputs that tell an LLM what to do.

We explain two very common prompt types, *System prompt* and *User prompt*, that you can adjust in the [Playground](../../../howto/ai/inference/playground.md).
Think of System prompts as a way to define the rules of engagement, while User prompts define tasks.

## System prompt

This is where you can type in detailed instructions, telling the AI model what role it should assume, how it should behave, and how it should respond.
Example:

```plain
You are an experienced log cabin builder from Relatively North.
No other person knows better than you how to survive off-grid.
Offer practical examples and detailed instructions.
Always warn about potentially dangerous techniques or approaches.
```

## User prompt

This is the actual instruction, question, or message you send to an LLM.
In other words, it is what you want the model to do.
