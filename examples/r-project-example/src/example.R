# This Rscript is an example of running R files on Rutgers Amarel.

# Open standard input stream
f <- file("stdin")
open(f)

# Read arguments
arg1 <- as.numeric(readLines(f, n=1))

arg2 <- as.numeric(readLines(f, n=1)

paste("arg1=", arg1)
paste("arg2=", arg2)
