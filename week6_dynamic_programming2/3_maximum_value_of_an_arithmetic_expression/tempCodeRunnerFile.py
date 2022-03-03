arith=input()

def Max_of_arith(arith):
    numbers = []
    operator = []
    number=""
 
    for i in range(len(arith)):
        if ((arith[i].isdigit())==False):
            operator.append(arith[i])
            numbers.append(int(number))
            number=""
            
        else:
            number= number +arith[i]
    numbers.append(int(number))

             
 
 
    total_numbers = len(numbers)
   
    matrix = [[ 0 for j in range(total_numbers)] for j in range(total_numbers)]
 
    for i in range(total_numbers):
        for j in range(total_numbers):
        
            matrix[i][j] = 0
 
            if (i == j):
                matrix[i][j] = numbers[i]
 
    
    for k in range(2, total_numbers + 1):
        for i in range(total_numbers - k + 1):
            j = i + k - 1
            for k in range(i, j):
 
              
                max = 0
 
                if(operator[k] == '+'):
 
                   
                    max = matrix[i][k] + matrix[k + 1][j]
 
                if(operator[k] == '-'):
 
                   
                    max = matrix[i][k] - matrix[k + 1][j]
                elif(operator[k] == '*'):
 
                   
                    max = matrix[i][k] * matrix[k + 1][j]
 
                
                if (max > matrix[i][j]):
                    matrix[i][j] = max
 
   
    return (matrix[0][total_numbers - 1])
 
print(Max_of_arith(arith))