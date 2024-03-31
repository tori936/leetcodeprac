from typing import List
class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        encoding_data = "$0"
        index=0
        for word in strs:
            index+=len(word)
            encoded_string+=word
            encoding_data+= "_"+str(index)
        encoded_string+=encoding_data
        return encoded_string
            
    def decode(self, s: str) -> List[str]:
        partition_character = "$"
        data=str.rpartition(partition_character)
        print(data[0])
        print(data[2])
        return ""
Input= ["neet","code","love","you"]
test_sol = Solution()
encoded_str = test_sol.encode(Input)
print(encoded_str)
test_sol.decode(encoded_str)