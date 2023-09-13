import random

print("Welcome to Movie Bot!,\nYou can ask me about Hollywood movies,\nI can recommend you the best movies and series to watch..")
chat={
     ("okay", "ok"): ["Sure, What kind of movie do you want to see?", "Tell me a movie name, and I'll provide you with the movie details."],
    ("what kind of movies can I ask about", "what types of films are there"): ["You can ask me about Hollywood movies. I can recommend you the best movies to watch."],
    ("how does your movie recommendation work", "how can you suggest a film"): ["I can suggest movies based on your preferences or provide information about specific movies. Just ask me about a movie genre, actor, director, or simply say 'recommend a movie.'"],
    ("can you recommend a good comedy movie", "suggest a film"): ["Of course! I recommend watching 'The Grand Budapest Hotel' if you're in the mood for a comedy. It's a delightful film directed by Wes Anderson."],
    ("tell me about 'Inception'", "give me details on 'Inception'"): ["'Inception' is a 2010 science fiction action film directed by Christopher Nolan. It explores the concept of dreams within dreams. The movie follows a skilled thief who enters the dreams of others to steal their secrets."],
    ("I don't like that movie", "movie is bad"): ["Oh, that's fine. You can try another movie from the list."],
    ("what's your favorite movie", "do you have a favorite film"): ["I don't have personal preferences, but I can recommend popular movies that match your taste."],
    ("thank you", "thanks", "thanks a lot"): ["You're welcome! If you have more questions or need movie recommendations, feel free to ask."],
     ("no","any other film"):["Try searching movies or series"]

    }
responses = {
    ("hai","hi","hello"): ["Hello!", "Hi there!", "Hey!!"],
    "hello": ["Hello!", "Hi there!", "Greetings!"],
    ("hi","hai", "hello"): ["Hello!", "Hi there!", "Greetings!"],
    "hey": ["Hai there!", "What can I do for you?", "Welcome!"],
    "how are you": ["I'm doing well, thanks for asking.", "I'm fine, how about you?"],
    "what's your name": ["My name is Movie bot.", "You can call me Movie bot."],
    "what is your name": ["I'm known as Movie bot.", "You can refer to me as Moviebot."],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    ("",""): ["ask something","Try asking top 10 movies or series"],
     ("idk","I don't know"):["It's okay can I suggest you movies",""],
    ("top 10 movies","best movies to watch","movie","movies"): [
        """ Here you go,Top 10 movies:
1. The Shawshank Redemption (1994) - 9.3/10
2. The Godfather (1972) - 9.2/10
3. The Dark Knight (2008) - 9.0/10
4. The Godfather: Part II (1974) - 9.0/10
5. 12 Angry Men (1957) - 9.0/10
6. Schindler's List (1993) - 8.9/10
7. The Lord of the Rings: The Return of the King (2003) - 8.9/10
8. Pulp Fiction (1994) - 8.9/10
9. The Good, the Bad and the Ugly (1966) - 8.8/10
10. The Lord of the Rings: The Fellowship of the Ring (2001) - 8.8/10
Now you can search by the above name for the movies details"""
    ],
    "top 10 series": [
         """ Top 10 series:
1. "Breaking Bad" (2008-2013) - 9.5/10
2. "Game of Thrones" (2011-2019) - 9.2/10
3. "Sherlock" (2010-2017) - 9.1/10
4. "Friends" (1994-2004) - 8.5/10
5. "The Office" (U.S.) (2005-2013) - 8.9/10
6. "Stranger Things" (2016-present) - 8.7/10
7. "The Crown" (2016-2022) - 8.6/10
8. "Black Mirror" (2011-present) - 8.8/10
9. "The Mandalorian" (2019-present) - 8.8/10
10. "The Witcher" (2019-present) - 8.2/10
Now you can search by the above name for the movies details"""
         ], 
          "Game of Thrones": {
        "release_date": "April 17, 2011",
        "imdb": 9.2,
        "description": "Game of Thrones, based on George R.R. Martin's A Song of Ice and Fire novels, is an epic fantasy series known for its political intrigue, complex characters, and dragons. It explores the power struggles among noble families in the fictional continents of Westeros and Essos."
    },
}



movie_and_series_database = {
    "Jurassic World: Fallen Kingdom": {
        "release_date": "Week of June 22, 2018",
        "imdb": 6.4,
        "description": "Jurassic World: Fallen Kingdom is a 2018 science fiction action film directed by J. A. Bayona and written by Derek Connolly and Colin Trevorrow."
    },
    "Avengers Infinity War": {
        "release_date": "April 27, 2018",
        "imdb": 8.4,
        "description": "Avengers: Infinity War, released in 2018, is a superhero film directed by Anthony and Joe Russo. The film brings together numerous Marvel superheroes as they join forces to stop the powerful villain Thanos from collecting all the Infinity Stones and wreaking havoc across the universe."
    },
    
    "Mad Max": {
        "release_date": "May 15, 2015",
        "imdb": 8.1,
        "description": "Mad Max: Fury Road, a 2015 action film directed by George Miller, is set in a post-apocalyptic desert wasteland. It follows the story of Max Rockatansky and Imperator Furiosa as they try to escape from the tyrannical ruler Immortan Joe and his army."
    },
    "La La Land": {
        "release_date": "December 9, 2016",
        "imdb": 8.0,
        "description": "La La Land, a 2016 musical romantic drama film directed by Damien Chazelle, stars Ryan Gosling and Emma Stone. The movie tells the story of an aspiring actress and a dedicated jazz musician who fall in love while pursuing their dreams in Los Angeles."
    },
    "The Revenant": {
        "release_date": "December 25, 2015",
        "imdb": 8.0,
        "description": "The Revenant, released in 2015, is a survival drama film directed by Alejandro González Iñárritu. The movie stars Leonardo DiCaprio as a frontiersman who must navigate the wilderness and survive after being left for dead by his hunting team."
    },
    "Inception": {
        "release_date": "July 16, 2010",
        "imdb": 8.8,
        "description": "Inception, a 2010 science fiction action film directed by Christopher Nolan, explores the concept of dreams within dreams. The movie follows a skilled thief who enters the dreams of others to steal their secrets."
    },
    "The Dark Knight": {
        "release_date": "July 18, 2008",
        "imdb": 9.0,
        "description": "The Dark Knight, released in 2008, is a superhero film directed by Christopher Nolan. It features Batman's battle against the Joker, a criminal mastermind who seeks to create chaos in Gotham City."
    },
    "The Shawshank Redemption": {
        "release_date": "September 23, 1994",
        "imdb": 9.3,
        "description": "The Shawshank Redemption, a 1994 drama film directed by Frank Darabont, tells the story of a banker who is wrongly convicted of murder and forms a close bond with a fellow inmate while seeking his redemption."
    },
    "Forrest Gump": {
        "release_date": "July 6, 1994",
        "imdb": 8.8,
        "description": "Forrest Gump, released in 1994, is a comedy-drama film directed by Robert Zemeckis. The movie follows the life of Forrest Gump, a man with low intelligence but a big heart, as he inadvertently influences major historical events."
    },
    "Pulp Fiction": {
        "release_date": "October 14, 1994",
        "imdb": 8.9,
        "description": "Pulp Fiction, a 1994 crime film directed by Quentin Tarantino, weaves together multiple interconnected stories involving crime, redemption, and the absurd. The movie is known for its non-linear narrative and memorable characters."
    },
    "The Matrix": {
        "release_date": "March 31, 1999",
        "imdb": 8.7,
        "description": "The Matrix, released in 1999, is a science fiction action film directed by the Wachowskis. It explores a dystopian future where humans are unknowingly trapped in a simulated reality by intelligent machines."
    },
    "Fight Club": {
        "release_date": "October 15, 1999",
        "imdb": 8.8,
        "description": "Fight Club, a 1999 drama film directed by David Fincher, follows an insomniac office worker who forms an underground fight club as a form of male bonding and rebellion against consumerism."
    },
    "Gladiator": {
        "release_date": "May 5, 2000",
        "imdb": 8.5,
        "description": "Gladiator, released in 2000, is an epic historical drama film directed by Ridley Scott. It tells the story of Maximus, a Roman general who seeks revenge against the corrupt emperor who murdered his family."
    },
    "The Lord of the Rings: The Fellowship of the Ring": {
        "release_date": "December 19, 2001",
        "imdb": 8.8,
        "description": "The Lord of the Rings: The Fellowship of the Ring, a 2001 epic fantasy film directed by Peter Jackson, is the first installment of the Lord of the Rings trilogy. It follows the journey of Frodo Baggins and his companions to destroy the One Ring."
    },
    "The Lord of the Rings: The Two Towers": {
        "release_date": "December 18, 2002",
        "imdb": 8.7,
        "description": "The Lord of the Rings: The Two Towers, released in 2002, is the second installment of the Lord of the Rings trilogy. It continues the epic journey to destroy the One Ring and features battles and alliances."
    },
    "The Lord of the Rings: The Return of the King": {
        "release_date": "December 17, 2003",
        "imdb": 8.9,
        "description": "The Lord of the Rings: The Return of the King, released in 2003, is the final installment of the Lord of the Rings trilogy. It culminates in the ultimate battle for Middle-earth and the fate of the One Ring."
    },
    "The Godfather": {
        "release_date": "March 24, 1972",
        "imdb": 9.2,
        "description": "The Godfather, a 1972 crime film directed by Francis Ford Coppola, is a classic tale of organized crime and family loyalty. It follows the Corleone family as they navigate the world of the mafia."
    },
    "The Godfather: Part II": {
        "release_date": "December 12, 1974",
        "imdb": 9.0,
        "description": "The Godfather: Part II is a 1974 crime film directed by Francis Ford Coppola. It is the second installment in The Godfather trilogy and explores the parallel stories of the young Vito Corleone and his son, Michael Corleone, as they navigate the world of organized crime."

    },
    "The Prestige": {
"release_date": "October 20, 2006",
"imdb": 8.5,
"description": "The Prestige, directed by Christopher Nolan and released in 2006, is a mystery thriller film set in the world of magic and illusion. It follows the rivalry between two magicians and their quest to create the ultimate trick."
},

"The Shining": {
"release_date": "May 23, 1980",
"imdb": 8.4,
"description": "The Shining, a 1980 psychological horror film directed by Stanley Kubrick, is based on Stephen King's novel. It tells the story of a family who becomes isolated in an eerie and haunted hotel, leading to the father's descent into madness."
},

"The Departed": {
"release_date": "October 6, 2006",
"imdb": 8.5,
"description": "The Departed, directed by Martin Scorsese and released in 2006, is a crime thriller film set in Boston. It follows an undercover cop and a mole in the police force as they try to identify each other while infiltrating an Irish gang in South Boston."
},

"The Social Network": {
"release_date": "October 1, 2010",
"imdb": 7.7,
"description": "The Social Network, a 2010 biographical drama film directed by David Fincher, explores the founding of Facebook and the legal battles that followed among its co-founders."
},

"Eternal Sunshine of the Spotless Mind": {
"release_date": "March 19, 2004",
"imdb": 8.3,
"description": "Eternal Sunshine of the Spotless Mind, a 2004 romantic science fiction film directed by Michel Gondry, tells the story of a couple who undergo a procedure to erase each other from their memories after a failed relationship."
},

"American Beauty": {
"release_date": "October 1, 1999",
"imdb": 8.3,
"description": "American Beauty, released in 1999 and directed by Sam Mendes, is a dark comedy-drama film that delves into the disintegration of a suburban family's life and the pursuit of happiness."
},

"Memento": {
"release_date": "March 16, 2001",
"imdb": 8.4,
"description": "Memento, a 2000 neo-noir psychological thriller film directed by Christopher Nolan, is known for its non-linear narrative. It follows a man suffering from short-term memory loss as he tries to solve the mystery of his wife's murder."
},

"Reservoir Dogs": {
"release_date": "October 23, 1992",
"imdb": 8.3,
"description": "Reservoir Dogs, a 1992 crime film directed by Quentin Tarantino, focuses on a group of criminals who come together for a diamond heist but suspect that one of them may be an undercover cop."
},

"Whiplash": {   
"release_date": "October 15, 2014",
"imdb": 8.5,
"description": "Whiplash, a 2014 drama film directed by Damien Chazelle, revolves around the intense and abusive relationship between a young jazz drummer and his demanding music instructor."
},

"The Grand Budapest Hotel": {
"release_date": "March 7, 2014",
"imdb": 8.1,
"description": "The Grand Budapest Hotel, directed by Wes Anderson and released in 2014, is a whimsical comedy film set in a luxurious European hotel. It follows the misadventures of the hotel's concierge and his protege."
},
   
}
new_category_responses = {
   "Breaking Bad": {
        "release_date": "January 20, 2008",
        "imdb": 9.5,
        "description": "Breaking Bad is a critically acclaimed crime drama series created by Vince Gilligan. It follows the transformation of Walter White, a high school chemistry teacher, into a ruthless methamphetamine manufacturer and drug lord."
   },
    "Game of Thrones": {
        "release_date": "April 17, 2011",
        "imdb": 9.2,
        "description": "Game of Thrones, based on George R.R. Martin's A Song of Ice and Fire novels, is an epic fantasy series known for its political intrigue, complex characters, and dragons. It explores the power struggles among noble families in the fictional continents of Westeros and Essos."
    },
    "Sherlock": {
        "release_date": "July 25, 2010",
        "imdb": 9.1,
        "description": "Sherlock is a modern adaptation of Sir Arthur Conan Doyle's detective stories. It stars Benedict Cumberbatch as Sherlock Holmes and Martin Freeman as Dr. John Watson, solving complex cases in contemporary London."
    },
    "Friends": {
        "release_date": "September 22, 1994",
        "imdb": 8.5,
        "description": "Friends is a beloved sitcom that revolves around a group of six friends living in New York City. The series follows their personal and professional lives, filled with laughter, love, and memorable moments."
    },
    "The Office (U.S.)": {
        "release_date": "March 24, 2005",
        "imdb": 8.9,
        "description": "The U.S. version of The Office is a mockumentary-style sitcom set in a mundane office environment. It humorously depicts the daily lives of the employees of Dunder Mifflin's Scranton branch."
    },
    "Stranger Things": {
        "release_date": "July 15, 2016",
        "imdb": 8.7,
        "description": "Stranger Things is a sci-fi horror series set in the 1980s. It follows a group of kids who encounter supernatural forces and government conspiracies when a young boy disappears in their small town."
    },
    "The Crown": {
        "release_date": "November 4, 2016",
        "imdb": 8.6,
        "description": "The Crown is a historical drama that chronicles the reign of Queen Elizabeth II. It explores the challenges and triumphs of the British monarchy and the evolving world during her reign."
    },
    "Black Mirror": {
        "release_date": "December 4, 2011",
        "imdb": 8.8,
        "description": "Black Mirror is an anthology series that delves into the dark side of technology and its impact on society. Each episode tells a standalone story that explores thought-provoking and dystopian themes."
    },
    "The Mandalorian": {
        "release_date": "November 12, 2019",
        "imdb": 8.8,
        "description": "The Mandalorian is a Star Wars-themed series set in the outer reaches of the galaxy. It follows the adventures of a lone bounty hunter in the aftermath of the Empire's fall."
    },
    "The Witcher": {
        "release_date": "December 20, 2019",
        "imdb": 8.2,
        "description": "The Witcher is a fantasy series based on the book series by Andrzej Sapkowski. It follows Geralt of Rivia, a monster hunter, as he navigates a world filled with magic, political intrigue, and dangerous creatures."
    }
}
faqs = {
    "idk": "It's okay, I can suggest you some movies.",
    "what kind of movie": "You can ask me to suggest the top 10 movies or series. Try asking 'movies' or 'series' for recommendations.",
    "cool":"yeh! what else do u want from me?",
    "good choice":"Oh, that's fine. type any other movie/series name I'll provide you the details..",

}




def get_response(message):
    for key_group in responses:
        if message in key_group:
            return random.choice(responses[key_group])
    for key_group in movie_and_series_database:
        if message.lower() == key_group.lower():
            return f"Movie name: {key_group}\nReleased on: {movie_and_series_database[key_group]['release_date']}\nIMDb: {movie_and_series_database[key_group]['imdb']}\nDescription: {movie_and_series_database[key_group]['description']}"
    for key_group in new_category_responses:
        if message.lower()== key_group.lower():
             return f"series name: {key_group}\nReleased on: {new_category_responses[key_group]['release_date']}\nIMDb: {new_category_responses[key_group]['imdb']}\nDescription: {new_category_responses[key_group]['description']}"
    for key_group in chat:
        if message in key_group:
            return random.choice(chat[key_group])
    for question in faqs:
        if question in message:
            return faqs[question]

    
    return "I'm sorry, I don't understand your message."

while True:
    message = input("You: ")
    response = get_response(message.lower())
    print("Chatbot:", response)
