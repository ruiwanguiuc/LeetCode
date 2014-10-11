# https://oj.leetcode.com/problems/gas-station/

# There are N gas stations along a circular route,
# where the amount of gas at station i is gas[i].
# You have a car with an unlimited gas tank and 
# it costs cost[i] of gas to travel from station i 
# to its next station (i+1). You begin the journey 
# with an empty tank at one of the gas stations.

# Return the starting gas station's index if you can 
# travel around the circuit once, otherwise return -1.

# Note:
# The solution is guaranteed to be unique.

class Solution:
# MyNote: First need to get the trick that you don't need to
# check the index that you already traveled. This trick reduces
# run time from N^2 to N.
# Then need to consider several different cases when start travel
# from index i:
# 1. Can't move at all.
# 2. Traveled a bit but didn't go beyond index 0.
# 3. Traveled a bit and went beyond index 0. (should return -1)
# 4. Traveld around and completed the circuit.
# Need to distinguish Case 1 and 4.


    def can_complete_circuit(self, gas, cost):
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
        i = 0
        while i < len(gas):
            farthest, ever_moved = self.start_travel_at(i, gas, cost)
            # have completed the circuit!
            if farthest == i and ever_moved:
                return i
            # moved beyond index 0 but didn't complete the circuit.
            # indicating there is no way to complete.
            if farthest < i:
                return -1
            # either normal case(traveled a bit but didn't go beyond
            # index 0) or didn't move at all.
            else: 
                i = farthest + 1
        return -1

    def start_travel_at(self, i, gas, cost):
    # @return the index of the farthest station you can get
    # and a boolean indicating if you ever moved.
        if gas[i] < cost[i]:
            return i, False
        initial = i
        cur_gas = 0
        while cur_gas >= 0:
            cur_gas += gas[i]
            cur_gas -= cost[i]
            i += 1
            if i == len(gas):
                i = 0
            if initial == i and cur_gas >= 0:
                return initial, True
        return i - 1, True

if __name__ == "__main__":
    print Solution().can_complete_circuit([4], [5])
    print Solution().can_complete_circuit([5,2,10,5,2], [2,7,1,5,1])