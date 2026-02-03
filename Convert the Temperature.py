class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        y=(celsius*9/5)+32
        r1=round(y,5)
        k=273.15+celsius
        r2=round(k,5)
        return [r2,r1]
        
