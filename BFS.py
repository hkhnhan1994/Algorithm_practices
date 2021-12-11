"""
format of graph map is dictionary:
graph={
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
"""
class BreadthSearch:
    def __init__(self,Series,start):
        self.visited=[]
        self.queue=[]
        self.Series=Series
        self.queue.append(start)
        self.visited.append(start)
    def BFS(self):
        # get node from queue
        # while self.queue:
        try:
            if self.queue is not None:
                get_q=self.queue.pop(0)
            print(get_q,end=" ")
            for i in self.Series[get_q]:
                if i not in self.visited:
                    self.queue.append(i)
                    self.visited.append(i)
        except:
            return
        return self.BFS()    
graph={
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8','9'],
  '2' : ['10'],
  '4' : ['8'],
  '8' : [],
  '9' :[],
  '10':[]
}
newBFS=BreadthSearch(graph,'5')
newBFS.BFS()

