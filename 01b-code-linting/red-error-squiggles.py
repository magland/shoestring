import nltk
import shoestring
import solver # import not found

def example1():
    s = shoestring.Sentence('This sentence is made up of words.')
    for i, w in enumerate(s.words):
    print(f'word {i}: {w}') # not properly indented
    print(s)

def download_nltk_lib(library_id: str):
    nltk.download(id, raise_on_error=True)

if __name__ == '__main__':
    library_id = 12
    download_nltk_lib(library_id) # incorrect argument type
    # download_nltk_lib('punkt')
    example1()