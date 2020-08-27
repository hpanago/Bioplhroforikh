RNA="AGCAGCGGCCAGGCGACGAAACUUACUAU"
array_length=len(RNA)
RNA_array=[]
for i in RNA:
    RNA_array.append(i)
print(RNA_array)
position=0

dict_pairs={"AU":0,"UU":0,"UA":0,"GG":0,"CC":0,"AA":0,"CG":0,"GC":0,"CA":0,"AC":0,"CU":0,"UC":0,"GA":0,"AG":0,"UG":0,"GU":0}

#print(dict_pairs["AG"])

dict_pairs_max=0

while position<(array_length-1):
#    print(position)
#    print(RNA_array[position])
    pair=RNA_array[position]+RNA_array[position+1]
    #print(pair)
    dict_pairs[pair]+=1
    if dict_pairs[pair]>dict_pairs_max:
        dict_pairs_max=dict_pairs[pair]
        string_to_print="The max number of non-alternating bonds is: {} for the pair: {}".format(str(dict_pairs_max),pair)
    position+=1
#print(dict_pairs)

print(string_to_print)
