# PyChronos
PyChronos is a python client for ChronosDB, databse for business/economic/financial time series.

* For more info about the ChronosDB go to https://www.chronosdb.io
* Also check out the time series analytics platform power by ChronosDB, [tshub](https://www.tshub.io)
* For documentation go to https://www.chronosdb.io/docs/



# Quick start
Initiate client
```python
import pychronos
```

Initialize with username and password
```python
cdb = pychronos.init(username="john")
```

or with API key
```python
cdb = pychronos.init(api_key="johns_api_key")
```

or token
```python
cdb = chronosdb.init(token=“<token>”)
```

# Spaces

To list spaces
```python
cdb.list_spaces()
```


To create a new space
```python
x = cdb.create("my_new_space_name")
```

To retrieve a space
```python
myspace = cdb["myspace"]
```

Info
```python
myspace.info
```

To change name, title, description use assignment
```python
myspace.description = "awesome"
```
 
# Collection
To list collection is a space
```python
myspace.list_collections()
```

To retrieve a collection
```python
mycoll = myspace['mycollection']
```

Info
```python
mycoll.info
```

To change name, title, description use assignment
```python
mycoll.description = "awesome"
```

Metadata 
```python
myspace.list_collections()
```

To list collection is a space
```python
myspace.list_collections()
```

# Time series
##Create time series
```python
ts = mycoll.create("ts", freq="Q", dtype="float")
# or with more information
ts = mycoll.create("ts", freq="Q", dtype="float", title="My time series", description="This is my time series")
# JSONifiable attributes can be assigned on creation
ts = mycoll.create("ts", freq="Q", dtype="float", attributes={'a': 123, 'b': 'abc'})
```

## Info about time series
Display info about time series properties
```python
ts.info
```

Change values using assignment
```python
ts.title = "New title"
ts.description = "New description"
ts.attributes = {'x': 123, 'y': 'abc', 'z': [1,2,3]}
```

## Save data
Single series
```python
ts.save(pd.Series(np.array([10,20,30,40,50,60]), index=pd.period_range(start=pd.Period("2000Q1"), periods=6)))
```

Multiple series in a collection
```python
df = pd.DataFrame({
  "ts1": pd.Series(np.random.rand(6), index=pd.date_range(start=pd.Timestamp("2000-1-7"), periods=6, freq="D")),
  "ts2": pd.Series(np.random.rand(6), index=pd.date_range(start=pd.Timestamp("2000-1-9"), periods=6, freq="D"))
})

mycoll.save(df)
```

## Retrieve data
Single series
```python
ts.get()
```

Fetch multitle series from a collection
```python
mycoll.get(['ts1', 'ts2'])
```

## delete time series
```python
ts.delete()
```
