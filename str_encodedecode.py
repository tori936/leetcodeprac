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
        data=s.rpartition(partition_character)
        split_indices=[int(x) for x in data[2].split("_")]
        res=[]
        current_index=0
        for i in split_indices[1::]:
            word = data[0][current_index:i:1]
            current_index=i
            res.append(word)
        return res