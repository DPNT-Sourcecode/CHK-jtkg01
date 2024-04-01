

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
    offers = {'A': [(5, 200), (3, 130)], 'B': [(2, 45)], 'E': [(2, 'B')]}

    total = 0

    sku_count = {sku: skus.count(sku) for sku in set(skus)}
    for sku, count in sku_count.items():
        if sku in offers:
            offer = offers[sku]
            if isinstance(offer[0][1], int):
                for offer_count, offer_price in offer:
                    while sku_count[sku] >= offer_count:
                        total += offer_price
                        sku_count[sku] -= offer_count
            else:
                free_offer = offer[0][1]
                while sku_count[sku] >= 2:
                    total += price[sku] * 2
                    sku_count[sku] -= 2
                    sku_count[free_offer] -= 1
    for sku, count in sku_count.items():
        total += price[sku] * count

    return total if all(count >= 0 for count in sku_count.values()) else -1


