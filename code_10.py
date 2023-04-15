import nltk
import pandas as pd
from yelpapi import YelpAPI
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer
#`search_results = yelp_api.search_query(term='TERM', location='LOCATION', sort_by='CRITERIA', limit=#) # Replace all UPPERCASE values and pound sign accordingly`
#* `review_response = yelp_api.reviews_query(id="ALIAS FOR BUSINESS") # Replace all UPPERCASE values accordingly`


#reviews = open('the-cookshack-fort-worth_yelpapi_businesses_results.csv')
#for review in reviews:
    #sentiment_score = analyzer.polarity_scores(review)
   # print(review)
    #print(sentiment_score)
    #print('\n')

api_key = "Hj-kWRaoHKUjz9JyU-WQfYJ_x6JO21f0fmNTvxO6nTdnhc0N0pCvFtMMl_vbBV2dybD70tsvJPEA-yCSpkbvvF8AWJgv34rssQFYQbPQmM1P0cgjYDwy992YKb01ZHYx"
yelp_api = YelpAPI('Hj-kWRaoHKUjz9JyU-WQfYJ_x6JO21f0fmNTvxO6nTdnhc0N0pCvFtMMl_vbBV2dybD70tsvJPEA-yCSpkbvvF8AWJgv34rssQFYQbPQmM1P0cgjYDwy992YKb01ZHYx')
search_term = "Hot chicken"
location_term = "Dallas, TX"

search_results = yelp_api.search_query(
    term=search_term, location = location_term,
    sort_by = 'rating', limit=20, offset = 20
)
#print(search_results)


result_df = pd.DataFrame.from_dict(search_results['rating'])
print(result_df['alias'])
result_df.to_csv("yelpapi_businesses_results.csv")
id_for_reviews = 'tuckers-grill-and-taqueria-mesquite'
id_for_reviews = 'the-cookshack-fort-worth'
id_for_reviews = 'babes-chicken-dinner-house-roanoke'
id_for_reviews = 'daynes-craft-barbecue-fort-worth'

review_response = yelp_api.reviews_query(id=id_for_reviews)
print(review_response)
result_df.to_csv(f"{id_for_reviews}yelpapi_businesses_results.csv")
Review_df = pd.DataFrame.from_dict(result_df['review'])
print(Review_df['text'])

for review in result_df['text']:
    tokens = nltk.word_tokenize(review)
    pos_tags = nltk.pos_tag(tokens)
    for tag in pos_tags:
        if tag[1] == 'JJ' or tag[1] == 'JJR' or tag[1] == 'NN':
            print(tag[0])
    print(pos_tags)



#result_df = pd.DataFrame.from_dict(search_results['businesses'])
#print(result_df)
result_df.to_csv(f"{id_for_reviews}yelpapi_businesses_results.csv")



#analyzer = SentimentIntensityAnalyzer
#reviews = open('yelpapi_businesses_results.csv')
#for review_count in reviews:
    #sentiment_score = analyzer.polarity_scores(review)
    #print(review)
    #print(sentiment_score)
    #print('\n')

#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

#reviews = open("tacos_reviews.txt.")

#for review in reviews:
    #tokens = nltk.word_tokenize(review)
    #pos_tags = nltk.pos_tag(tokens)
    #print(pos_tags)
    #print(tokens)
#pos_tags = nltk.pos_tag(tokens)
#for token in pos_tags:
    #if token[1] == 'JJ' or token[1] == 'JJS':
        #print(token[0])


#work on slide 16 for Vader and to work on
# three reviews to make something insightful for opeing a business and what are you trying to find on the insigts information and sort criterioa 
#for the review i found these words were most used when describing tacos. Use keywords and location of El Paso TX
#pick a food to start and complile the information and city then comply the information



