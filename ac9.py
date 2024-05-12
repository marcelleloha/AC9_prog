def folhas_necessarias(c, f, p):
    num_folhas = c * f
    if num_folhas <= p:
        return "S"
    else:
        return "N"

c, p, f = map(int, input().split())
print(folhas_necessarias(c, f, p))
