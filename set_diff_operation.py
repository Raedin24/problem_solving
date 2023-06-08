line1 = input()
eng_subs = set(map(int, input().split()))

line2 = input()
french_subs = set(map(int, input().split()))

print(len(eng_subs.difference(french_subs)))