from Model.MongoDB.Models.books import Book


def main():
    new_book = Book(
        {
            "title": "1984",
            "ISBN": "9780451524935",
            "authors": ["George Orwell"],
            "storyline": "The story takes place in an imagined future, the year 1984, when much of the world has fallen victim to perpetual war, omnipresent government surveillance, historical negationism, and propaganda. Great Britain, known as Airstrip One, has become a province of a superstate named Oceania that is ruled by the Party who employ the Thought Police to persecute individuality and independent thinking. Big Brother, the leader of the Party, enjoys an intense cult of personality despite the fact that he may not even exist. The protagonist, Winston Smith, is a diligent and skillful rank-and-file worker and Party member who secretly hates the Party and dreams of rebellion. He enters a forbidden relationship with a co-worker, Julia.",
            "genres": [
                "science fiction",
                "social science fiction",
                "dystopian fiction",
                "political fiction"
            ],
            "characters": [
                "Winston Smith",
                "Julia",
                "O'Brien"
            ],
            "pages": 328,
            "language": "english",
            "publisher": "Secker & Warburg",
            "publication_date": "1946-06-08",
            "copies_sold": 10000000,
            "book_type": "fiction",
            "source": [
                {
                    "audio_books":
                        {
                            "_id": 1,
                            "link": "https://www.amazon.com/1984-New-Classic-Edition-audiobook/dp/B000Q6ZLOI"
                        }
                },
                {
                    "e-books":
                        {}
                },
                {
                    "physical":
                        {}
                }
            ]
        }
    )
    new_book.save()


if __name__ == '__main__':
    main()
