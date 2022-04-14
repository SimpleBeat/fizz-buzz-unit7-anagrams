import flask

app = flask.Flask(__name__)

@app.route("/")
@app.route("/anagrams/<string:a_word>")
def start(a_word="hello"):

    word_file = open("words.txt")
    all_words = word_file.read().splitlines()
    word_file.close()

    anagrams = []

    a_word_letters_sorted = "".join(sorted(a_word.upper()))

    for word in all_words:
        if len(word) == len(a_word):
            if word != a_word.upper():
                if "".join(sorted(word)) == a_word_letters_sorted:
                    anagrams.append(word)

    if anagrams == []:
        anagrams = ["Looks like there are no anagrams of this word!"]

    return flask.render_template('anagrams.html', answers=anagrams, original_word=a_word.upper())