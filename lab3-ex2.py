# A certain number of flights connect s cities. You are provided an array of flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei. You are also given three integers start, destination, and k. Start represents the start point of the graph and destination represents the city where you want to fly. The variable k represents the number of stops that are allowed to be done. Return message  no route if there is no such route.

n = int(input("n = "))
flights = eval(input("flights = "))
start = int(input("start = "))
destination = int(input("destination = "))
k = int(input("k = "))


prices = [float("inf") for _ in range(n)]
prices[start] = 0

for _ in range(k + 1):
    temp_prices = list(prices)
    for source, dest, price in flights:
        flight_price = prices[source] + price
        if flight_price < temp_prices[dest]:
            temp_prices[dest] = flight_price
    prices = temp_prices

if prices[destination] != float("inf"):
    print(prices[destination])
else:
    print("Undefined")
