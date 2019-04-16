# Login

After you get an account, make sure you are under the Rutgers network (or behind a Rutgers VPN).

## Terminal
### Password Login

You may simply use Rutgers NetID password to login the server. Open a terminal, connect with ssh.

```bash
$ ssh <netid>@amarel.rutgers.edu  # Replace <netid> with yours

```
### SSH-key Login (Optional)
This is a very handy tool. You can opt in this password-less way.
#### Generate your key
The basic program here is `ssh-keygen`.

```bash
$ ssh-keygen
```

After answering several questions, you can generate your key pair in ``~/.ssh/``, the private key `id_rsa` and the public key `id_rsa.pub`. You should never give away your private key. Remember your passphrase unless you left it blank. The passphrase is used to decipher your private key.

#### Put public key on the server

After receiving your key pair, you need to put your public key on the server. You can use a tool called ssh-copy-id.

```bash
$ ssh-copy-id -i ~/.ssh/id_rsa <netid>@amarel.rutgers.edu
```

Or, you may simply use scp to put your public key into the file `~/.ssh/authorized_keys`. Or simply put the content of `id_rsa.pub` into the file.

#### Add your private key to ssh-agent

SSH-Agent can hold your private key, so that you don't need to type your passphrase every time unless you reboot your machine. Type

```bash
$ ssh-add ~/.ssh/id_rsa
```

The agent will ask your passphrase if applicable.
> More information can be found [here](https://www.ssh.com/ssh/keygen/).

## Graphics

You may also use the graphical UI offered by Rutgers. Open the [link](https://ondemand.hpc.rutgers.edu/). This is a great place to launch RStudio or Jupyter Notebook without specific configuration.
