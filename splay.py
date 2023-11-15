from __future__ import annotations
import json
from typing import List

verbose = False

# DO NOT MODIFY!
class Node():
    def  __init__(self,
                  key       : int,
                  leftchild  = None,
                  rightchild = None,
                  parent     = None,):
        self.key        = key
        self.leftchild  = leftchild
        self.rightchild = rightchild
        self.parent     = parent

# DO NOT MODIFY!
class SplayTree():
    def  __init__(self,
                  root : Node = None):
        self.root = root

    # For the tree rooted at root:
    # Return the json.dumps of the object with indent=2.
    # DO NOT MODIFY!
    def dump(self) -> str:
        def _to_dict(node) -> dict:
            pk = None
            if node.parent is not None:
                pk = node.parent.key
            return {
                "key": node.key,
                "left": (_to_dict(node.leftchild) if node.leftchild is not None else None),
                "right": (_to_dict(node.rightchild) if node.rightchild is not None else None),
                "parentkey": pk
            }
        if self.root == None:
            dict_repr = {}
        else:
            dict_repr = _to_dict(self.root)
        return json.dumps(dict_repr,indent = 2)


    def searchhelp(self,key:int):
        curr = self.root
        while((curr.key != key)):
            if(curr.key < key):
                if(curr.rightchild != None):
                    curr = curr.rightchild
                else:
                    return curr
            else:
                if(curr.leftchild != None):
                    curr = curr.leftchild
                else:
                    return curr
        return curr
    # Search add until root
    def search(self,key:int):
        if(self.root == None):
            return self
        splaykey = self.searchhelp(key)
        if(splaykey.parent == None):
            return self
        while(splaykey.parent != None):
            if(splaykey.parent.parent == None):
                if(splaykey == splaykey.parent.rightchild):
                    self.root = splaykey
                    splaykey.parent.rightchild = splaykey.leftchild
                    if(splaykey.leftchild != None):
                        splaykey.leftchild.parent = splaykey.parent
                    splaykey.leftchild = splaykey.parent
                    splaykey.parent.parent = splaykey 
                    splaykey.parent = None
                    return self
                else:
                    self.root = splaykey
                    parent = splaykey.parent
                    parent.leftchild = splaykey.rightchild
                    if(splaykey.rightchild != None):
                        splaykey.rightchild.parent = splaykey.parent
                    splaykey.rightchild = parent
                    parent.parent = splaykey 
                    splaykey.parent = None

                    return self
            elif(splaykey.parent == splaykey.parent.parent.rightchild):
                if(splaykey == splaykey.parent.rightchild):
                    grand = splaykey.parent.parent
                    parent = splaykey.parent
                    if(grand == self.root):
                        self.root = splaykey
                    if(grand.rightchild != None):
                        grand.rightchild.parent = grand
                    grand.rightchild = parent.leftchild
                    if(grand.rightchild != None):
                        grand.rightchild.parent = grand
                    parent.leftchild = grand
                    splaykey.parent = grand.parent 
                    if(grand.parent != None):
                        if(grand.parent.rightchild == grand):
                            grand.parent.rightchild = splaykey
                        else:
                            grand.parent.leftchild = splaykey
                    grand.parent = parent 
                    parent.parent = splaykey
                    if(splaykey.leftchild != None):
                        splaykey.leftchild.parent = parent

                    parent.rightchild = splaykey.leftchild
                    splaykey.leftchild = parent
                    
                else:
                    grand = splaykey.parent.parent
                    parent = splaykey.parent
                    if(grand == self.root):
                        self.root = splaykey
                    else:
                        if(grand.parent.rightchild == grand):
                            grand.parent.rightchild = splaykey 
                        else: 
                            grand.parent.leftchild = splaykey
                    parent.parent = splaykey 
                    parent.leftchild = splaykey.rightchild
                    grand.rightchild = splaykey.leftchild
                    if(grand.rightchild != None):
                        grand.rightchild.parent = grand
                    if(parent.leftchild != None):
                        parent.leftchild.parent = parent
                    splaykey.leftchild = grand
                    splaykey.rightchild = parent
                    splaykey.parent = grand.parent 
                    grand.parent = splaykey

            elif(splaykey.parent == splaykey.parent.parent.leftchild):
                if(splaykey == splaykey.parent.leftchild):
                    grand = splaykey.parent.parent
                    parent = splaykey.parent
                    if(grand == self.root):
                        self.root = splaykey
                    grand.leftchild = parent.rightchild
                    if(grand.leftchild != None):
                        grand.leftchild.parent = grand
                    parent.rightchild = grand
                    splaykey.parent = grand.parent 
                    if(grand.parent != None):
                        if(grand.parent.leftchild == grand):
                            grand.parent.leftchild = splaykey
                        else:
                            grand.parent.rightchild = splaykey
                    grand.parent = parent 
                    parent.parent = splaykey
                    if(splaykey.rightchild != None):
                        splaykey.rightchild.parent = parent
                    parent.leftchild = splaykey.rightchild
                    splaykey.rightchild = parent
                    # if(key == 777):
                    #     # print("woohoo!")
                    #     # print("GRAND " , grand.key, grand.leftchild, grand.rightchild, grand.parent.key)
                    #     # print("PARENT " , parent.key, parent.leftchild, parent.rightchild.key, parent.parent.key)
                    #     # print("SPLAY " , splaykey.key, splaykey.leftchild,splaykey.rightchild.key, splaykey.parent.rightchild.key)
                    #     # print(grand.key, grand.leftchild.parent.key, splaykey.key, " penis")
                    #     # print(self.dump())
                    #     return
                else:
                    grand = splaykey.parent.parent
                    parent = splaykey.parent
                    if(grand == self.root):
                        self.root = splaykey
                    else:
                        if(grand.parent.rightchild == grand):
                            grand.parent.rightchild = splaykey 
                        else: 
                            grand.parent.leftchild = splaykey
                    parent.parent = splaykey 
                    parent.rightchild = splaykey.leftchild
                    grand.leftchild = splaykey.rightchild
                    if(grand.leftchild != None):
                        grand.leftchild.parent = grand
                    if(parent.rightchild != None):
                        parent.rightchild.parent = parent
                    splaykey.rightchild = grand
                    splaykey.leftchild = parent
                    splaykey.parent = grand.parent 
                    grand.parent = splaykey
        return self

    # Insert Method 1
    def insert(self,key:int):
        if(self.root == None):
            self.root = Node(key=key,rightchild=None,leftchild=None,parent=None)
            return self
        self = self.search(key)
        if(self.root.key < key):
            curr = self.root
            new = Node(key=key,leftchild=curr,rightchild=curr.rightchild, parent= None)
            self.root = new
            curr.parent = new
            if(curr.rightchild != None):
                curr.rightchild.parent = new
            curr.rightchild = None
            return self
        else:
            curr = self.root
            new = Node(key=key,leftchild=curr.leftchild,rightchild=curr, parent= None)
            self.root = new
            curr.parent = new
            if(curr.leftchild != None):
                curr.leftchild.parent = new
            curr.leftchild = None
            return self

    # Delete Method 1
    def delete(self,key:int):
        splay = self.search(key)
        splaykey  = splay.root
        if((splaykey.leftchild == None) & (splaykey.rightchild == None)):
            return None
        elif(splaykey.rightchild == None):
            self.root = splaykey.leftchild
            self.root.parent = None
            return self
        elif(splaykey.leftchild == None):
            self.root = splaykey.rightchild
            self.root.parent = None
            return self
        else:
            repl = SplayTree(root =Node(splaykey.rightchild.key,leftchild=splaykey.rightchild.leftchild,rightchild=splaykey.rightchild.rightchild,parent=None))
            repl = repl.search(key)
            replacement = repl.root
            replacement.leftchild = splaykey.leftchild
            if(splaykey.rightchild != None):
                splaykey.rightchild.parent = replacement
            if(splaykey.leftchild != None):
                splaykey.leftchild.parent = replacement
            self.root = replacement 
            return self.root
        

# tree = SplayTree(root=None)

# tree.insert(661)
# tree.insert(916)
# tree.insert(886)
# tree.insert(897)
# tree.insert(516)
# tree.insert(954)
# tree.insert(654)
# tree.insert(273)
# tree.insert(206)
# tree.insert(777)
# tree.insert(16)
# tree.insert(18)
# print(tree.dump())