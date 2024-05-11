"""
Have the function GasStation(strArr) take strArr which will be an an array consisting of the 
following elements: N which will be the number of gas stations in a circular route and each 
subsequent element will be the string g:c where g is the amount of gas in gallons at that gas 
station and c will be the amount of gallons of gas needed to get to the following gas station.

For example strArr may be: ["4","3:1","2:2","1:2","0:1"]. Your goal is to return the index of the 
starting gas station that will allow you to travel around the whole route once, otherwise return 
the string impossible. For the example above, there are 4 gas stations, and your program should 
return the string 1 because starting at station 1 you receive 3 gallons of gas and spend 1 getting 
to the next station. Then you have 2 gallons + 2 more at the next station and you spend 2 
so you have 2 gallons when you get to the 3rd station. You then have 3 but you spend 2 getting 
to the final station, and at the final station you receive 0 gallons and you spend your final 
gallon getting to your starting point. Starting at any other gas station would make getting 
around the route impossible, so the answer is 1. If there are multiple gas stations that are 
possible to start at, return the smallest index (of the gas station). N will be >= 2.

Examples
Input: ["4","1:1","2:2","1:2","0:1"]
Output: impossible
Input: ["4","0:1","2:2","1:2","3:1"]
Output: 4
"""

# chatgpt solution
def GasStation(strArr):
    # Convertendo a string de entrada em uma lista de dicionários
    gas_stations = []
    for station in strArr[1:]:
        gas, cost = map(int, station.split(':'))
        gas_stations.append({'gas': gas, 'cost': cost})

    # Loop através de cada posto de gasolina como ponto de partida potencial
    for start in range(len(gas_stations)):
        fuel = 0
        possible = True
        
        # Viajar ao redor da rota circular
        for i in range(start, start + len(gas_stations)):
            station = gas_stations[i % len(gas_stations)]
            fuel += station['gas'] - station['cost']
            
            # Se o combustível ficar negativo em algum ponto, a rota é impossível
            if fuel < 0:
                possible = False
                break
        
        # Se a rota for possível a partir do ponto de partida atual, retorne o índice
        if possible:
            return start + 1  # Adicionando 1 para converter para índice baseado em 1
    
    # Se nenhum ponto de partida permitir viajar ao redor da rota, retorne "impossível"
    return "impossível"

# Mantenha esta chamada de função para o código do usuário
print(GasStation(input()))
