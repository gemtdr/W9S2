def check_File(filename):
    pass

if __name__ == "__main__":

    dataDict = {}

    fileName = input("Enter the name of a file to open ==> ")

    with ('testScoreData.txt') as inFile: #Error 1
        
        lines = inFile.readlines()
        
        for i in lines: #Error 2
            i = i[:-1] #remove newline character
            i = i.split(',') 
            dataDict[i[0]] = [i][1:] 

    sort_dataDict = sorted(dataDict.keys()) #Error 3

    print('TEST SCORES SORTED')
    print()

    for value in sort_dataDict: #Error 4
        key = [k for k, v in dataDict.items() if v == value] #check for key that matches sorted value
        print(f'Name: {key[0]}, Score: {value[0]}') #output first value of each list
              

        

        
