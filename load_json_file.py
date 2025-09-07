

df = pd.read_json(r'C:\\Users\Ajay\Downloads\sample_employees.json')
print(df)

# to_string to get all the rows
print(df.to_string())

# in order to restrict upto 20
df.options.display.max_rows = 20)
print(df) 
