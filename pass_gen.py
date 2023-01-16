import random
import string

alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase
numbers = string.digits
signs = string.punctuation
raw_data = []

def main():
    length = get_value("What is the length of the pass phrase? ")
    upp_n = get_value("How many uppercase letters you need? ")
    num_n = get_value("How many numbers? ")
    sig_n = get_value("How many punctuation signs? ")

    for i in range(0, upp_n):
        raw_data.append(random.choice(alphabet_upper))

    for j in range(0, num_n):
        raw_data.append(random.choice(numbers))

    for k in range(0, sig_n):
        raw_data.append(random.choice(signs))

    for l in  range(0, (length - upp_n - num_n - sig_n)):
        raw_data.append(random.choice(alphabet_lower))

    random.shuffle(raw_data)

    password = "".join(raw_data)

    print(password)

def get_value(prompt):
    while True:
    try:
      value = int(input(prompt))
      break
    except ValueError:
      continue
    return value

if __name__ == "__main__":
    main()
