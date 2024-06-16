file = open('table.txt','w')
n = int(input("How many tables do you want to print? = "))
for i in range(n):
    table_number = int(input("Which number of table you want to print? = "))
    for i in range(1,11):
        result = f"{table_number} * {i} = {table_number*i}\n"
     
        print(result)
        file.write(result)


