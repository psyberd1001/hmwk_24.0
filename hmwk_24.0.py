def apply_all_func(int_list, *functions):
    result = {}
    for i in functions:
        name1 = i.__name__
        result_of_pr = i(int_list)
        result.update({name1: result_of_pr})
    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))


