import numpy as np
import matplotlib.pyplot as plt

def run_simulation(initial_males, initial_females, food_availability, mating_probability, simulation_years, steps_per_year):
    male_population = [initial_males]
    female_population = [initial_females]

    for year in range(1, simulation_years + 1):  # Start at year 1 for easier understanding
        # Simple simulation logic: Every year, each mating pair produces offspring
        num_mating_pairs = min(male_population[-1], female_population[-1])
        new_males = 0
        new_females = 0

        for _ in range(num_mating_pairs):
            if np.random.rand() < mating_probability:
                # Assume each successful mating results in a fixed number of offspring
                num_offspring = np.random.randint(1, 5)  # Random number of offspring
                for _ in range(num_offspring):
                    if np.random.rand() < food_availability:
                        new_females += 1  # Higher food availability favors female offspring
                    else:
                        new_males += 1

        # Update populations for the next year
        male_population.append(male_population[-1] + new_males)
        female_population.append(female_population[-1] + new_females)

        # Early termination if population exceeds 5000
        if male_population[-1] > 5000 or female_population[-1] > 5000:
            print(f"Simulation stopped early at year {year} due to population limit exceeded.")
            break

    return male_population, female_population

# Parameters
initial_males = 100
initial_females = 100
food_availability = 0.1  # Higher values favor more female offspring
mating_probability = 0.05  # Chance of mating when close
simulation_years = 100
steps_per_year = 10

# Run the simulation
male_counts, female_counts = run_simulation(initial_males, initial_females, food_availability, mating_probability, simulation_years, steps_per_year)

# Plot the results
years = np.arange(len(male_counts))
plt.figure(figsize=(10, 5))
plt.plot(years, male_counts, label='Male Population', color='blue')
plt.plot(years, female_counts, label='Female Population', color='pink')
plt.title('Population Growth Over Time')
plt.xlabel('Year')
plt.ylabel('Population')
plt.legend()
plt.grid(True)
plt.show()
