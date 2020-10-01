#Given a keypad and an n digit number, list all words which are possible by pressing these numbers.


hashTable = ["", "", "abc", "def", "ghi", "jkl",  
                    "mno", "pqrs", "tuv", "wxyz"] 
                    
def printWordsUtil(number, curr, output, n): 
    if(curr == n): 
        print(output) 
        return
          


    for i in range(len(hashTable[number[curr]])): 
        output.append(hashTable[number[curr]][i]) 
        printWordsUtil(number, curr + 1, output, n) 
        output.pop() 
        if(number[curr] == 0 or number[curr] == 1): 
            return;  
              
def printWords(number, n): 
    printWordsUtil(number, 0, [], n) 
      

if __name__ == '__main__': 
    number = [2, 3, 4] 
    n = len(number) 
    printWords(number, n); 
    
'''
output for the above input:
adg adh adi aeg aeh aei afg afh 
afi bdg bdh bdi beg beh bei bfg 
bfh bfi cdg cdh cdi ceg ceh cei 
cfg cfh cfi
'''
