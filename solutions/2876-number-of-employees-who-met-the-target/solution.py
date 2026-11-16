class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        res = 0
        for employee_hours in hours:
            if employee_hours >= target:
                res += 1

        return res
