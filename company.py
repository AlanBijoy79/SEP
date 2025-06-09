
company_name = input("Enter the full company name: ")
abbreviation = ''.join(word[0].upper() for word in company_name.split())
print("Abbreviation:", abbreviation)
