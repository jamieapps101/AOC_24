# Source this from a bash-like shell

if [ ! -d .venv ] ; then
    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install -r requirements.txt
else
    source .venv/bin/activate
fi