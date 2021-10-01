from random import choice
questions=["Why the sky is blue?:", "Where are the dinosaures now?:","Why is there a face on the moon?:"]

question=choice(questions)
answer=input(question).strip().lower()

while answer != "just because":
    answer=input("why? :").strip().lower()

print("Oh..okkay")    