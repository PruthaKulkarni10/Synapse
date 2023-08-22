jumbled_superheroes=['DocToR_sTRAngE','sPidERmaN','moON_KnigHT','caPTAIN_aMERIca','hULK']
indices=[]
decoded_names=[]

for index, i in enumerate(jumbled_superheroes):
    indices.append(index)                         #index of each element is found
    x=i.lower().replace("_"," ")                  #name is converted to lowercase and underscores are replaced with spaces
    decoded_names.append(x)

print(indices)
print(decoded_names)

get_length = lambda sequence: len(sequence)  #lambda function to get the length of a sequence

name_lengths = list(map(get_length, decoded_names))   #name_lengths list using map and the lambda function

indices.sort(key=lambda x: name_lengths[x])   # Sorting the indices list based on name_lengths

list=[decoded_names[i].title() for i in indices]   #element from decoded names list is fetched corresponding to sorted indices list

print("Phase 5 of kickoff list: ")
for x, superh in enumerate(list, start=1):
    print(f"{x}. {superh}")

