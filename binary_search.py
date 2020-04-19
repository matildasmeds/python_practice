import math

def main():
    def get_offset(j, i):
        return int(math.floor((j-i) / 2))

    def binary_search(arr, t):

        i = 0  # Beginning of subarray
        j = len(arr)  # End of subarray
        k = get_offset(j, i)  # Initial midpoint
        print(f"Begin with i: {i}, j: {j}, k: {k}")
        while (True):
            print(f"Sub-array: {arr[i:j]}")

            if j == i:
                return None
            if j - i == 1:
                if arr[i] == t:
                    print(f"Result: {i}")
                    return i
                else:
                    return None

            if arr[k] == t:
                print(f"Result: {k}")
                return k
            if arr[k] > t:
                j = k
                k -= get_offset(j, i)
                print(f"Process left half with i: {i}, j: {j}, and k: {k}")
            else:
                i = k
                k += get_offset(j, i)
                print(f"Process right half with i: {i}, j: {j}, and k: {k}")


    # Jotakin satunnaisia testicaseja
    arr = [0,1,2,7,18,34,35,47]
    print("---")
    print("Assert -1 --> None")
    assert(binary_search(arr, -1) == None)
    print("---")
    print("Assert 0 --> 0")
    assert(binary_search(arr, 0) == 0)
    print("---")
    print("Assert 2 --> 2")
    assert(binary_search(arr, 2) == 2)
    print("---")
    print("Assert 3 --> None")
    assert(binary_search(arr, 3) == None)
    print("---")
    print("Assert 18 --> 4")
    assert(binary_search(arr, 18) == 4)
    print("---")
    print("Assert 47 --> 7")
    assert(binary_search(arr, 47) == 7)
    assert(binary_search(arr, 50) == None)

    arr.pop()

    assert(binary_search(arr, 0) == 0)
    assert(binary_search(arr, 7) == 3)
    assert(binary_search(arr, 47) == None)

    assert(binary_search([], 42) == None)
    assert(binary_search([1], 42) == None)
    assert(binary_search([1], 1) == 0)

    arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    assert(binary_search(arr, 8) == 7)

if __name__ == "__main__":
    main()
