import google.generativeai as ai

ai.configure(api_key="AIzaSyCgxKPd2-x-e56465x73u1YqWAfBw_ABhY")

models = ai.list_models()
for model in models:
    print(model.name)
