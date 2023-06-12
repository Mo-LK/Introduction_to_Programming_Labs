def combine_dic(dic_1, dic_2):
    # combine dic_1 et dic_2 en gardant la valeur max en cas de clef commune
    dic_3 = dic_1.copy()
    for key in dic_2:
        if key not in dic_3:
            dic_3[key] = dic_2[key]
        else:
            dic_3[key] = max(dic_1[key], dic_2[key])

    return dic_3

if __name__ == '__main__':
    # Combinaison de dictionnaire
    dic_1 = {'a': 5, 'b': 2, 'c': 9}
    dic_2 = {'a': 1, 'b': 8, 'd': 17}

    dic_3 = combine_dic(dic_1,dic_2)
    print(dic_3)
