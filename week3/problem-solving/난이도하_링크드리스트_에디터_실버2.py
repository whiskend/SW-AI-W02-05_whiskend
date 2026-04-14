# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406

class Node:
    def __init__(self, char=None):
        self.item = char
        self.prev = None
        self.next = None

list1 = list(input().rstrip())
size = len(list1)

ll = []
for i in range(size):
    ll.append(Node(list1[i]))
        
for i in range(0, size):
    if 0 < i:
        ll[i].prev = ll[i-1]
    if i < size-1:
        ll[i].next = ll[i+1]

head = Node()
tail = Node()

if size == 0:
    head.next = tail
    tail.prev = head
    cursor = head
else:
    head.next = ll[0]
    ll[0].prev = head
    ll[-1].next = tail
    tail.prev = ll[-1]
    cursor = ll[-1] # cursor는 맨 끝에서 시작해

m = int(input())

for _ in range(m):
    move = input().split()

    if move[0] == 'L':
        if cursor != head:
            cursor = cursor.prev
    elif move[0] == 'D':
        if cursor.next != tail:
            cursor = cursor.next
    
    elif move[0] == 'B':
        if cursor != head:
            delete_node = cursor
            left_node = delete_node.prev
            right_node = delete_node.next

            left_node.next = right_node
            right_node.prev = left_node
            cursor = left_node

    elif move[0] == 'P':
        new_node = Node(move[1])

        right_node = cursor.next
        cursor.next = new_node
        new_node.prev = cursor
        new_node.next =right_node
        right_node.prev = new_node

        cursor = new_node

result = []
cur = head.next
while cur != tail:
    result.append(cur.item)
    cur = cur.next

print(''.join(result))