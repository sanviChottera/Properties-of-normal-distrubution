import random
import statistics
import plotly.figure_factory as ff 
import plotly.graph_objects as go

#empty list
dice_result =[]
for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1 + dice2)


mean = statistics.mean(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)
std = statistics.stdev(dice_result)

# {} is called placeholder
print( " Mean  : {} ".format( mean ))
print( " Median : {}".format( median ))
print( " Mode  : {}".format( mode ))


first_std_start, first_std_end = mean-std, mean + std
sec_std_start, sec_std_end = mean-(2*std), mean + (2*std)
third_std_start, third_std_end = mean-(3*std), mean + (3*std)

fig = ff.create_distplot( [dice_result],["result"],show_hist = False )
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines+markers",name = "mean of data"  ))

fig.add_trace(go.Scatter(x=[first_std_start, first_std_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 start"))
fig.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 end"))

fig.add_trace(go.Scatter(x=[sec_std_start, sec_std_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 start"))
fig.add_trace(go.Scatter(x=[sec_std_end, sec_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 end"))

fig.add_trace(go.Scatter(x=[third_std_start, third_std_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 start"))
fig.add_trace(go.Scatter(x=[third_std_end, third_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 end"))


fig.show()


data_within_1_std = [i for result in dice_result if result > first_std_start and result < first_std_end]
data_within_2_std = [i for result in dice_result if result > sec_std_start and result < sec_std_end]
data_within_3_std = [i for result in dice_result if result > third_std_start and result < third_std_end]

# len() method finds the length of the list,number of elements in the list
print("{} % of data lies within 1st standard deviation".format( len(data_within_1_std) * 100.0/len(dice_result) ) )
print("{} % of data lies within 2nd standard deviation".format( len(data_within_2_std) * 100.0/len(dice_result) ) )
print("{} % of data lies within 3rd standard deviation".format( len(data_within_3_std) * 100.0/len(dice_result) ) )