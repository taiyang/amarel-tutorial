# Install R

Since you are using a sharing cluster, you don't have the root access as on your own machine. Package management tools are not allowed to install the package into the locations you don't have write access per your request. Generally you need to install from source.

## Download R source

Go to [CRAN](https://cloud.r-project.org/sources.html), you will see the R sources page. You can choose your own version. Right now, the latest version is 3.5.3. Right click the link and select `Copy Link Address`. To see all versions, you can visit [here](https://cloud.r-project.org/src/base/R-3/).

Now, go to your Amarel terminal, use `wget` to download and extract the R source file.

```bash
$ wget https://cloud.r-project.org/src/base/R-3/R-3.5.3.tar.gz
$ tar -xvzf R-3.5.3.tar.gz
```

Now you will see a folder named `R-3.5.3`. Change directory into it.

```bash
$ cd R-3.5.3
```

## Install R from source

Here, we will install the R into folder `~/.local`. Run the following chunk.

```bash
$ module load intel/17.0.4             # load compiler, you can opt for gcc if you have installed it
$ ./configure --prefix="$HOME/.local"  # Configure install location
$ make                                 # Compile R source
$ make install                         # Install R
```

> Note: You may see several minutes waiting before the compilation completes.

## Export R to the PATH

Right now, you can open R use `~/.local/bin/R`. However, to simplify your life, you can add R into your PATH. Simply run the following chunk.

```bash
$ export PATH="~/.local/bin:$PATH"
# You can then add this line into your bashrc file so that you can use it next time you login
$ echo 'export PATH="~/.local/bin:$PATH"' >> ~/.bashrc
```

Now, you can simply use `R` to open your own version R.

## References

* [R-Project](https://www.r-project.org/)
