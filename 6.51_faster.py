def calculate(RNA):
    array_length=len(RNA)
    RNA_array=[]
    for i in RNA:
        RNA_array.append(i)
    position=0
    
    dict_pairs={"AU":0,"UU":0,"UA":0,"GG":0,"CC":0,"AA":0,"CG":0,"GC":0,"CA":0,"AC":0,"CU":0,"UC":0,"GA":0,"AG":0,"UG":0,"GU":0}
    
    
    dict_pairs_max=0
    
    while position<(array_length-1):
        pair=RNA_array[position]+RNA_array[position+1]
        dict_pairs[pair]+=1
        if dict_pairs[pair]>dict_pairs_max:
            dict_pairs_max=dict_pairs[pair]
            string_to_print="The max number of non-alternating bonds is: {} for the pair: {}".format(str(dict_pairs_max),pair)
        position+=1
    
    return string_to_print

RNA="AGCAGCGGCCAGGCGACGAAACUUACUAU"
print("A first example will be with the RNA: {}".format(RNA))
print(calculate(RNA)+"\n")
RNA1="AUGGCCAUGGCGC"
print("A second example will be with the RNA: {}".format(RNA1))
print(calculate(RNA1)+"\n")
RNA2="AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
print("A third example will be with the RNA: {}".format(RNA2))
print(calculate(RNA2)+"\n")
RNA3="AUGGGU"
print("A forth example will be with the RNA: {}".format(RNA3))
print(calculate(RNA3)+"\n")
