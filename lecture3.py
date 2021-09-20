def permutations(str:str,ans:str)->int:
    
    if len(str)==0:
        print(ans)
        return 1
    
    
    count=0
    for i in range(len(str)):
       count+=permutations(str[0:i]+str[i+1:],ans+str[i])

    return count

def permutations(str:str)->list(str):
    return []
 

print(permutations("abc",""))


  


