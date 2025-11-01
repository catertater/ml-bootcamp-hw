import pickle

with open('pipeline_v2.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)


customer = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}


customer = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}


print(pipeline.predict_proba(client)[0, 1])