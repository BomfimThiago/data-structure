
if __name__ == "__main__":
    n = int(input().strip())
    d = {}

    for _ in range(n):
        tupl = tuple(input().rstrip().split())
        d[tupl[0]] = tupl[1]

    queries = []

    while True:
        name = input()
        if not name.strip():  # Verifica se a linha está em branco
            break

        if name in d:
            r = f"{name}={d[name]}"
            f = lambda: print(r)
        else:
            f = lambda: print("Not found")

        queries.append(f)

    for query in queries:
        query()
