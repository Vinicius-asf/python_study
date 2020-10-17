def get_triangle_number(x):
    """
    Get the x-th triangle number
    """
    return int((x*(x+1))/2)

def get_index_offset(x,y):
    """
    Get the offset related to de triangle's index
    """
    return sum([x+(i-1) for i in range(1,y)])

def solution(x, y):
    return get_triangle_number(x) + get_index_offset(x,y)

if __name__ == "__main__":
    print(solution(3,2))
    print(solution(5,10))