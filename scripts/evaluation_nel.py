
def precision_at_k(golden_cui_ds, candidate_ids_ds):
        total_entities = 0
        correct_at_1 = 0
        correct_at_2 = 0
        correct_at_5 = 0
        for golden_cui, candidate_ids in zip(golden_cui_ds, candidate_ids_ds):

                if check_label(golden_cui = golden_cui , predicted_cuis= candidate_ids, k=1 ):
                        correct_at_1 += 1
                if check_label(golden_cui = golden_cui , predicted_cuis= candidate_ids, k=2 ):
                        correct_at_2 += 1
                if check_label(golden_cui = golden_cui , predicted_cuis= candidate_ids, k=5 ):
                        correct_at_5 += 1

                total_entities += 1
                
        precision_at_1 = correct_at_1 / total_entities
        precision_at_2 = correct_at_2 / total_entities
        precision_at_5 = correct_at_5 / total_entities
        
        print("Total entities: ", total_entities)
        print(
                "Correct at 1: ", correct_at_1, "Precision at 1: ", precision_at_1
        )
        print(
                "Correct at 2: ", correct_at_2, "Precision at 2: ", precision_at_2
        )
        print(
                "Correct at 5: ",
                correct_at_5,
                "Precision at 5: ",
                precision_at_5,
                )
        return precision_at_1, precision_at_2, precision_at_5


def check_label(golden_cui:str , predicted_cuis:list, k:int ):
    """
    Some composite annotation didn't consider orders
    So, return True if any cui is matched within composite cui (or single cui)
    Otherwise, return False
    """
    result = []
    for predicted_cui in predicted_cuis[:k]:
        ans = len(set(predicted_cui.split("|")).intersection(set(golden_cui.split("|")))) > 0
        result.append(ans)
    
    return any(result)

if __name__ =="__main__":
    
    golden_cui_ds = ["C200"]    # list of correct cuis 
    
    candidate_ids_ds = [["C100", "C200", "C500|C600"]] 
    # nested list: where each list contains topk linked entites
    # a surface form can have more than one cui which are joined by | such as "C500|C600"
    # prediction is considered correct if any of the cui matches

    precision_at_k(golden_cui_ds, candidate_ids_ds)