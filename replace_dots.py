def replace_dots(s):

    s_join = []

    for i in s:
        s_join.append(i)

    for i in s_join:
        if i == ".":
            y = s_join.index(i)
            s_join.remove(i)
            s_join.insert(y, "-")

    final_value = "".join(s_join)
   
    return final_value
    

print(replace_dots("one.two.three"))
print(replace_dots("..."))
print(replace_dots(""))
print(replace_dots("no dots"))