from typing import Optional
import linked_list as LinkedList

#this uses Floy'd cycle detection algorithm
def start_of_loop(head: LinkedList.Node) -> Optional[LinkedList.Node]:    
    p = has_loop(head)
    if p:
        q = head
        while p != q:
            p = p.next
            q = q.next
        return p
    return None

#if the linked list contains a loop, return the  
def has_loop(head: LinkedList.Node) -> Optional[LinkedList.Node]:
    p = head
    q = head
    while p and q and q.next:
        p = p.next
        q = q.next.next
        if p == q:
            return p
    return None