group_des = grouped_des.get_group("RED WOOLLY HOTTIE WHITE HEART.")
days = (group_des["InvoiceDate"].max() - group_des["InvoiceDate"].min()).days
group_day = group_des.groupby([group_des["InvoiceDate"].dt.date])
# print(group["InvoiceDate"].dt.date.max())
# print(group["InvoiceDate"].dt.date.min())
bought_day = []

indexes = group_day.groups.keys()
prev_date = group_des["InvoiceDate"].dt.date.min()
for name, group in group_day:
    print(name)
    days_passed = (name - prev_date).days
    # print(days_passed)
    while days_passed > 1:
        bought_day.append(0)
        days_passed -= 1 
    bought_day.append(group.shape[0])
    prev_date = name
# print(len(bought_day))
plt.plot(range(days), bought_day)
plt.show()