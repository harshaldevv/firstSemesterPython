try:
    f = open('')

except ZeroDivisionError:

    print("sorry,age cannot be zero ")

except NameError:
    print("name error hai bro")

except FileNotFoundError as e:
    print(e)
