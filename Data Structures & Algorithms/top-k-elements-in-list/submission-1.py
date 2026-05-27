class Solution:
    '''
    We have two things to do:
    1. Count the frequency of each element - O(n)
    2. Efficiently get the K most frequent ones - O(n) + O(k*logn)

    We can get the frequencies by iterating the list and storing them in
    a dictionary, the key is the element and the value is its frequency.

    Then, since we may have have k < n, we can use a max heap to get the k elements.
    1. We convert the dictionary into an array of tuples, where the first element is
    the frequency so we can order them by frequency.
    2. We heapify the array of frequencies - O(n)
    3. We pop the k most frequent elements - O(logn) k times
    4. Return the k most frequent elements

    We can improve this solution by just keeping in the heap the k most frequent elements
    We can do this by storing one by one in a MinHeap, whenever the heap is bigger than k
    we pop from the heap. At the end we pop the elements from the heap and that is our result.
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Built-in DS to get frequency of elements
        frequencies = Counter(nums)

        heap = []
        for n, freq in frequencies.items():
            heapq.heappush(heap, (freq, n))
            # We pop the smallest element from the heap, keeping the biggest values there
            if len(heap) > k:
                heapq.heappop(heap)

        results = [n for _, n in heap]

        return results