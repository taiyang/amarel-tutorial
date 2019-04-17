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

### Modifying Source Files
#### Taking Args From Command Line

In R, we can use `commandArgs` to get arguments from command line.

```R
# Put this in your source file
args <- commandArgs(trailingOnly = T)
textArg <- args[1]
# Explicit type conversion is needed for numeric arg
numericArg <- as.numeric(args[2])
```

#### Taking Args From Input File

Unlike many programming languages, you need to open standard input stream manually. Add the snippet below in your source file to do so.

```R
# Open standard input stream
f <- file("stdin")
open(f)

# Read arguments
textArg <- readLines(f, n=1)
# Explicit type conversion is needed as well
numericArg <- as.numeric(readLines(f, n=1)
```

This assumes the input file feeding one argument per line.

### Generating Input Files

Here I'm offering a [Python script](../src/input-gen.py) automatically generating the input files. To use the script, consider put it into your `PATH`. You may follow this tutoiral.

```bash
# If you don't create your own local folder. Please run this chunk.
# From Amarel terminal through ssh
$ mkdir -p ~/.local/bin
$ export PATH="~/.local/bin:$PATH"
# You can then add this line into your bashrc file so that you can use it next time you login
$ echo 'export PATH="~/.local/bin:$PATH"' >> ~/.bashrc
```

If you have already done the first part, you can continue here to "install" the script.

```bash
# From the terminal from your local machine
$ cd ~/Downloads/  # Assume you download the script into this folder
$ scp input-gen.py <netid>@amarel.rutgers.edu:~/.local/bin/input-gen

# From Amarel terminal through ssh
$ chmod u+x ~/.local/bin/input-gen
```

Now, you may use this script to create your input files. For example, if your job have two variables, arg1 and arg2, you can create a file `input` like this

```
1 2 3
100 200 300
```

And then you run the script

```bash
$ input-gen ./input/input  # Assume you are in your project root.
```

You will end up with 9 input files in the folder `./input/`, with name from `input.0` to `input.8`.

### Write Your Own SBATCH Script

You may look at the [example file](../examples/r-project-example/run).

## Submit Your Job

Simply run the following command from the project directory.

```bash
$ sbatch run
```

## References

* [An example of project structure](../examples/r-project-example)
* [Slurm Documentation](https://slurm.schedmd.com/documentation.html)
