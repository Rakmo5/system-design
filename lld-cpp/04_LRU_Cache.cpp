#include <iostream>
#include <unordered_map>
#include <list>

using namespace std;

/*
 * Problem: Design a Least Recently Used (LRU) Cache
 * Pattern: Hash Map + Doubly Linked List
 * Complexity: O(1) Get, O(1) Put
 */

class LRUCache {
private:
    int capacity;
    // list stores {key, value} pairs in order of access (front = most recent, back = least recent)
    list<pair<int, int>> dll;
    // map stores key -> iterator pointing to the node in dll
    unordered_map<int, list<pair<int, int>>::iterator> cache;

public:
    LRUCache(int cap) : capacity(cap) {}

    int get(int key) {
        if (cache.find(key) == cache.end()) {
            return -1; // Key not found
        }
        
        // Move the accessed node to the front of the list (mark as most recently used)
        auto node_it = cache[key];
        int value = node_it->second;
        dll.erase(node_it);
        dll.push_front({key, value});
        cache[key] = dll.begin();
        
        return value;
    }

    void put(int key, int value) {
        // If key already exists, update and move to front
        if (cache.find(key) != cache.end()) {
            dll.erase(cache[key]);
        } 
        // If at full capacity, evict the least recently used element from the back
        else if (dll.size() >= capacity) {
            int lru_key = dll.back().first;
            dll.pop_back();
            cache.erase(lru_key);
        }

        // Insert new element at the front
        dll.push_front({key, value});
        cache[key] = dll.begin();
    }
};

int main() {
    cout << "Testing LRU Cache..." << endl;
    LRUCache lru(2); // Capacity 2

    lru.put(1, 10);
    lru.put(2, 20);
    cout << "get(1): " << lru.get(1) << " (Expected: 10)" << endl; // Returns 10, moves 1 to front

    lru.put(3, 30); // Evicts key 2 (since 1 was recently used)
    cout << "get(2): " << lru.get(2) << " (Expected: -1, evicted)" << endl; // Returns -1

    lru.put(4, 40); // Evicts key 1
    cout << "get(1): " << lru.get(1) << " (Expected: -1, evicted)" << endl; // Returns -1
    cout << "get(3): " << lru.get(3) << " (Expected: 30)" << endl; // Returns 30
    cout << "get(4): " << lru.get(4) << " (Expected: 40)" << endl; // Returns 40

    return 0;
}
