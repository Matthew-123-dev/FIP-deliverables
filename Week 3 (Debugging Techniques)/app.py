



# Prices are now in Nigerian Naira (₦)
items = {
    "Wireless Noise-Cancelling Headphones": 250000.00,
    "Bluetooth Earbuds": 150000.00,
    "Portable Charger": 80000.00,
    "Smartwatch": 200000.00,
    "Fitness Tracker": 120000.00,
    "VR Headset": 3000000.00,
    "Stainless Steel Chef Knife 8\"": 400000.00,
    "Laptop Backpack (water-resistant)": 350000.00,
    "Electric Kettle": 90000.00,
    "Air Fryer": 750000.00,
    "Wireless Charging Pad": 300000.00,
    "Reusable Water Bottle 26oz": 150000.00,
    "Yoga Mat 6mm": 250000.00,
    "Extra Virgin Olive Oil 500ml": 75000.00,
    "Ceramic Dinner Plate (set of 4)": 350000.00,
}

import logging
from io import StringIO
import pdb

# Configure logging
logger = logging.getLogger("checkout")
logger.setLevel(logging.DEBUG)
fmt = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(fmt)
logger.addHandler(ch)
fh = logging.FileHandler('checkout.log')
fh.setFormatter(fmt)
logger.addHandler(fh)


def calculate_subtotal(cart):
    """Calculate subtotal (in Naira) for the given cart dict: {item_name: qty}.
    Returns (subtotal_naira, line_items)"""
    line_items = []
    subtotal = 0.0
    for name, qty in cart.items():
        price = items.get(name)
        if price is None:
            logger.error(f"Unknown item in cart: %s", name)
            continue
        line_total = price * qty
        line_items.append((name, qty, price, line_total))
        subtotal += line_total
    logger.debug("Calculated subtotal: ₦%.2f", subtotal)
    return subtotal, line_items


def apply_discount(total_naira, code=None):
    """Apply discount and return (discount_amount_naira, new_total_naira).

    Intentional bug: percentage discounts are mis-calculated by multiplying
    the percentage value by 100 again.
    """
    if not code:
        return 0.0, total_naira

    # Discount definitions: percentage (fraction) or fixed amount in Naira
    discounts = {
        'TENPERCENT': 0.10,
        'FIVEOFF': 5000.00,  # ₦5,000 off
    }

    val = discounts.get(code)
    if val is None:
        logger.error("Invalid discount code: %s", code)
        return 0.0, total_naira

    if isinstance(val, float) and val < 1:
        # Bug: multiplying by 100 twice — wrong discount calculation
        discount_amount = total_naira * (val * 100)
        logger.debug("(BUG) Applying percentage discount: code=%s raw_fraction=%s computed_amount_naira=₦%.2f", code, val, discount_amount)
    else:
        discount_amount = val
        logger.debug("Applying fixed discount: code=%s amount_naira=₦%.2f", code, discount_amount)

    new_total = max(0.0, total_naira - discount_amount)
    logger.info("Discount applied: ₦%.2f, new total: ₦%.2f", discount_amount, new_total)
    return discount_amount, new_total


def format_naira(naira):
    return f"₦{naira:,.2f}"


def checkout(cart, discount_code=None):
    subtotal, lines = calculate_subtotal(cart)
    logger.info("Cart subtotal: %s", format_naira(subtotal))
    for name, qty, price, line_total in lines:
        logger.debug("Line: %s x%s @ %s => %s", name, qty, format_naira(price), format_naira(line_total))

    discount_amount, total_after = apply_discount(subtotal, discount_code)
    logger.info("Final total: %s (discount: %s)", format_naira(total_after), format_naira(discount_amount))
    return {
        'subtotal_naira': subtotal,
        'discount_naira': discount_amount,
        'total_naira': total_after,
        'lines': lines,
    }


def checkout_demo():
    # Example cart
    cart = {
        'Wireless Noise-Cancelling Headphones': 1,
        'Portable Charger': 2,
        'Yoga Mat 6mm': 1,
    }
    # Intentionally use the percentage discount to trigger the bug
    result = checkout(cart, discount_code='TENPERCENT')
    print('\nSummary:')
    print('Subtotal:', format_naira(result['subtotal_naira']))
    print('Discount:', format_naira(result['discount_naira']))
    print('Total:', format_naira(result['total_naira']))


def automated_pdb_run():
    """Run a non-interactive pdb session with predefined commands to step
    through the checkout flow and print the debugger transcript.
    """
    commands = [
        'n',  # step into calculate_subtotal
        'n',  # proceed
        'n',  # proceed
        'p subtotal',
        'n',
        'p total_naira',
        'n',
        'p val',
        'n',
        'p discount_amount',
        'q',
    ]

    stdin = StringIO('\n'.join(commands) + '\n')
    out = StringIO()
    debugger = pdb.Pdb(stdin=stdin, stdout=out)

    # We'll run the checkout_demo under the debugger so the transcript shows key vars
    try:
        debugger.runcall(checkout_demo)
    except SystemExit:
        # pdb 'q' raises SystemExit — ignore to capture transcript
        pass

    transcript = out.getvalue()
    logger.info('Automated pdb session transcript:\n%s', transcript)
    print('\n--- pdb transcript (truncated) ---')
    for line in transcript.splitlines()[:60]:
        print(line)


if __name__ == '__main__':
    # Run demo and then an automated pdb session that steps through the flow
    checkout_demo()
    automated_pdb_run()


