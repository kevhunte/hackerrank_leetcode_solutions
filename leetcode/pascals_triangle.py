class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        
        if numRows == 1:
            return output
        
        for i in range(1,numRows):
            last_layer = output[i-1]
            layer = []
            layer.append(1)
            
            for j in range(1,len(last_layer)):
                layer.append(last_layer[j-1]+last_layer[j])
            
            layer.append(1)
            output.append(layer)
            
        return output