alphabet = [
    # a - j
        "100000",
        "110000",
        "100100",
        "100110",
        "100010",
        "110100",
        "110110",
        "110010",
        "010100",
        "010110",
    # k - t
        "101000",
        "111000",
        "101100",
        "101110",
        "101010",
        "111100",
        "111110",
        "111010",
        "011100",
        "011110",
    # u - z
        "101001",
        "111001",
        "010111", # w is weird
        "101101",
        "101111",
        "101011",
    ]



def solution(s):
    new_s = ""
    s_lower = [str.islower(letter) for letter in s]
    s = str.lower(s)
    s = [ord(letter) - 97 for letter in s]
    print(s)
    for i in range(len(s)):
        if s[i] < 0: # space
            print("space")
            new_s += "000000"
        else:
            if not s_lower[i]:
                new_s += "000001"
            new_s += alphabet[s[i]]
        print(new_s)
    return new_s