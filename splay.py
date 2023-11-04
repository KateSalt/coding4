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
    # Search
    def search(self,key:int):
        splaykey = self.searchhelp(key)
        if(splaykey.parent == None):
            print("this is the root")
        elif(splaykey.parent.parent == None):
            print("this is a child of the root")
            if(splaykey == splaykey.parent.rightchild):
                print("this is a zig right")
            else:
                print("this is a zig left")
        elif(splaykey.parent == splaykey.parent.parent.rightchild):
            if(splaykey == splaykey.parent.rightchild):
                print("this is a zig zig for the right")
            else:
                print("this is a zig zag -right to left")
        elif(splaykey.parent == splaykey.parent.parent.leftchild):
            if(splaykey == splaykey.parent.leftchild):
                print("this is a zig zig for left")
            else:
                print("this is zig zag - left to right")

    # Insert Method 1
    def insert(self,key:int):
        self = self.search(key)
        if(self.root < key):
            curr = self.root
            curr.parent = Node(key=key,leftchild=curr,rightchild=curr.rightchild, parent= None)
            self.root = curr.parent
            curr.rightchild.parent = self.root
        else:
            curr = self.root
            curr.parent = Node(key=key,leftchild=curr.leftchild,rightchild=curr, parent= None)
            self.root = curr.parent
            curr.leftchild.parent = self.root

    # Delete Method 1
    def delete(self,key:int):
        print('This is a place-holder')