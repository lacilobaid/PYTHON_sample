# Yasasın indian youtubers
def manuel_sort(dizi, indeks1,indeks2):
    i = indeks1 - 1
    pivot = dizi[indeks2]
    for j in range(indeks1, indeks2):
        if dizi[j] <= pivot:
            i += 1
            dizi[i], dizi[j] = dizi[j], dizi[i]
    dizi[i+1], dizi[indeks2] = dizi[indeks2], dizi[i+1]
    return i+1

def ikinci(dizi, indeks1, indeks2):
    if indeks1 < indeks2:
        pivot = manuel_sort(dizi, indeks1, indeks2)
        ikinci(dizi, indeks1, pivot-1)
        ikinci(dizi, pivot + 1, indeks2)

# Yasasın indian youtubers
def manuel_sort_tersten(dizi, indeks1,indeks2):
    i = indeks1 - 1
    pivot = dizi[indeks2]
    for j in range(indeks1, indeks2):
        if dizi[j] >= pivot:
            i += 1
            dizi[i], dizi[j] = dizi[j], dizi[i]
    dizi[i+1], dizi[indeks2] = dizi[indeks2], dizi[i+1]
    return i+1

def ikinci_tersten(dizi, indeks1, indeks2):
    if indeks1 < indeks2:
        pivot = manuel_sort_tersten(dizi, indeks1, indeks2)
        ikinci_tersten(dizi, indeks1, pivot-1)
        ikinci_tersten(dizi, pivot + 1, indeks2)
