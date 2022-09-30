Awesome work! You just about nailed the implementation. I really like the idea to use pandas to store the scoring matrix. I will note, to make your code work with ANY input scoring matrix, you can just do `scoring_df = pd.read_csv(sys.argv[2], header=0, index_col=0, delim_whitespace=True)`. That'll set up the index and header properly for any scoring matrix, without assuming the order of the amino acids or nucleotides in the file. There was one minor issue:

When you're filling in the matricies and when you're doing traceback, it looks like you're using `U` to move left, and `L` to move up. However, when you initialize the traceback matrix, you have this the other way around. It looks like this has a small effect on your alignment and alignment stats (-0.25)

Otherwise, excellent work.

9.75/10
