colorList = ["white","red","black","blue"]
numberList = [1,1,4,2,3]

#add
colorList.append("pink")

#travel the list
for temp in colorList:
    print(temp)

print(colorList[0])

# for(i=0;color.len;i++) -- this is the JS
    # let temp = color[i]
# console.log(temp)

#dictionary
me={
    "first_name":"Adrian",
    "month":"july",
    "last_name":"Aguinaga",
    "age":37,    
}
print(me["first_name"])

me["age"] = 99
me["color"]="Blue"
print(me)