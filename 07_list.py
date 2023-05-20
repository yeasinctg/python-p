#--list is a order container--
#creat a list
#pets = []#empty list
pets = ["dog","cat","rabbit"]
                #positive index start-- 0,1,2
                #negative index start-- -3,-2,-1
#print(pets)

#--indexing--
#print(pets[1])


#--negative indexing-- # 
#print(pets[-3])


#--Rane of index---
#print(pets[1:3])



#--Adding item to a list---
#append-

#pets.append("elephent")
#print(pets)

#insert
#pets.insert(0,"elephent")
#print(pets)


#---delating item from a list--
#pop
#pets.pop()
#print(pets)

#remove
#pets.remove("cat")
#print(pets)



#----getting the length of a list
#print(len(pets))


#---changing an item value-----
#pets[1] = "fish"
#print(pets)

#---extending a list--
#num1 = [1,2,3]
#num2 = [4,5,6]
#num1.extend(num2)
#print(num1)

#----check if an item exict--
#membership operator----1 in , 2 not in
country = ["india","bangladesh","australia","england"]
check_item = "bangladesh" in country
print(check_item)



country = ["india","bangladesh","australia","england"]
check_item = "bangladesh" not in country
print(check_item)