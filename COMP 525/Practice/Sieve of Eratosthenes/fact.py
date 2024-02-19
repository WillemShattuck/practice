def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

def main():
    r = fact(4)
    print(r)

if __name__ == "__main__":
    main()

def print_list_recursive(lst, index=0):
    if index < len(lst):
        print(lst[index])
        print_list_recursive(lst, index + 1)

# Example usage:
my_list = [3, 4, 5, 6]
print_list_recursive(my_list)
