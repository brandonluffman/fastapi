import requests as r

# add review
review = "Does this model even work?"


keys = {"review": review}

prediction = r.get("http://127.0.0.1:8000/predict-review/", params=keys)

results = prediction.json()
print(results["prediction"])
print(results["Probability"])