def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def ft_recursive(n):
        if n > days:
            print("Harvest time!")
        else:
            print("Day", n)
            ft_recursive(n + 1)

    ft_recursive(1)
