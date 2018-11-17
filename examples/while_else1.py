# Note: driver assumes a function with the same name as the file basename
# test
def testing(a):
    while a:
        a += 2
    else:
        a = 5
    return a

def expect():
    return """
loop BasicBlock(#0 range: (0, 0), flags=[0, 2], follow_offset=2, edge_count=2, jumps=[22])
  while else BasicBlock(#1 range: (2, 4), follow_offset=6, edge_count=2, jumps=[16])
    continue BasicBlock(#2 range: (6, 14), flags=[8], follow_offset=16, edge_count=2, jumps=[2])
    sequence pop block while else BasicBlock(#3 range: (16, 20), flags=[6], follow_offset=22, edge_count=1)
    end sequence pop block while else
  end while else
end loop
"""
