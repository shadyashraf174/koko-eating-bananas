def minEatingSpeed(piles, h):
    def canEatAllBananas(k):
        hours = 0
        for pile in piles:
            hours += (pile + k - 1) // k  # equivalent to ceil(pile / k)
        return hours <= h

    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        if canEatAllBananas(mid):
            right = mid
        else:
            left = mid + 1
    return left