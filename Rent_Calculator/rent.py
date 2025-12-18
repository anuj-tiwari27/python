# Rent Calculator

# rent + food + electricity + charge per unit

rent = int(input("Enter your monthly rent: "))
food = int(input("Enter your monthly food expenses: "))
units = int(input("Enter the number of electricity units consumed: "))
charge_per_unit = int(input("Enter the charge per electricity unit: "))

electricity = units * charge_per_unit

tenants = int(input("Enter the number of tenants sharing the rent: "))

total_rent = rent+food+electricity;

rent_per_tenant = total_rent/tenants

print("Each tenant should pay: ", rent_per_tenant)