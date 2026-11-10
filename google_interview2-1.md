Imagine we design a simple file system metadata.
There are 2 types of entities: 'file' and 'directory'.
Each entity is given an integer 'entity id' and has a 'name'.
File entities also have a 'size' field of how much space they consume in bytes.
Directory entities have a list of 'children', representing entity ids inside them.

Overall, we have the following structures:
```
EntityId: int
Entity = {
  type: ‘file’ | ‘directory’
  name: string
  oneof {
    size: int
    children: [EntityId]
  }
}

Filesystem: map<EntityId, Entity>
```
Given this the file system:

root (id=1)
    dir (id=7)
        file8 (id=8): 50b
    dir (id=2)
        file1 (id=4): 100b
        file2 (id=5): 200b
    file3 (id=3): 300b

will be represented as the following:

Filesystem = { 1: { "type": 'directory', "name": "root", "children": [3, 2] },
               2: { "type": 'directory', "name": "dir", "children": [4, 5] },
               4: { "type": 'file', "name": "file1", "size": 100 },
               5: { "type": 'file', "name": "file2", "size": 200 },
               3: { "type": 'file', "name": "file3", "size": 300 },
               6: { "type": "file": ..., "size": 150}}

summation_table = dict() # key: id, value: summation
def get_size(filesystem, id) -> int:
  # filesystem get children from ids
  # children: files, subdirectories
  
  if id in summation_table:
    return summation_table.get(id)
  
  def recursive(id: int, summation: int)->int:
    
    summation = 0

    # recursive: subdirectories call get_size
    node = filesystem.get(id)
    if node.get("type") == "file":
      summation_table[id] = node.get("size")
      return node.get("size")

    else: # directory
      children = node.get("children")
      for child in children:
        size_child = 0
        if child in summation_table:
          size_child = summation_table.get(child)
        else:
          size_child=recursive(child, summation)
        summation_table[child] = size_child
        summation+=size_child
      return summation
  
  recursive(id, 0)
  summation_table[id] = summation
  return summation

get_size(Filesystem, 1)
summation = 0, summation_table = {}
recursive(1)
  recursive(2)
    child_size = recursive(4) = 100
summation = 100, summation_table = {4: 100}
    child_size = recursive(5) = 200
summation = 300, summation_table = {4: 100, 5: 200}
   child_size = 300, summation_table = {4: 100, 5: 200, 2: 300}
summation = 600

get_size(Filesystem, 2)
