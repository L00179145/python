########################
Tuple Unpacking

##################################

def highest_rated(product_ratings):
  #####################################
    Iterate through a list and find the highest-rated item
###############################
# Set up the variables
    max_rating = 0
    highest_rated_product = ""
# Iterate, unpacking the tuple
    for product, rating in product_ratings:
# If this is the highest rating, record that in our variables
        if rating > max_rating:
            max_rating = rating
            highest_rated_product = product
# If it is not the highest rating, do nothing
        else:
            pass
# Return the highest-rated item and its rating
    return highest_rated_product, max_rating

# Provide the data
product_ratings = [("Laptop", 4.8), ("Camera", 4.5), ("Smartphone", 4.9), ("Tablet", 4.7)]
# Call the function and unpack its return values
product, rating = highest_rated(product_ratings)
print(f"The highest-rated product is {product} with a rating of {rating}")
