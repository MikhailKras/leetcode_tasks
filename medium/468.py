class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        ipv4 = queryIP.split('.')
        if len(ipv4) == 4:
            for item in ipv4:
                if not item.isdigit() or int(item) > 255 or (item.startswith('0') and item != '0'):
                    return 'Neither'
            return 'IPv4'
        
        ipv6 = queryIP.split(':')
        if len(ipv6) == 8:
            for item in ipv6:
                if not item or len(item) > 4:
                    return 'Neither'
                for char in item:
                    if not char.isdigit():
                        if char.lower() not in {'a', 'b', 'c', 'd', 'e', 'f'}:
                            return 'Neither'
            return 'IPv6'
        
        return 'Neither'

