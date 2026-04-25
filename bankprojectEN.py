__author__ = "lina04py"

# This program calculates the IBAN and checksum for the person
# who enters their bank code and account number.

# 1. The program takes the user's bank code and account number:

bank_code = input("Please enter your 8-digit bank code: ")
if not bank_code.isdigit():
    raise ValueError("Bank code must be numeric.")
bank_code = bank_code.zfill(8)

account = input("Please enter your 10-digit account number: ")
if not account.isdigit():
    raise ValueError("Account number must be numeric.")
account = account.zfill(10)

# 2. The country code "DE" is created:

country_code = "DE"

# 3. The IBAN is prepared with a placeholder for the checksum:
iban_with_placeholder = bank_code + account + "131400"

# Explanation:
# - Country code "DE" is converted: D = 13, E = 14.
# - Generally, the range starts at A = 10 and ends at Z = 35.
# - The placeholder "00" is already included in the conversion (DE → 1314).
# - Order: (Bank code + Account number + DE00)

# 4. Calculate the remainder modulo 97 to obtain the remainder for the checksum calculation:
remainder = int(iban_with_placeholder) % 97

# 5. Calculate the checksum:
calculated_checksum = 98 - remainder

# 6. If the checksum is a single digit, pad with zeros:
calculated_checksum = str(calculated_checksum).zfill(2)

# 7. Assemble the complete IBAN:
iban_full = country_code + calculated_checksum + bank_code + account

# 8. Output
print("\n-----------------------------------")
print("Calculated IBAN:")
print(iban_full)
print("-----------------------------------")
print("Explanation:")
print(f"Country code: {country_code}")
print(f"Checksum: {calculated_checksum}")
print(f"Bank code: {bank_code}")
print(f"Account number: {account}")
print("Calculation method:")
print("1. Country code (DE) is replaced by numbers (D=13, E=14).")
print("2. These numbers are placed after the bank code and account number.")
print("3. This results in: (bank code + account number + 131400).")
print("4. This number is calculated modulo 97.")
print("5. Checksum = 98 - (number mod 97).")
print("6. The result is the complete IBAN.")
