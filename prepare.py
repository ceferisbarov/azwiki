# # from gensim.test.utils import datapath
# # from gensim.corpora import WikiCorpus

# # path_to_wiki_dump = datapath("/home/jafar/playground/nanoGPT/data/azwiki/azwiki-latest-pages-articles.xml.bz2")

# # for vec in WikiCorpus(path_to_wiki_dump):
# #     print(vec)
# #     break
# import os
# from wiki_dump_reader import Cleaner, iterate

# output_folder = "raw"
# cleaner = Cleaner()

# counter = 0
# for id, (title, text) in enumerate(iterate("azwiki-latest-pages-articles.xml")):
#     counter += 1
#     text = cleaner.clean_text(text)

#     filename = str(id) + "_" + title.replace(" ", "_").replace("/","~") + ".txt"
#     filepath = os.path.join(output_folder, filename)
#     with open(filepath, "w") as f:
#         f.write(text)

#     if id == 39952:
#         print(text)
