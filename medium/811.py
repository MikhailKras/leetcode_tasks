class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = {}
        for cpdomain in cpdomains:
            num, domain = cpdomain.split()
            domain_list = domain.split('.')
            while domain_list:
                cur_domain = '.'.join(domain_list)
                counter[cur_domain] = counter.get(cur_domain, 0) + int(num)
                domain_list.pop(0)
        res = []
        for key, value in counter.items():
            res.append(f"{value} {key}")
        return res

