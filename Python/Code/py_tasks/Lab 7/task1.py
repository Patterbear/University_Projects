data = ((45, 'foot'), (21, 'basket'), (10, 'hand'), (24, 'foot'), (21, 'hand'))

def unique_data_items(data):
    unique_nums = ()
    unique_words = ()

    for i in range(len(data)):
        unique_nums = unique_nums + (data[i][0],)
        unique_words = unique_words + (data[i][1],)
        
    num_list = list(unique_nums)
    word_list = list(unique_words)

    for i in range(len(unique_nums)):
        if num_list.count(data[i][0]) > 1:
            for j in range(num_list.count(data[i][0])):
                num_list.remove(data[i][0])
        if word_list.count(data[i][1]) > 1:
            for j in range(word_list.count(data[i][1])):
                word_list.remove(data[i][1])
                
    unique_nums = tuple(num_list)
    unique_words = tuple(word_list)

    return(unique_nums, unique_words)

print(unique_data_items(data))



