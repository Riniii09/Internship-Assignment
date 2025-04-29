import openai
import os

openai.api_key = os.getenv("YOUR_API_KEY")

response = openai.FineTuningJob.create(
  training_file = "your-file",
  model = "gpt-3.5-turbo",
  hyperparameters = {"n_epochs": 2}
)

print(response)
