activities=[(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11),(2,14),(12,16)]
activities.sort(key=lambda x:x[1])#按照活动结束时间进行排序

def activity_selection(a):
    res=[a[0]]
    for i in range(1,len(a)):
        if a[i][0]>=res[-1][1]:#当活动开始时间大于等于最后一个入选活动的结束时间，则不冲突，可以入选
            res.append(a[i])
    return  res

print(activity_selection(activities))