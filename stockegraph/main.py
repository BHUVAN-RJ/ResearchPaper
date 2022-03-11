import readfiles as rf
from matplotlib import pyplot as plt

countries = ["Russia", "India", "China", "UK", "USA"]
values = {}
sectors = ["Energy", "Material", "Industrial", "Healthcare", "Financial", "Consumer-Discretionary", "Consumer-Staples",
           "IT", "Communication Service", "Real Estate"]

for item in countries:
    i = 1
    while i <= len(rf.name(item.lower())):
        result = rf.Data(rf.name(item.lower())[i-1], item, i)
        answer = result.components()
        values[answer[0]] = [answer[1], answer[2]]
        i += 1


new_dict = {}
new_dict["value1"] = [values["Russia_1"], values["India_1"], values["UK_1"], values["USA_1"], values["China_1"]]
new_dict["value2"] = [values["Russia_2"], values["India_2"], values["UK_2"], values["USA_2"], values["China_2"]]
new_dict["value3"] = [values["Russia_3"], values["India_3"], values["UK_3"], values["USA_3"], values["China_3"]]
new_dict["value4"] = [values["Russia_4"], values["India_4"], values["UK_4"], values["USA_4"], values["China_4"]]
new_dict["value5"] = [values["Russia_5"], values["India_5"], values["UK_5"], values["USA_5"], values["China_5"]]
new_dict["value6"] = [values["Russia_6"], values["India_6"], values["UK_6"], values["USA_6"], values["China_6"]]
new_dict["value7"] = [values["Russia_7"], values["India_7"], values["UK_7"], values["USA_7"], values["China_7"]]
new_dict["value8"] = [values["Russia_8"], values["India_8"], values["UK_8"], values["USA_8"], values["China_8"]]
new_dict["value9"] = [values["Russia_9"], values["India_9"], values["UK_9"], values["USA_9"], values["China_9"]]
new_dict["value10"] = [values["Russia_10"], values["India_10"], values["UK_10"], values["USA_10"], values["China_10"]]


num = 0
for key in new_dict.keys():
    plt.plot(new_dict[key][0][0], new_dict[key][0][1], label="Russia")
    plt.plot(new_dict[key][1][0], new_dict[key][1][1], label="India")
    plt.plot(new_dict[key][2][0], new_dict[key][2][1], label="UK")
    plt.plot(new_dict[key][3][0], new_dict[key][3][1], label="USA")
    plt.plot(new_dict[key][4][0], new_dict[key][4][1], label="China")
    plt.title(sectors[num])
    plt.xlabel("Time")
    plt.ylabel("Gains")
    plt.gcf().canvas.manager.set_window_title('Test')
    plt.legend()
    num += 1
    plt.show()














