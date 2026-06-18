class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        minute_angle = minutes * 6

        hour_angle = (hour % 12) * 30 + minutes * 0.5
        angle = abs(hour_angle - minute_angle)

        return min(angle, 360 - angle)