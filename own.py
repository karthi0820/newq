class binarytree:
    def _int_(self,value):
        self.left=None
        self.right=None
        self.value=value
    def insert(self,value):
        if self.value:
            if data<self.data:
                if self.left is None:
                    self.left=binarytree(value)
                else:
                    self.left.insert(value)
            elif data>self.value:
                if self.right is None:
                    self.data=binarytree(value)
                else:
                    self.data.insert(value)
            else:
                self.value=value
    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.data)
        if  self.right:
            self.right.oprinttree()
root=binarytree(100)
root.insert(50)
root.insert(23)
root.insert(45)
root.insert(7)
root.printtree()
