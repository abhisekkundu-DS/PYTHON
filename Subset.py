def isSubset(a, b):

    # Create a hash set and insert all elements of arr1
    hash_set = set(a)

    # Check each element of arr2 in the hash set
    for num in b:
        if num not in hash_set:
            return False

    # If all elements of arr2 are found in the hash set
    return True


if __name__ == "__main__":
  a = [11, 1, 13, 21, 3, 7]
  b = [11, 3, 7, 1]

  if isSubset(a, b):
      print("true")
  else:
      print("false")
