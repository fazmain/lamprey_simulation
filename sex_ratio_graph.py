import numpy as np
import matplotlib.pyplot as plt

def run_simulation_with_sex_ratio(initial_males, initial_females, food_availability, mating_probability, simulation_years, steps_per_year):
    male_population = [initial_males]
    female_population = [initial_females]
    sex_ratios = [initial_males / initial_females if initial_females > 0 else np.inf]  # Avoid division by zero

    for year in range(1, simulation_years + 1):  # Start at year 1 for easier understanding
        num_mating_pairs = min(male_population[-1], female_population[-1])
        new_males = 0
        new_females = 0

        for _ in range(num_mating_pairs):
            if np.random.rand() < mating_probability:
                num_offspring = np.random.randint(1, 5)  # Random number of offspring
                for _ in range(num_offspring):
                    if np.random.rand() < food_availability:
                        new_females += 1
                    else:
                        new_males += 1

        # Update populations for the next year
        updated_males = male_population[-1] + new_males
        updated_females = female_population[-1] + new_females
        male_population.append(updated_males)
        female_population.append(updated_females)

        # Calculate and store the sex ratio for the year
        current_sex_ratio = updated_males / updated_females if updated_females > 0 else np.inf
        sex_ratios.append(current_sex_ratio)

        # Early termination if population exceeds 5000
        if updated_males > 5000 or updated_females > 5000:
            print(f"Simulation stopped early at year {year} due to population limit exceeded.")
            break

    return male_population, female_population, sex_ratios

# Parameters
initial_males = 10
initial_females = 10
food_availability = 0.1
mating_probability = 0.01
simulation_years = 100
steps_per_year = 10

# Run the simulation and get sex ratios over time
male_counts, female_counts, sex_ratios = run_simulation_with_sex_ratio(initial_males, initial_females, food_availability, mating_probability, simulation_years, steps_per_year)

# Plotting the sex ratio over time
years = np.arange(len(sex_ratios))
plt.figure(figsize=(10, 5))
plt.plot(years, sex_ratios, label='Sex Ratio (Males/Females)', color='green')
plt.title('Sex Ratio Over Time')
plt.xlabel('Year')
plt.ylabel('Sex Ratio')
plt.legend()
plt.grid(True)
plt.show()
