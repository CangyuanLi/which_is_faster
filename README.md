Have you ever wondered what the fastest way to do something in Python is? Is it faster to use
a list comprehension or a for loop? Whats the difference between len(df) and len(df.index)?
This repository aims to answer all of these questions. Contributions are welcome.

# Summary of Results

* If you want to perform some calculation over a list and store the results, use ```map()```
* If you want to find the number of rows in a Pandas DataFrame, use ```len(df.index)```