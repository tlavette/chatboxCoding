def calculate_materials_cost(receptacles, switches, gfis, twelve_two_wire_ft, number_eight_wire_ft):
    # Define costs
    cost_receptacle = 1.50
    cost_switch = 1.00
    cost_gfi = 23.00
    cost_twelve_two_wire_per_15ft = 30.00
    cost_number_eight_wire_per_100ft = 140.00
    
    # Calculate total costs
    total_receptacles = receptacles * cost_receptacle
    total_switches = switches * cost_switch
    total_gfis = gfis * cost_gfi
    total_twelve_two_wire = (twelve_two_wire_ft / 15) * cost_twelve_two_wire_per_15ft
    total_number_eight_wire = (number_eight_wire_ft / 100) * cost_number_eight_wire_per_100ft
    
    # Sum total costs
    total_cost = total_receptacles + total_switches + total_gfis + total_twelve_two_wire + total_number_eight_wire
    return total_cost

def main():
    # Get user input
    receptacles = int(input("Enter the number of receptacles: "))
    switches = int(input("Enter the number of switches: "))
    gfis = int(input("Enter the number of GFIs: "))
    twelve_two_wire_ft = float(input("Enter the length of TwelveTwo wire in feet: "))
    number_eight_wire_ft = float(input("Enter the length of NumberEight wire in feet: "))
    
    # Calculate the total cost
    total_cost = calculate_materials_cost(receptacles, switches, gfis, twelve_two_wire_ft, number_eight_wire_ft)
    
    # Print the result
    print(f"Your total estimate for materials is: ${total_cost:.2f}")

if __name__ == "__main__":
    main()