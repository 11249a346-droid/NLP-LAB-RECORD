import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "student name": ["Taruni", "Sita", "Radha", "Sai"],
    "math": [101, 102, 103, 104],
    "science": [15, 27, 71, 85],
    "english": [91, 28, 77, 98],
    "age": [8, 11, 22, 9],
    "hour studies": [5, 7, 9, 6]
}

# Create DataFrame
df = pd.DataFrame(data)
print(df)

plt.figure(figure=(7,4))
plt.scatter(df["Hours_Studied"],df["math"], c=df["math "] ,           
            cmap="viridis",s=100,edgecolors ="black")
for i,name in enumerate (df["Student"]):
    plt.annotate(name, (df["Hours Studies"][i], df["math"][i]),
             textcoords ="offset points",xytext=(5,5),fontsize=8)
plt.colorbar(label="math score ")
plt.title("hours studied vs math score")
plt.xlabel("Hours Studied per day")
plt.ylabel("math score")
plt.tight_layout()
plt.savefig("scatter.png",dpi=150)
plt.show()                                          