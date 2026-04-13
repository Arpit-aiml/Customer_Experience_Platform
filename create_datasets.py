import pandas as pd
import random

positive_reviews = [
    "Product is amazing and works perfectly",
    "Very good quality and durable",
    "Excellent product, highly recommended",
    "Worth every rupee",
    "Loved the product, very useful",
    "Exceeded my expectations in every way",
    "Outstanding value and superb performance",
    "I am very happy with this purchase",
    "High-quality product and fast delivery",
    "Great design, works exactly as advertised"
]
negative_reviews = [
    "Product is disappointing and does not work as expected",
    "Poor quality and not worth the money",
    "Very dissatisfied with this product",
    "Not recommended, waste of money",
    "Completely disappointed with the purchase",
    "Terrible experience, the product stopped working after one day",
    "The item arrived damaged and customer support was useless",
    "Extremely poor build quality, completely regret buying",
    "The product is overpriced and underperforms",
    "Not happy at all, it failed to meet expectations"
]
neutral_reviews = [
    "The product is okay, nothing special",
    "Average quality, does the job",
    "Not bad, but not great either",
    "It's fine for the price",
    "Neither good nor bad, just average",
    "Works as expected without standing out",
    "Fair quality for the cost",
    "Meets the basic needs, nothing extra",
    "Acceptable performance, but not impressive",
    "A decent option if you are not looking for anything special"
]

data = []
for _index in range(1000):
    review = random.choice(positive_reviews + negative_reviews + neutral_reviews)
    if review in positive_reviews:
        label = "positive"
    elif review in negative_reviews:
        label = "negative"
    else:
        label = "neutral"
    
    data.append({"review": review, "label": label})
df = pd.DataFrame({
    "review": positive_reviews + negative_reviews,
    "sentiment": ["positive"] * len(positive_reviews) +["negative"] * len(negative_reviews)
    })
df.to_csv("reviews_dataset.csv", index=False)

print("Dataset created and saved as reviews_dataset.csv")
