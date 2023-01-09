from scipy import stats
data =[[9,1,2,3,6],[2,34,45,22,67],[54,70,51,27,1]]
print("")
print("Moment Generating Functions - MGF for Multi-dimensional data")
print("0th Moment =",stats.moment(data,moment =0))
print("1st Moment =",stats.moment(data,moment =1))
print("2nd Moment =",stats.moment(data,moment =2,axis=1))
print("3rd Moment =",stats.moment(data,moment =3,axis=1))
print("4th Moment =",stats.moment(data,moment =4,axis=1))
print("5th Moment =",stats.moment(data,moment =5,axis=1))