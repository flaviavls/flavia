def matrice():
    n = 4
    matrice = [[0] * n for n in range(n)]
    sdp = 0
    sds = 0

    for i in range(n):
        for j in range(n):
            matrice[i][j] = int(input())
            if i < j:  # sunt deasupra diagonalei principale
                sdp = sdp + matrice[i][j]
            if i + j < n - 1:  # sunt deasupra diagonalei secundare
                sds = sds + matrice[i][j]

    print(sdp)
    print(sds)


if __name__ == "__main__":
    matrice()
