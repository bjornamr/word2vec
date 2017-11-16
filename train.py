# -*- coding: utf-8 -*-
import logging
import os.path
import sys
import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


def train_w2v():
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    model = Word2Vec(LineSentence(os.path.join("data",'no.wiki.txt')), size=300, window=5, min_count=5, workers=multiprocessing.cpu_count())
    model.init_sims(replace=True) # trim memory usage
    model.save(os.path.join("data","no_wiki"))

def test():
    model = Word2Vec.load(os.path.join("data","no_wiki"))
    print(model.most_similar(positive=['blomst']))


if __name__ == "__main__":
    train_w2v()
    test()


