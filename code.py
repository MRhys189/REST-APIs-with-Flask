def missing_char(str: str, n: int):
    for letter in str:
        while n == str.index(letter):
            str.replace(letter, "")
            return str


print(missing_char("kitten", 1))


# n = "james"
# print(n.find("j"))


# m = "my name is rhys"
# print(m[1])
