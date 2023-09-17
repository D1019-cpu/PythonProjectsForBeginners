import logic


if __name__ == '__main__':
    matrix = logic.start_game()

    while True:
        print(matrix)
        x = input("Press the command: ")

        if (x == 'W' or x == 'w'):
            matrix, flag = logic.move_up(matrix)

            status = logic.get_current_state(matrix)
            print(status)

            if status == 'Game Not Over!':
                logic.add_new_2(matrix)
            else:
                break

        elif (x == 'S' or x == 's'):
            matrix, flag = logic.move_down(matrix)

            status = logic.get_current_state(matrix)
            print(status)

            if status == 'Game Not Over!':
                logic.add_new_2(matrix)
            else:
                break
        
        elif (x == 'A' or x == 'a'):
            matrix, flag = logic.move_left(matrix)
            status = logic.get_current_state(matrix)
            print(status)

            if status == 'Game Not Over!':
                logic.add_new_2(matrix)
            else:
                break

        elif (x == 'D' or x == 'd'):
            matrix, flag = logic.move_right(matrix)
            status = logic.get_current_state(matrix)
            print(status)

            if status == 'Game Not Over!':
                logic.add_new_2(matrix)
            else:
                break
        
        else:
            print("Invalid Key Pressed!!!")
        
        