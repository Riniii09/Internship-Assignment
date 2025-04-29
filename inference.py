prompts = [
  "Mujhe ek chai pilao.",
  "Kal tu aayega na party main?",
  "Weather kaisa hai?"
]

responses = [
  "Zarur, ek garam chai turant laata hoon.",
  "Of course, sabse pehle main hi aunga!",
  "Aaj thoda cloudy hai, par baarish nahi hogi."
]

for prompt, response in zip(prompts, responses):
  print(f"User: {prompt}\nAssistant: {response}\n")
