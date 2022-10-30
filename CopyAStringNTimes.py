def copy(str, n):
    result = ""
    for i in range(n):
        if i == n-1:
            result += str + "."
        else:
            result += str + ", "
    return result


print(copy("low", 5))
