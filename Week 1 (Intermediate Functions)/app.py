def student_score_calc(*scores, **config):
    bonus = config.get('bonus', 0)
    weight = config.get('weight', 0)

    # Calculate total with bonus
    current_sum = sum(scores)
    total = current_sum + bonus

    divisor = len(scores) + weight
    weighted_average = total / divisor if divisor > 0 else 0

    return {
        "total": total,
        "average": weighted_average
    }

def main():
    print("--- Student Score Calculator ---")
    
    # Initialize the list inside the main scope
    scores = [] 

    # Handle input locally to avoid scope issues
    while True:
        add_more = input("Add score? (y/n): ").strip().lower()
        if add_more == 'y':
            try:
                val = float(input("Enter a score: "))
                scores.append(val)
            except ValueError:
                print("Invalid number.")
        elif add_more == 'n':
            break
        else:
            print("Please enter 'y' or 'n'.")

    # Handle defaults for config using 'or' logic
    try:
        b_input = input("Enter bonus score (default 0): ")
        bonus = float(b_input) if b_input else 0.0
        
        w_input = input("Enter weight factor (default 0): ")
        weight = float(w_input) if w_input else 0.0
    except ValueError:
        print("Invalid config input, using defaults.")
        bonus, weight = 0.0, 0.0

    config = {
        'bonus': bonus,
        'weight': weight
    }

    # Unpack scores and config values
    if scores:
        result = student_score_calc(*scores, **config)
        print(f"\nResults:\nTotal Score: {result['total']}\nAverage: {result['average']:.2f}")
    else:
        print("No scores were entered.")

if __name__ == "__main__":
    main()