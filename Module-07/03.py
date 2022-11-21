import pyjokes
def tell_some_jokes():
    jokes = pyjokes.get_joke(language="en", category="neutral")
    print(jokes)
tell_some_jokes()