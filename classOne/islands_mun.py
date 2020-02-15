input_world = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]


def count_islands_1(world_list):
    island = []
    island_line = []
    line_flag = False
    is_add = False
    for line_num in range(len(world_list)):
        world_line = world_list[line_num]
        for element_num in range(len(world_line)):
            list_num = element_num
            if is_add:
                list_num = list_num + 1
                is_add = False
            world_element = world_line[list_num]
            if not line_flag:
                island_element = []
            line_flag = True

            if world_element == 1:
                # if line_num == 0:
                island_element.append(world_element)

            elif world_element == 0:
                if line_num == 0:
                    break
                else:
                    next_element_num = element_num + 1
                    if next_element_num <= len(world_line) - 1:
                        if world_line[next_element_num] == 1:
                            next_island_line = island_line[line_num - 1]
                            if next_island_line[element_num + 1] == 1:
                                island_element.append("*")
                                island_element.append(1)
                                is_add = True
        line_flag = False

        island_line.append(island_element)
    island.append(island_line)

    print(island)


def count_islands_2(world_list):
    print(world_list)


# count_islands_1(input_world)
