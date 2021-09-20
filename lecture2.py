
from typing import List

def count(s:str)->int:    
    if len(s)==0:
        return 0

    ans=count(s[1:])
    if s[0]=='x':
        ans+=1

    return ans

print(count("xxxixieelewxx3442"))

def sumofDigit(num:int)->int:
    if(num==0):
        return 0
    ans=sumofDigit(num//10)
    ans+=num%10
    return ans


print(sumofDigit(1232322))


#First Occurence

def FirstOccurence(s:str,ch:str,index:int)->int:

    if index==len(s):
        return -1
    
    if s[index]==ch:
        return index
    
    ans=FirstOccurence(s,ch,index+1)
    return ans



print(FirstOccurence("eweweeefddfddw","d",0))
    

#last Occurence

def LastOccurence(s:str,index:int,ch:str):
    
     if index==len(s):
         return -1


     ans=LastOccurence(s,index+1,ch)

     if s[index]==ch and ans==-1:
         return index

     return ans

print(LastOccurence("eweweeefddfddw",0,"a"))



# All Occurence

def AllOccurence(s:str,index:int,ch:str,count:int)->List[int]:
    
   
   if s[index]==ch:
       count+=1

   ans=[]
   ans.append(AllOccurence(s,index+1,ch,count))
