
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
    offers = {'A': [(5, 200), (3, 130)], 'B': [(2, 45)], 'E': [(2, 'B')]}

    total = 0


    if any(sku not in price for sku in skus):
        return -1

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
                special_offer, free_offer = offer[0]
                while sku_count[sku] >= special_offer:
                    total += price[sku] * special_offer
                    sku_count[sku] -= special_offer
                    if free_offer in sku_count:
                        sku_count[free_offer] -= 1

    for sku, count in sku_count.items():
        total += price[sku] * count

    return total

