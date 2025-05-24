# frontpagetotext-backend
the backend for frontpage to text, a scratch project

> [!WARNING]
> Remember that this is still in Beta, so expect things to break

> [!NOTE]
> This was made using scratchattach. Check it out [here](https://github.com/TimMcCool/scratchattach/)


# How to use
If you want to use the code, follow the steps below:

**1. Enter your username and session id**

Enter your user name and session id at line 3

If you want to know how to get your session id, click [here](https://github.com/Timbal5p/scratch_python_server_code_timbal5p/blob/main/how_to_get_session_id.md).

**2. Set up your project**

Remix [this](https://scratch.mit.edu/projects/1097547212/) project

**3. Enter your project id**

Copy and paste your project id to line 4

**4. Host the code**

Now, you need to host the code somewhere to keep it online.

**5. Done!**

# FAQ
## Is this safe?
Yes, it is! Your login information will only be used to process the cloud requests using scratchattach.
## What libraries does it need?
This only needs scratchattach to work. Just run ``pip install scratchattach``
## How does it work?
The project first pings the server, then, the project will send a ``get_frontpage_mode_1`` or ``get_frontpage_mode_2_step_(step)`` request to the server, the server converts the frontpage to text and sends it back to the project
## I found a bug!
Dont worry, just open an issue!
