class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # build the next array off of the last array
        row = [1]
        
        if rowIndex == 0:
            return row
        
        for _ in range(rowIndex):
            new = []
            
            new.append(1)
            
            for i in range(1,len(row)):
                new.append(row[i-1]+row[i])
            
            new.append(1)
            row = new
        
        return row