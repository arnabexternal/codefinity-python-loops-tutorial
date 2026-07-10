# List of countries you are considering for travel
countries = ['Wales', 'Denmark', 'Belgium', 'Japan', 'South Korea', 'South Africa', 'Indonesia', 'Singapore', 'Australia', 'India', 'Saudi Arabia', 'Mexico', 'Turkey', 'Greece', 'Netherlands', 'Finland', 'Monako', 'United Arab Emirates', 'Egypt', 'Morocco', 'Brazil', 'Argentina', 'Ireland', 'Portugal', 'Chile', 'Spain', 'Czech Republic', 'Sweden', 'Switzerland', 'Thailand', 'Luxemburg', 'New Zealand', 'France', 'Italy', 'Germany', 'China', 'Canada', 'Hungary', 'Scotland', 'Norway', 'Austria', 'Ukraine', 'Poland']

# List of countries that require a visa
visa_required = ['China', 'India', 'Saudi Arabia', 'Brazil', 'United Arab Emirates', 'Egypt']

# List of visa-free travel destinations
travel_list = []
travel_list_count = 0

for coun in countries:
    if coun in visa_required:
        pass
    else:
        travel_list.append(coun)
        travel_list_count += 1
        if travel_list_count == 10:
            break

# Testing
print('Visa-free travel destinations:', travel_list)