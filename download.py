import os
import wget
from wget import bar_thermometer
os.makedirs("data",exist_ok=True)

if not(os.path.isfile(os.path.join("data","nowiki-20170620-pages-articles.xml.bz2"))):
    wget.download("https://dumps.wikimedia.org/nowiki/20170620/nowiki-20170620-pages-articles.xml.bz2",out="data", bar=bar_thermometer)