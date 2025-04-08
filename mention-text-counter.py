counter = 0
user = input("Enter the username you want to search for, including the @: ")
user2 = input("Do they have a past username?: ")
if "@" not in user2:
    with open("tweets.js", "r") as in_file:
        for line in in_file:
            counter += line.count(user)
        print(f"The user {user} has been mentioned around {str(counter)} times by you.")

else:
    with open("tweets.js", "r") as in_file:
        for line in in_file:
            counter += line.count(user)
            counter += line.count(user2)
        print(f"The user {user} (f.k.a {user2}) has been mentioned around {str(counter)} times by you.")
