import google.generativeai as ai

ai.configure(api_key="your api key")

models = ai.list_models()
for model in models:
    print(model.name)
