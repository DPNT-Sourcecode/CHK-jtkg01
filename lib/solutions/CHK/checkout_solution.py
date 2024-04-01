

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
    offers = {'A': [(5, 200), (3, 130)], 'B': [(2, 45)], 'E': [(2, 'B')]}

    total = 0

    sku_count = {sku: skus.count(sku) for sku in set(skus)}
    for sku, count in sku_count.items():
        if sku not in price:
            return -1

        price_per_item = price[sku]
        if sku in offers:
            for offer in offers[sku]:
                if isinstance(offer[1], int):
                    offer_count, offer_price = offer
                    offer_deal = (count // offer_count) * offer_price
                    total += (count // offer_count) * offer_price
                    count %= offer_count
                else:
                    offer_count, offer_sku = offer
                    if offer_sku in sku_count and sku_count[offer_sku] >= offer_count //:
                        total += (count - count // offer_count) * price_per_item
                    else:
                        total += count * price_per_item
                    break

    return total



