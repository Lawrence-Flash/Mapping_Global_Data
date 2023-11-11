import json

def main():
    display_population()

def display_population():
        # Load the data into a list
    filename = 'population_data.json'
    with open(filename) as file:
        pop_data = json.load(file)
        
    # Print the 2010 population for each country
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            print(f"{country_name}: {str(population)}")

main()