def mat_to_list(adj_mat):
    """ Convert adjacency matrix to an adjacency list representation

    Parameters:
    -----------
    adj_mat : (a square 0-1 matrix)
        Adjacency matrix (n x n) of the graph (of n nodes)


    Returns:
    --------
     adj_list: list[list[int]]
        The adjacency list of the graph


    adj_mat =   [[0, 1, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0]]

    adj_list = [[1, 3], [2], [0], [4], [3], []]

    """
    # TODO
    adj_list = [] 
    for i in range(len(adj_mat)):
        index_list = []
        for j in range(len(adj_mat[i])):
            if adj_mat[i][j] == 1:
                index_list.append(j)
        adj_list.append(index_list)

    return adj_list