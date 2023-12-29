##############################
Dictionaries
##########################################


# Create the initial dictionary
ecommerce_company = {"Company Name": "Amazon", "Industry": "E-commerce", "Total Employees": "100000+"}

# Print the whole sentence
print('Company details are:', ecommerce_company)

# Use dict.keys() to show keys
print('Keys:', ecommerce_company.keys())

# Use dict.values() to show values
print('Values:', ecommerce_company.values())

# Use dict.items() to show keys and values
print('Items:', ecommerce_company.items())

print("*********************************************************************************************************")

# Now update the company name and number of employee details
ecommerce_company["Company Name"] = "Flipkart"
ecommerce_company["Total Employees"] = "90,000+"

print("Update company name to Flipkart")
print('Company details after update:', ecommerce_company)

print("*********************************************************************************************************")
