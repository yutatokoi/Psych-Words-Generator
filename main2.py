import numpy as np

psych_words = np.array(["prejudice", "stereotype", "discrimination", "social dominance orientation", "authoritarian personality", "realistic group conflict theory", "social identity", "ingroup", "outgroup", "ingroup bias", "outgroup homogeneity", "own-race bias", "group-serving bias", "just-world phenomenon", "subtyping", "subgrouping", "stereotype threat", "cyberbullying", "aggression", "physical aggression", "social aggression", "hostile aggression", "instrumental aggression", "frustration-aggression theory", "frustration", "displacement", "relative deprivation", "social learning theory", "prosocial behavior", "catharsis"])

print(np.random.choice(psych_words, 100))