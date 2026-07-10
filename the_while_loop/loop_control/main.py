# List of country names
countries = ['Wales', 'Denmark', 'Belgium', 'Japan', 'South Korea', 'South Africa', 'Indonesia', 'Singapore', 'Australia', 'India', 'Saudi Arabia', 'Mexico', 'Turkey', 'Greece', 'Netherlands', 'Finland', 'Monako', 'United Arab Emirates', 'Egypt', 'Morocco', 'Brazil', 'Argentina', 'Ireland', 'Portugal', 'Chile', 'Spain', 'Czech Republic', 'Sweden', 'Switzerland', 'Thailand', 'Luxemburg', 'New Zealand', 'France', 'Italy', 'Germany', 'China', 'Canada', 'Hungary', 'Scotland', 'Norway', 'Austria', 'Ukraine', 'Poland']

# List to hold selected countries
selected = []
country_index = 0
s_country_count = 0

while country_index < len(countries):
    if countries[country_index].lower().startswith("s"):
        if s_country_count > 2:
            break
        else:
            selected.append(countries[country_index])
            s_country_count += 1
    country_index += 1

# Testing
print('First three countries starting with "S":', selected)