class Solution:
    def intToRoman(self, num: int) -> str:
        dct = {1: 'I', 4: 'IV', 5: 'V',
               9: 'IX', 10: 'X', 40: 'XL',
               50: 'L', 90: 'XC', 100: 'C',
               400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}

        sum_num = 0
        num_keys = sorted(dct, reverse=True)
        i = 0
        copy_num = num
        roman_num = ''
        while sum_num != num:
            while copy_num >= num_keys[i]:
                sum_num += num_keys[i]
                copy_num -= num_keys[i]
                roman_num += dct[num_keys[i]]
            else:
                if i < len(num_keys) - 1:
                    i += 1
        return roman_num
