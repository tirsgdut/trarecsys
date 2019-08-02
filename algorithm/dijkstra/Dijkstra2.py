# encoding:utf-8import randomimport timeimport numpy as np# 随机生成顶点矩阵：# 输入：矩阵的的行数# 输出：矩阵（随机生成）# 矩阵的内容为权值def random_matrix_genetor(vex_num=10):    data_matrix = []    for i in range(vex_num):        #一行的数据        one_list = []        for j in range(vex_num):            one_list.append(random.randint(1, 3))        data_matrix.append(one_list)    print(data_matrix)    return data_matrix# 计算最短路径# 输入为：起始点、终点、矩阵def dijkstra(data_matrix, start_node):    # 记录点的个数    vex_num = len(data_matrix)    # 标志列表    flag_list = ['False'] * vex_num    # 先前的记录列表    prev = [0] * vex_num    # 距离记录列表    dist = ['0'] * vex_num    # 初始化    for i in range(vex_num):        flag_list[i] = False        prev[i] = 0        # 记录起始点对应的连接点的权值        dist[i] = data_matrix[start_node][i]    flag_list[start_node] = False    # 自己与自己的距离变成0:    dist[start_node] = 0    # 记录点    k = 0    # 遍历（vex_num-1）次    for i in range(1, vex_num):        # 找出最小权值        min_value = np.inf        # 遍历每一列（第一次）        # 找出最小的权值        for j in range(vex_num):            if flag_list[j] == False and dist[j] != np.inf and min_value >= dist[j] :                min_value = dist[j]                k = j        # 标记已被选取的顶点,标记成true        flag_list[k] = True        for j in range(vex_num):            # 距离最小的点对应的行中有无穷大（不可直达）            if data_matrix[k][j] == np.inf:                temp = np.inf            else:                temp = min_value + data_matrix[k][j]            if flag_list[j] == False and temp != np.inf and temp < dist[j]:                dist[j] = temp                #记录上距离最小的点                print("hh",k)                prev[j] = k    for i in range(vex_num):        print('顶点' + str(start_node) + '到顶点' + str(i) + '最短距离是--->' + str(dist[i]))def main_test_func(vex_num=10):    start_time = time.time()    data_matrix = random_matrix_genetor(vex_num)    dijkstra(data_matrix,4)    end_time = time.time()    return end_time - start_timeif __name__ == '__main__':    time = main_test_func(5)    print("预测所需要的时间为：%s s" % time)