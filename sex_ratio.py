import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
initial_males = 10
initial_females = 10
food_availability = 0.8  # Influences offspring sex ratio, higher means more females
mating_probability = 0.05  # Chance of mating when close
simulation_steps = 1000  # Increased to simulate more years
steps_per_year = 10  # Define how many steps constitute a year

# Environment setup
field_size = 100
male_positions = np.random.rand(initial_males, 2) * field_size
female_positions = np.random.rand(initial_females, 2) * field_size
total_offspring = 0  # Track the total number of offspring

fig, ax = plt.subplots()

def offspring_sex_based_on_food(food_availability):
    # Higher food availability increases the chance of female offspring
    return 'F' if np.random.rand() < food_availability else 'M'

def animate(i):
    global male_positions, female_positions, total_offspring
    
    # Correctly update positions with dynamic size
    male_positions += (np.random.rand(male_positions.shape[0], 2) - 0.5) * 10
    female_positions += (np.random.rand(female_positions.shape[0], 2) - 0.5) * 10
    
    # Keep within bounds
    male_positions = np.clip(male_positions, 0, field_size)
    female_positions = np.clip(female_positions, 0, field_size)
    
    # Check for mating
    new_males = []
    new_females = []
    for male in male_positions:
        for female in female_positions:
            if np.linalg.norm(male - female) < 5 and np.random.rand() < mating_probability:
                # Determine offspring based on food availability
                for _ in range(10):  # Adjusted for a reasonable number of offspring per mating event
                    offspring_sex = offspring_sex_based_on_food(food_availability)
                    if offspring_sex == 'M':
                        new_males.append(np.random.rand(1, 2) * field_size)
                    else:
                        new_females.append(np.random.rand(1, 2) * field_size)
                total_offspring += 10  # Increment total offspring count
                        
    # Update populations
    if new_males:
        male_positions = np.append(male_positions, np.concatenate(new_males, axis=0), axis=0)
    if new_females:
        female_positions = np.append(female_positions, np.concatenate(new_females, axis=0), axis=0)
    
    ax.clear()
    ax.scatter(male_positions[:, 0], male_positions[:, 1], color='blue', label='Males')
    ax.scatter(female_positions[:, 0], female_positions[:, 1], color='red', label='Females')
    ax.set_xlim(0, field_size)
    ax.set_ylim(0, field_size)
    ax.legend()

    # Display counts, time, and calculate years
    current_year = i // steps_per_year
    ax.text(field_size * 1.1, field_size * 0.9, f'Year: {current_year}')
    ax.text(field_size * 1.1, field_size * 0.8, f'Males: {len(male_positions)}')
    ax.text(field_size * 1.1, field_size * 0.7, f'Females: {len(female_positions)}')
    ax.text(field_size * 1.1, field_size * 0.6, f'Offspring: {total_offspring}')
    sex_ratio = len(male_positions) / (len(female_positions) if len(female_positions) > 0 else 1)  # Avoid division by zero
    ax.text(field_size * 1.1, field_size * 0.5, f'Sex ratio: {sex_ratio:.2f}')
    ax.set_xlim(0, field_size * 1.5)  # Adjust xlim to make room for text
    ax.set_ylim(0, field_size)

    if total_offspring > 5000:
        ani.event_source.stop()

ani = animation.FuncAnimation(fig, animate, frames=simulation_steps, repeat=False)

plt.show()
