## College Search CSV

The purpose of this lab set is to practice working with a relatively large comma separated (CSV) file in Python. The file, `university-data.csv`, is about 65mb and contains just over 7,100 rows with almost 2,000 columns per record. 

You're going to implement 3 separate functions, each in their own file.

### state_count

`state_count` needs to parse the `university-data.csv` file and return the number of times that `state` matches the `STABBR` field. 

### highest_in_state

`highest_in_state` also has a `state` parameter, but this time it's going to return the highest in state tuition for that state along with the name of the highest cost institution as a tuple. 

Python supports multiple returns. Look at the following code snippet.

```python
def some_method():
    x = 3
    y = 4
    return x, y

a, b = some_method()
```

`some_method` returns a tuple containing `(x, y)`. After the call the values from that tuple are stored in `a` and `b`. You will want to do something similar so that `highest_in_state` returns the highest amount and the name of the highest cost school in a single line.

### closest_university

For `closest_university` you're going to determine the closest university to a give latitude and longitude pair. 

To help you out there's a `distance` method given to you in the `closest_university.py` file. This method uses the [Haversine forumla](https://en.wikipedia.org/wiki/Haversine_formula) to determine the distance between to points accounting for the radius of the Earth. 

In the `closest_university` function, given `location` as a tuple containing latitude and longitude, you're going to find the closest university to that point. Your return value will be a tuple containing the calculated distance followed by the institution name. 



## Some Hints

#### Casting

Everything you pull out of the CSV file will be a string. You can convert between strings and numeric values using either the `int(x)` method or the `float(x)` method depending on whether you need decimals.

#### Non-numeric values

Some of the numeric fields may have non-numeric values. For example. `TUITIONFEE_IN` has a `-` for a value when the value isn't known. You can treat these as outliers and not consider non-numeric data. But you do need to trap for it. `int('-')` will cause an error. 



## Testing

You have a unit test file `test_csv.py` with a test method for each of the 3 methods you're implementing. These will also run when you push your code to GitHub. 