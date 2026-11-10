rpcid(unique), timestamp, start/end
1. start must be before the end
2. end may not be called
3. target: return the first timeout rpcid

input:
1, 0, start
2, 1, start
...

timeout: 3

output: 
2
