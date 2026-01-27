marks = {
    "Pankaj" : 288,
    "Nadu" : 189,
    "Six" :  87,
    "Musi" : 105,
    0 : "Pandu",   
}

# print(marks.items()) # give items in list in the form of tuple and for identifing tuple see this bracket().
# print(marks.keys()) # for finding key pairs.
# print(marks.values()) # for finding values pairs.
# marks.update({"Pankaj":188, "Kalu":200}) # for updating and add new pairs and value in Dictnoary
# print(marks)

# print(marks.get("Six"))
# print(marks["Six"])

print(marks.get("Six1")) # Get give none when no key present in Dict
print(marks["Six1"])     # But when you try write key name that not present in Dict it will give error