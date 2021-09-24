def permutations(str:str,ans:str)->int:
    
    if len(str)==0:
        print(ans)
        return 1
    
    
    count=0
    for i in range(len(str)):
       count+=permutations(str[0:i]+str[i+1:],ans+str[i])

    return count

def permutations(str:str,index:int):
    
    if len(str)==0:
        base=[]
        base.append("")
        return base

    myAns=[]
    recAns=permutations(str[1:],index+1)
                                                                    # including Current Character
    myAns.extend(recAns)                                            # Excluding Current Character
    
    return myAns
 

print(permutations("abc",0))



  


