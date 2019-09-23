#include <iostream>
using namespace std;

class ListNode{
public:
    int data;
    ListNode* prev;
    ListNode* next;

    // Constructor
     ListNode (int data = 0, ListNode* p = nullptr, ListNode* n = nullptr)  {
        this->data = data;
        this->prev = p;
        this->next = n;
     };
};

class List {
private:
    // Data stored in a list
    int _size;
    ListNode head;
    ListNode tail;

public:
    // Constructor
    List() {
        head.next = &tail;
        tail.prev = &head;
        _size = 0;
    }

    // Read-only operations
    int size() {return _size;};
    int first() {
        if (_size > 0) return head.next->data;
        else throw "error";
    };
    int last() {
        if (_size > 0) return tail.prev->data;
        else throw "error";
    };

    // Write operations
    int insertAsFirst(int data) {
        // Should check boundary conditions first but omitted here

        // Create new node
        ListNode* node = new ListNode(data);

        // Change current First node
        ListNode* curFirst = head.next;
        curFirst->prev = node;

        // Insert newNode into place
        head.next = node;
        node->prev = &head;
        node->next = curFirst;

        // Increase size
        _size++;
        return node->data;
    }

    int deleteFirst() {
        // Should check boundary conditions first but omitted here

        ListNode* curFirst = head.next;
        // head.next points to the second element
        head.next = curFirst->next;
        // second element's prev points to head
        head.next->prev = &head;
        return curFirst->data;
    }
};

int main() {
    List list;
    list.insertAsFirst(6);
    list.insertAsFirst(5);
    list.insertAsFirst(4);
    cout << "After insertion, we have elements [4, 5, 6]" << endl;
    cout << "The first element is " << list.first() << endl;
    cout << "The last element is " <<  list.last() << endl;
    list.deleteFirst();
    cout << "After deleting first, we have elements [5, 6]" << endl;
    cout << "The first element is " << list.first() << endl;
    cout << "The last element is " <<  list.last() << endl;
    return 0;
}
