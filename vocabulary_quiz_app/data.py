from __future__ import annotations

from vocabulary_quiz_app.quiz_logic import Word

WORDS: list[Word] = [
    Word(term="apple", meaning="사과", example="I made an apple pie."),
    Word(term="book", meaning="책", example="Is that book yours?"),
    Word(term="chair", meaning="의자", example="Is this an empty chair?"),
    Word(term="door", meaning="문", example="Shut the door!"),
    Word(term="flower", meaning="꽃", example="a garden full of flowers"),
    Word(term="friend", meaning="친구", example="Is he a friend of yours?"),
    Word(term="music", meaning="음악", example="What kind of music do you like?"),
    Word(term="school", meaning="학교", example="My brother and I went to the same school."),
    Word(term="summer", meaning="여름", example="It's near summer."),
    Word(term="water", meaning="물", example="The water is flowing."),
]
