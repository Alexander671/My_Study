def huffman_decode(s, d):  
    sub_string = ""
    while len(s) != 0:
        if sub_string in d:
            print(d[sub_string], end='')
            s = s[len(sub_string):]
            sub_string = ""
        sub_string = s[:len(sub_string) + 1]
        
def main():
    alphabet_length, _ = map(int, input().split())
    codes = { v : k for k, v in (input().split(': ') for _ in range(alphabet_length)) }

    s = input() 
    huffman_decode(s, codes) 
    
if __name__ == "__main__":
    main()