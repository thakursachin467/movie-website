import media
import fresh_tomatoes
toy_story=media.Movie("TOY STORY",
                        "A STORY OF A BOY AND TOYS COME TO LIFE",
                        "http://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg" ,
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar=media.Movie("Avatar",
                     "Jake, a paraplegic marine, replaces his brother on the  inhabited Pandora for a corporate mission",
                     "https://images-na.ssl-images-amazon.com/images/I/91qDRmPbAjS._SL1500_.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
john_wick=media.Movie("John wick",
                        "John Wick a retired hitman grieving the loss of his wife, is forced to return to his old ways",
                        "https://i.ytimg.com/vi/ZdOmCSmI4X0/movieposter.jpg",
                        "https://www.youtube.com/watch?v=2AUmvWm5ZDQ")
john_wick2=media.Movie("John Wick 2",
                         "Retired super-assassin John Wick plans to resume a quiet civilian life are cut short when Italian gangster Santino DAntonio shows up on his doorstep with a gold marker, compelling him to repay past favors ",
                         "http://t0.gstatic.com/images?q=tbn:ANd9GcR5VZ6Un0Fn4RYJSjH6MLsKgEmICbWqxWbfOBjDxkKSD891Thuj",
                         "https://www.youtube.com/watch?v=ChpLV9AMqm4")
game_of_thrones=media.Movie("game of thrones",
                            "Several royal families desire the Iron Throne to gain control of Westeros. Whilst kingdoms fight each other for power",
                            "http://www.gstatic.com/tv/thumb/tvbanners/14160794/p14160794_b_v8_aa.jpg",
                            "https://www.youtube.com/watch?v=giYeaKsXnsI")
vikings=media.Movie("Vikings",
                    "Ragnar Lothbrok, a legendary Norse hero, is a mere farmer who rises up to become a fearless warrior and commander of the Viking tribes with the support of his equally ferocious family.",
                    "http://www.gstatic.com/tv/thumb/tvbanners/14564057/p14564057_b_v8_aa.jpg",
                    "https://www.youtube.com/watch?v=s28cBkmoVIk")
movies=[toy_story,avatar,john_wick,john_wick2,game_of_thrones,vikings]

fresh_tomatoes.open_movies_page(movies)
