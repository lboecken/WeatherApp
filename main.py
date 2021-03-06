from individual import Individual
import pandas as pd
column_names = ["Name", "City, State, Zip", "Latitude", "Longitude"]
df = pd.DataFrame(columns=column_names)
John = Individual(name="John")
print(John.coordinates)
df = df.iloc[0:0]