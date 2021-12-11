class TreeNode:
    def __init__(self,name, spot) -> None:
        self.name=name
        self.spot=spot
        self.children=[]
        self.parent=None
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
    def print_name(self):
        prefix=' '*self.get_level()+"|--" if self.parent else ' '*self.get_level()
        print (prefix+self.name)
        if self.children:
            for child in self.children:
                child.print_name()

    def print(self):
        prefix=' '*self.get_level()+"|--" if self.parent else ' '*self.get_level()
        print (f"{prefix} {self.name} ({self.spot})")
        if self.children:
            for child in self.children:
                child.print()

    def print_spot(self):
        prefix=' '*self.get_level()+"|--" if self.parent else ' '*self.get_level()
        print (prefix+self.spot)
        if self.children:
            for child in self.children:
                child.print_spot()
def build_tree():
    family=TreeNode("GrandFather",'First generate')
    Next_gen1=TreeNode("Father","Second generate")
    Next_gen2_1=TreeNode("Me","Third generate")
    Next_gen2_2=TreeNode("My sister","Third generate")
    Next_gen3_1_1=TreeNode("My kid","Fourth generate")
    Next_gen3_2_1=TreeNode("Sister's kid 1","Fourth generate")
    Next_gen3_2_2=TreeNode("Sister's kid 2","Fourth generate")

    family.add_child(Next_gen1)
    Next_gen1.add_child(Next_gen2_1)
    Next_gen1.add_child(Next_gen2_2)
    Next_gen2_1.add_child(Next_gen3_1_1)
    Next_gen2_2.add_child(Next_gen3_2_1)
    Next_gen2_2.add_child(Next_gen3_2_2)
    return family
if __name__ == '__main__':
    build_tree().print()
    