import numpy as np

psych_words = np.array(["persuasion", "central route to persuasion", "peripheral route to persuasion", "credibility", "sleeper effect", "attractiveness", "foot-in-the-door phenomenon", "lowball technique", "door-in-the-face technique", "primacy effect", "recency effect", "channel of communication", "two-step flow of communication", "need for cognition", "attitude inoculation", "counterarguments", "group", "social facilitation", "evaluation apprehension", "social loafing", "free riders", "deindividuation", "self-awareness", "group polarization", "groupthink", "leadership", "task leadership", "social leadership", "transformational leadership"])

print(np.random.choice(psych_words, 100))