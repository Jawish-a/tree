class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child_name):
        if len(self.children) == 2:
            print("child is an orphan")
        else:
            self.children.append(child_name) 

    def search(self, person_name):
        
        for child in self.children:
            if person_name == child.name:
                return child
            else:
                for child in child.children:
                    if person_name == child.name:
                        return child
                    else:
                        for x in child.children:
                            if person_name == x.name:
                                return child    
                        
            

    def traverse(self):
        nodes = [self]
        while len(nodes) > 0:
            current_node = nodes.pop()
            print(current_node.name)
            nodes += current_node.children






family = TreeNode("family")


while True:
    person_name = input("enter child full name (done if finished): ")
    person_name = person_name.lower()
    if person_name == "done":
        break
    # 
    names = person_name.split(" ")
    if len(names) < 2:
        person_name = input("enter child FULL NAME (done if finished): ")
        person_name = person_name.lower()
    names = person_name.split(" ")

    first_name = names[0]
    parent_name = names[1]
    print(f"{first_name} , {parent_name}")
    child = TreeNode(first_name)
    parent = family.search(parent_name)
    if parent:
        print("-"*30)
        print("fond BABA!")
        parent.add_child(child)
        print(f"added a child to {parent_name}")
        print("-"*30)

    else:
        family.add_child(child)
        print("-"*30)
        print("added a child to family")
        print("-"*30)

    





family.traverse()

