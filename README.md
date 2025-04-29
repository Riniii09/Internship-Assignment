# Internship-Assignment
LLM Fine-Tuning Mini–Project – Hinglish Voice-AI

## Setup Instructions

1. Clone this repo.
   git clone https://github.com/Riniii09/Internship-Assignment.git
   cd Internship-AssignmentNO  
2. Add the OpenAI API key `YOUR_API_KEY` to your environment.
3. Upload the `dataset.jsonl`.
4. Run `fine_tune.py` to initiate fine-tuning (requires paid access).

## Dataset

23 Hinglish-style prompt-completion pairs simulating casual conversational scenarios (as required).

## Fine-Tuning Setup (Theoretical)

- **Model**: `gpt-3.5-turbo` – balances cost and performance.
- **Epochs**: 2 – enough for a small dataset.
- **Learning Rate**: Default (OpenAI handles it automatically).


## Why Not Actually Fine-Tuned?

Due to budget constraints, the fine-tuning wasn't executed on OpenAI. However:

- The code provided is fully functional.
- Inference was simulated using mock logic.

## Sample Outputs (Simulated)

**Prompt**: Mujhe ek chai pilao.  
**Assistant**: Zarur, ek garam chai turant laata hoon.

**Prompt**: Kal tu aayega na party mein?  
**Assistant**: Of course, sabse pehle main hi aunga!

**Prompt**: Weather kaisa hai aaj?  
**Assistant**: Aaj thoda cloudy hai, par baarish nahi hogi.

## How to Evaluate

In real production:
- Ask human reviewers to rate response naturalness to adjust the temperatur of the model accordingly.
- Check understanding on unseen Hinglish inputs to see how much fine-tuning has actually helped the actual model.

## Conclusion

This repo shows a practical fine-tuning workflow using Hinglish dialogue. Even though actual fine-tuning wasn’t possible, simulated inference validates the conversational design.

**Note**: The original GPT-2 does perform well for regular English prompts, but when fine-tuned for Hinglish sentences, it doesn't perform as expected. This is because GPT-2 was not trained on much Hinglish data, and the sample dataset I provided wasn't enough for the model to adapt. 

Using the `gpt-3.5-turbo` model would be the most efficient choice for this task, saving time and resources that would otherwise be spent training the model from scratch for Hinglish responses. 

If you're curious, you can check the notebook where I experimented with GPT-2 for Hinglish testing. (https://colab.research.google.com/drive/1dg5-sdWrovFJSJv3gr9JY_NjlBji0JDP?usp=sharing)](#)
