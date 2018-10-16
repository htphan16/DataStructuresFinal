from linked_binary_tree import LinkedBinaryTree

class ExtendedLinkedBinaryTree(LinkedBinaryTree):
    
    def postorder_next(self, p):
        """Return the next position from p in postorder tranversal"""
        if self.parent(p) == None:       #base case
            return None
        elif self.right(self.parent(p)) == p:   #if p is the right child
            return self.parent(p)
        else:
            if self.right(self.parent(p)) == None: #if the parent of p does not have a right child
                return self.parent(p) 
            else:                           #if the parent of p has a right child
                a = self.right(self.parent(p)) 
                if self.left(a) != None:    #if there's a left child to a
                    b = self.left(a)
                    while self.num_children(b) != 0:   #loop to return the furthest left child of that subtree
                        if self.left(b) != None:
                            b = self.left(b)
                        else:
                            b = self.right(b)
                    return b
                elif self.right(a) != None:
                    b = self.right(a)
                    while self.num_children(b) != 0: #loop to return the furthest right child of that subtree
                        if self.right(b) != None:
                            b = self.right(b)
                        else:
                            b = self.left(b)
                    return b
                else:
                    return a
                
    def inorder_next(self, p):
        """Return the next position from p in inorder tranversal"""
        if p == self.root():     #base case
            d = self.right(p)
            while self.left(d) != None:   #loop to return the furthest left child of that tree
                d = self.left(d)
            return d
        
        elif self.left(self.parent(p)) == p: #if p is a left child
            if self.num_children(p) == 0: #if p doesn't have any children
                return self.parent(p)   
            else:
            
                if self.right(p) != None:
                    a = self.left(self.right(p))   
                    if a != None:     #if a exist
                        while self.left(a) != None:  #Loop to return the furthest left of the subtree
                            a = self.left(a)
                        return a
                    return self.right(p) #return right child of p
                else:
                    return self.parent(p) #return parent of p
        
        
        else:  #if p is a right child
            if self.right(p) != None:  #if p has right child
                q = self.right(p)
                if self.left(q) != None:
                    c = self.left(q)
                    while self.left(c) != None: #loop to return the furthest left of the subtree
                        c = self.left(c)
                    return c
                else:
                    return q #return right child of p
            
            
            else:
                b = self.parent(p)
                while self.right(self.parent(b)) == b: #loop to see if it is the last of element
                    b = self.parent(b)
                    if b == self.root():
                        return None
                        break
                if self.left(self.parent(b)) == b: 
                    return self.parent(b)
                else:
                    return None

    def preorder_next(self, p):
        """Return the next position from p in preorder tranversal"""
        if self.left(p) != None:
            return self.left(p)
        elif self.right(p) != None:
            return self.right(p)
        
        else:             # if p does not have children
            if self.left(self.parent(p)) == p:    # if p is the left child
                if self.right(self.parent(p)) != None: # if p has a sibling.
                    return self.right(self.parent(p))
                else:                            # if p dont have 
                    q = self.parent(p)           # q la parent cua p
                    while self.sibling(q) == None and self.right(q) == None: #if q has no sibling and right child
                        q = self.parent(q)
                    
                    if q == self.right(self.parent(q)): #if q is the right child
                        return None
                    return self.sibling(q)
                    
                
            if self.right(self.parent(p)) == p:
                q = self.parent(p)
                while self.sibling(q) == None or (self.sibling(q) == self.left(self.parent(q))): #loop to see if it is the last position of the tree
                    q = self.parent(q)
                    if q == self.root():
                        return None
                
                return self.sibling(q)
    
    def delete_subtree_recur(self, p):
        """Delete the subtree rooted at p"""
        if self.left(p) != None:   # if p have left child
            a = self.left(p)       # a is left child of p
            if self.num_children(a) != 0: #if a have children
                temp = self.left(p)        
                self.delete_subtree_recur(temp)  
            self._delete(a)
                
        if self.right(p) != None: #if p have a right child
            a = self.right(p)      # a is right child of p
            if self.num_children(a) != 0: #if a have children        
                temp = self.right(p)
                self.delete_subtree_recur(temp)
            self._delete(a)

    def delete_subtree(self, p):
        self.delete_subtree_recur(p)
        self._delete(p)


import unittest 

class extend_linked_binary_treeTest(unittest.TestCase):
    def test_extend_linked_binary_tree1(self):
        '''Check preorder_next(p), inorder_next(p), postorder_next(p), delete_subtree(p) methods
        with a set of valid data
        '''
        C = ExtendedLinkedBinaryTree()
        p1 = C._add_root(23)
        p2 = C._add_left(p1,15)
        p3 = C._add_left(p2,8)
        p4 = C._add_right(p2,20)
        p5 = C._add_left(p4,19)
        p6 = C._add_right(p4,22)
        p7 = C._add_right(p1,63)
        p8 = C._add_left(p7,32)
        p9 = C._add_right(p7,80)
        p10 =C._add_right(p8,60)
        p11 =C._add_left(p10,50)
        #Test preorder_next(p)
        print('\n')
        print("call preorder")
        a = C.preorder()
        pre1 = []
        for i in a:
            print(i.element(), end = " ")
            pre1.append(i.element())
        print('\n')
        print("test preorder_next")
        node1 = p1
        pre2 = []
        while node1 != None:
            print(node1.element(), end=" ")
            pre2.append(node1.element())
            node1 = C.preorder_next(node1)
        self.assertEqual(pre1, pre2)
        #Test inorder_next(p)
        print('\n')
        print("call inorder")
        b = C.inorder()
        in1 = []
        for i in b:
            print(i.element(), end = " ")
            in1.append(i.element())
        print('\n')
        print("test inorder_next")
        node2 = p3
        in2 = []
        while node2 != None:
            print(node2.element(), end=" ")
            in2.append(node2.element())
            node2 = C.inorder_next(node2)
        self.assertEqual(in1, in2)
        # Test postorder_next(p)
        print('\n')
        print("call postorder")
        c = C.postorder()
        post1 = []
        for i in c:
            print(i.element(), end = " ")
            post1.append(i.element())
        print('\n')
        print("test postorder_next")
        node3 = p3
        post2 = []
        while node3 != None:
            print(node3.element(), end=" ")
            post2.append(node3.element())
            node3 = C.postorder_next(node3)
        self.assertEqual(post1, post2)
        
        # Test delete_subtree(p)
        print('\n')
        print("test delete_subtree")
        C.delete_subtree(p2)
        for i in C.inorder():
            print(i.element(), end = " ")
        '''Element at p2 and its subsequent subtree is deleted, 
        so raise ValueError when delete_subtree(p2) is called again'''
        self.assertRaises(ValueError, C.delete_subtree, p2)
        
    def test_extend_linked_binary_tree2(self):
        '''Check preorder_next(p), inorder_next(p), postorder_next(p), delete_subtree(p) methods
        with another set of valid data
        '''
        t = ExtendedLinkedBinaryTree()
        t1 = t._add_root(10)
        t2 = t._add_left(t1, 3)
        t3 = t._add_right(t1, -7)
        t4 = t._add_left(t2, 24)
        t5 = t._add_right(t2, 53)
        t6 = t._add_left(t3, -9)
        t7 = t._add_right(t3, 33)
        t8 = t._add_right(t4, 41)
        t9 = t._add_left(t5, 20)
        t10 = t._add_left(t6, -17)
        t11 = t._add_right(t6, -21)
        t12 = t._add_left(t7, -1)
        t13 = t._add_right(t7, -10)
        t14 = t._add_left(t9, 22)
        t15 = t._add_left(t12, -2)
        t16 = t._add_left(t13, -8)
        t17 = t._add_right(t11, -36)
        t18 = t._add_right(t14, 14)
        t19 = t._add_right(t17, 5)
        
        # Test preorder_next(p)
        print('\n')
        print("call preorder")
        a = t.preorder()
        pre1 = []
        for i in a:
            print(i.element(), end = " ")
            pre1.append(i.element())
        print('\n')
        print("test preorder_next")
        node1 = t1
        pre2 = []
        while node1 != None:
            print(node1.element(), end=" ")
            pre2.append(node1.element())
            node1 = t.preorder_next(node1)
        self.assertEqual(pre1, pre2)
        
        # Test inorder_next(p)
        print('\n')
        print("call inorder")
        b = t.inorder()
        in1 = []
        for i in b:
            print(i.element(), end = " ")
            in1.append(i.element())
        print('\n')
        print("test inorder_next")
        node2 = t4
        in2 = []
        while node2 != None:
            print(node2.element(), end=" ")
            in2.append(node2.element())
            node2 = t.inorder_next(node2)
        self.assertEqual(in1, in2)
        
        # Test postorder_next(p)
        print('\n')
        print("call postorder")
        c = t.postorder()
        post1 = []
        for i in c:
            print(i.element(), end = " ")
            post1.append(i.element())
        print('\n')
        print("test postorder_next")
        node3 = t8
        post2 = []
        while node3 != None:
            print(node3.element(), end=" ")
            post2.append(node3.element())
            node3 = t.postorder_next(node3)
        self.assertEqual(post1, post2)
        
        # Test delete_subtree(p)
        print('\n')
        print("test delete_subtree")
        t.delete_subtree(t3)
        for i in t.inorder():
            print(i.element(),end = " ")
        '''Element at t3 and its subsequent subtree is deleted, 
        so raise ValueError when delete_subtree(t3) is called again'''
        self.assertRaises(ValueError, t.delete_subtree, t3)
        
        
    def test_extend_linked_binary_tree3(self):
        '''Check preorder_next(p), inorder_next(p), postorder_next(p), delete_subtree(p) methods 
        with invalid data type and value'''
        p = ExtendedLinkedBinaryTree()
        p1 = p._add_root(20)
        p2 = p._add_left(p1, 9)
        p3 = p._add_right(p1, 11)
        p4 = p._add_left(p2, 8)
        t = ExtendedLinkedBinaryTree()
        t1 = t._add_root(32)
        t2 = t._add_left(t1, 2)
        self.assertRaises(TypeError, p.preorder_next, 5)
        self.assertRaises(TypeError, p.preorder_next, 'p3')
        self.assertRaises(ValueError, t.preorder_next, p2)
        self.assertRaises(TypeError, p.inorder_next, 5)
        self.assertRaises(TypeError, p.inorder_next, 'p3')
        self.assertRaises(ValueError, t.inorder_next, p2)
        self.assertRaises(TypeError, p.postorder_next, 5)
        self.assertRaises(TypeError, p.postorder_next, 'p3')
        self.assertRaises(ValueError, t.postorder_next, p2)
        self.assertRaises(TypeError, p.delete_subtree, 5)
        self.assertRaises(TypeError, p.delete_subtree, 'p5')
        self.assertRaises(ValueError, t.delete_subtree, p2)
        
    def test_extend_linked_binary_list4(self):
        L = ExtendedLinkedBinaryTree()
        l1 = L._add_root(1)
        l2 = L._add_left(l1,2)
        l3 = L._add_left(l2,3)
        l4 = L._add_right(l2,4)
        l5 = L._add_left(l4,5)
        l6 = L._add_right(l5,6)
        l7 = L._add_left(l6,7)
        l8 = L._add_left(l7,8)
        l9 = L._add_right(l7,9)
        l10 = L._add_right(l1,10)
        l11 = L._add_left(l10,11)
        l12 = L._add_right(l10,12)
        l13 = L._add_left(l12,13)
        l14 = L._add_left(l13,14)
        l15 = L._add_right(l13,15)
        l16 = L._add_left(l14,16)
        l17 = L._add_left(l16,17)
        l18 = L._add_right(l16,18)
        l19 = L._add_right(l15,19)
        l20 = L._add_right(l19,20)
        l21 = L._add_right(l12,21)
        l22 = L._add_left(l21,22)
        l23 = L._add_left(l22, 23)
        l24 = L._add_right(l21, 24)
        l25 = L._add_right(l24, 25)
         # Test preorder_next(p)
        print('\n')
        print("call preorder")
        a = L.preorder()
        pre1 = []
        for i in a:
            print(i.element(), end = " ")
            pre1.append(i.element())
        print('\n')
        print("test preorder_next")
        node1 = l1
        pre2 = []
        while node1 != None:
            print(node1.element(), end=" ")
            pre2.append(node1.element())
            node1 = L.preorder_next(node1)
        self.assertEqual(pre1, pre2)
        
        # Test inorder_next(p)
        print('\n')
        print("call inorder")
        b = L.inorder()
        in1 = []
        for i in b:
            print(i.element(), end = " ")
            in1.append(i.element())
        print('\n')
        print("test inorder_next")
        node2 = l3
        in2 = []
        while node2 != None:
            print(node2.element(), end=" ")
            in2.append(node2.element())
            node2 = L.inorder_next(node2)
        self.assertEqual(in1, in2)
        
        # Test postorder_next(p)
        print('\n')
        print("call postorder")
        c = L.postorder()
        post1 = []
        for i in c:
            print(i.element(), end = " ")
            post1.append(i.element())
        print('\n')
        print("test postorder_next")
        node3 = l3
        post2 = []
        while node3 != None:
            print(node3.element(), end=" ")
            post2.append(node3.element())
            node3 = L.postorder_next(node3)
        self.assertEqual(post1, post2)
        
        # Test delete_subtree(p)
        print('\n')
        print("test delete_subtree")
        L.delete_subtree(l10)
        for i in L.inorder():
            print(i.element(),end = " ")
        '''Element at t3 and its subsequent subtree is deleted, 
        so raise ValueError when delete_subtree(t3) is called again'''
        self.assertRaises(ValueError, L.delete_subtree, l10)
        
        
        
if __name__=='__main__':
    unittest.main()
