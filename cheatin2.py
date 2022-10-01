Data = ['D', 'o', 'I', 't', '@', '1', '2', '3', '!']
for i in range(len(Data)-1):
    if (Data[i].isupper()):
        Data[i]=Data[i].lower()
    elif (Data[i].isspace()):
        Data[i]=Data[i+1]
print(Data)