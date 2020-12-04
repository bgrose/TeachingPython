from statistics import median

class Math_Stuff_Class:
    def Median(_list):
        ret = median(_list)
        return ret
    def Square(_list):
        ret = []
        for i in _list:
             ret.append(i * i)
        return ret
    def Times_Table(_num):
        for x in range(1, 13):
            print(str(_num)+ " x " +str(x) + "  = " + str(x*_num))