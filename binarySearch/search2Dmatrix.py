# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

# Output: true

def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    # jadi kita initialize dlu si ujung2 pointernya (oiya m itu baris dan n itu kolom)
    m,n = len(matrix), len(matrix[0])
    left, right = 0, (m*n)-1

    # mulai deh geser geser
    while left<=right:
        mid = left+(right-left)//2 # ini si pointer tengahnya
        # tengah row kan brati kita bagikan dia dg si n(jum kolomnya)
        mid_row = mid//n
        mid_col = mid%n
        mid_value = matrix[mid_row][mid_col] # mngambil nilai tengahnya

        if mid_value == target:
            return True
        elif mid_value<target:
            left = mid+1
        else:
            right = mid-1
    return False


# contoh case 
# searchMatrix(matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10)