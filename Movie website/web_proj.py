# -*- coding: utf-8 -*-
import media
import fresh_tomatoes

movies = []
movies.append(media.Movie("Avanda",
                          "Avatar (marketed as James Cameron's Avatar) is a 2009 American[7][8] epic science fiction film directed, written, produced, and co-edited by James Cameron, and starring Sam Worthington, Zoe Saldana, Stephen Lang, Michelle Rodriguez, and Sigourney Weaver. The film is set in the mid-22nd century, when humans are colonizing Pandora, a lush habitable moon of a gas giant in the Alpha Centauri star system, in order to mine the mineral unobtanium,[9][10] a room-temperature superconductor.[11] The expansion of the mining colony threatens the continued existence of a local tribe of Na'vi – a humanoid species indigenous to Pandora. The film's title refers to a genetically engineered Na'vi body with the mind of a remotely located human that is used to interact with the natives of Pandora.",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                          "https://www.youtube.com/watch?v=V--3JqeoQvA"))
movies.append(media.Movie("Toy story",
                          "Toy Story is a 1995 American computer-animated adventure buddy comedy film produced by Pixar Animation Studios and released by Walt Disney Pictures. Directed by John Lasseter at his directorial debut, Toy Story was the first feature-length computer-animated film and the first theatrical film produced by Pixar. Toy Story follows a group of anthropomorphic toys who pretend to be lifeless whenever humans are present, and focuses on the relationship between Woody, a pullstring cowboy doll (voiced by Tom Hanks), and Buzz Lightyear, an astronaut action figure (voiced by Tim Allen). The film was written by John Lasseter, Andrew Stanton, Joel Cohen, Alec Sokolow, and Joss Whedon, and featured music by Randy Newman. Its executive producers were Steve Jobs and Edwin Catmull. It was released in theatres November 22, 1995.",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                          "https://www.youtube.com/watch?v=KYz2wyBy3kc"))

fresh_tomatoes.open_movies_page(movies)
