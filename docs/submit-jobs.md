# Submit Jobs

## Preparation
### Project Structure
Normally, I would like to use the following project structure.

```
.
|____img/    # For `.RData` files
|____input/  # For input files
|____out/    # For output files
|____run     # The sbatch script
|____src/    # The source `.R` files
```

### Taking Args From Command Line
In R, we can use `commandArgs` to get arguments from command line.

```R
# Put this in your source file
args <- commandArgs(trailingOnly = T)
textArg <- args[1]
# Explicit type conversion is needed for numeric arg
numericArg <- as.numeric(args[2])
```

### Taking Args From Input File
Unlike many programming languages, you need to open standard input stream manually. Add the snippet below in your source file to do so.

```R
# Open standard input stream
f <- file("stdin")
open(f)

# Read arguments
textArg <- readLines(f, n=1)
# Explicit type conversion is needed as well
numericArgs <- as.numeric(readLines(f, n=1)
```

This assumes the input file feeding one argument per line.
