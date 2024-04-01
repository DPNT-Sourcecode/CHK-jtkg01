

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    offers = {'A': (3, 130), 'B': (2, 45)}

    total = 0

    sku_count = {sku: skus.count(sku) for sku in set(skus)}
    for sku, count in sku_count.items():
        if sku not in price:
            return -1

        price_per_item = price[sku]
        if sku in offers:
            offer_quantity, offer_price = offers[sku]
            offer_count = count // offer_quantity
            remaining_count = count % offer_quantity
            total += offer_count * offer_price + remaining_count * price_per_item
        else:
            total += count * price_per_item
    raise NotImplementedError()
