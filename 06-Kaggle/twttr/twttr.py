tweet = input("tweet: ")
for letter in "AaEeIiOoUu":
    tweet = tweet.replace(letter, "")
print(tweet)