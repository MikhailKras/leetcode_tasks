class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            name, domain = email.split("@")
            name = name.split("+")[0]
            name = name.replace(".", "")
            seen.add(name + "@" + domain)
        return len(seen)

