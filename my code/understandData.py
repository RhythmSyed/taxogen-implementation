pd = dict()
pd['data_dir'] = '../data/dblp/'
pd['raw/papers'] = pd['data_dir'] + 'raw/papers.txt'
pd['raw/keywords'] = pd['data_dir'] + 'raw/keywords.txt'
pd['input/embeddings'] = pd['data_dir'] + 'input/embeddings.txt'
pd['input/index'] = pd['data_dir'] + 'input/index.txt'
pd['input/keyword_cnt'] = pd['data_dir'] + 'input/keyword_cnt.txt'
pd['input/keywords'] = pd['data_dir'] + 'input/keywords.txt'
pd['input/papers'] = pd['data_dir'] + 'input/papers.txt'
pd['init/doc_ids'] = pd['data_dir'] + 'init/doc_ids.txt'


for key in pd.keys():
    if key == "data_dir":
        continue
    print("\n\n\n")
    print(key)
    fpa = open(pd[key])
    index = 0
    for linea in fpa.readlines():
        index = index + 1
        linea = linea.replace("\n", "")
        print(linea)
        if index == 10:
            break
    fpa.close()
