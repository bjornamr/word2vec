import gensim
from gensim.models import Word2Vec
import os.path

def train_w2v():
    sentences = gensim.models.word2vec.LineSentence(os.path.join("data",'no.wiki.txt'))
    model = gensim.models.Word2Vec(sentences, size=300, window=5, min_count=5, workers=4, iter=5)
    model.save(os.path.join("data","no_wiki"))

def test():
    model = Word2Vec.load(os.path.join("data","no_wiki"))
    print(model.most_similar(positive=['blomst']))


if __name__ == "__main__":
    train_w2v()
    test()


