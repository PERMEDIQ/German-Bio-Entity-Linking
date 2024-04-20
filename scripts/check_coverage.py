from tqdm import tqdm
from collections import defaultdict

def coverage(kb_path):
    "check if query cui is in kb cui or not. description of cui is not considered"
    

    cui_name_map_kb = defaultdict(set)

    with open(kb_path, encoding="utf-8") as file:
        for line in file:
            cuis, desc = line.strip("\n").split("||")
            for cui in cuis.split("|"):
                cui_name_map_kb[cui].add(desc.lower())
                
                
    for query_path in [
                        "data/de_1k_test_query.txt",
                    "data/de_wikimed_bel_train_query.txt",
                    "data/de_wikimed_bel_dev_query.txt",
                    "data/de_wikimed_bel_test_query.txt",
                    ]:

        print(query_path)
        query_tuples = []
        cui_name_map_query = defaultdict(set)
        with open(query_path, encoding="utf-8") as file:
            for line in file:
                cuis, desc = line.strip("\n").split("||")
                query_tuples.append((cuis, desc.lower()))
                for cui in cuis.split("|"):
                    cui_name_map_query[cui].add(desc.lower())
        
        
        counter = 0
        for query_cuis, _ in tqdm(query_tuples):
            
            for query_cui in query_cuis.split("|"):
                if query_cui in cui_name_map_kb:
                    counter += 1
                    break
                
                
        print(f'Query Samples {len(query_tuples)}')
        print(f'Linked Samples {counter}')
    
        print(f'Coverage {counter / len(query_tuples)}')
        

def coverage_with_alias(kb_path):
    """For a cui in query data, query decription should be
    in the kb descriptions or aliases for that cui in the KB """
    
    cui_name_map_kb = defaultdict(set)

    with open(kb_path, encoding="utf-8") as file:
        for line in file:
            cuis, desc = line.strip("\n").split("||")
            for cui in cuis.split("|"):
                cui_name_map_kb[cui].add(desc.lower())
                
                
    for query_path in [
                    "data/de_1k_test_query.txt",
                   "data/de_wikimed_bel_train_query.txt",
                   "data/de_wikimed_bel_dev_query.txt",
                   "data/de_wikimed_bel_test_query.txt",
                   ]:

        print(query_path)
        query_tuples = []
        cui_name_map_query = defaultdict(set)
        with open(query_path, encoding="utf-8") as file:
            for line in file:
                cuis, desc = line.strip("\n").split("||")
                query_tuples.append((cuis, desc.lower()))
                
        
        
        counter = 0
        for query_cuis, query_name in tqdm(query_tuples):
            kb_names = set()
            query_names = set()
            query_names.add(query_name)
            
            for query_cui in query_cuis.split("|"):
                
                
                kb_names.update(cui_name_map_kb.get(query_cui, set()))
                
            
            
            if len(kb_names.intersection(query_names)) > 0:
                counter += 1
            else:
                # print("Not matched")
                # print(kb_names)
                # print(query_names)
                # print("+++++++")
                
                # for query_cui in query_cuis.split("|"):
                        
                #         print(query_cui)
                #         print(cui_name_map_kb[query_cui])
                #         print(cui_name_map_query[query_cui])
                #         print("------------------")
                pass
            
                
                
        print(f'Query Samples {len(query_tuples)}')
        print(f'Linked Samples {counter}')
    
        print(f'Coverage {counter / len(query_tuples)}')

if __name__ == "__main__":
    for kb_path in ["data/qids_with_cui_kb.txt","data/umls_onto_all_lang_cased_wikimed_only_399931.txt" ]:
        print(f"Coverage for KB = {kb_path}")
        print("="*40)
        # coverage(kb_path)
        coverage_with_alias(kb_path)
            


            
