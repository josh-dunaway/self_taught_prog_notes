from typing import Optional
import linked_list as LinkedList

#this uses Floy'd cycle detection algorithm
def start_of_cycle(head: LinkedList.Node) -> Optional[LinkedList.Node]:    
    pointer1 = has_cycle(head)
    if pointer1:
        pointer2 = head
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1
    return None

#if the linked list contains a loop, return the  
def has_cycle(head: LinkedList.Node) -> Optional[LinkedList.Node]:
    slow = head
    fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow
    return None