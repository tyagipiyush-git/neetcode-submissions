class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''

        for char in strs:
            encoded_str = encoded_str+str(len(char))+';'+char
        
        return encoded_str
        

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        str_len = len(s)
        print(str_len)
        i =0
        while i < str_len:
            j = i
            while s[j] != ';':
                j+=1

            char_len = int(s[i:j])
            
            decoded_str.append(s[j+1:j+1+char_len])

            i = j+1+char_len

        return decoded_str
