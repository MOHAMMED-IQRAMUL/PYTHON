import re


def main1 () :
    pattern = r"[A-Z]+Code"
    text = "ABCCode DEFCode GHICode JKLCode"
    
    matches = re.findall(pattern, text)
    print(matches)
    print(len(matches))
    
    
main1()
    